/*
 * SPDX-FileCopyrightText: 2023-2025 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <soc/gpio_num.h>
#include <soc/rtc_io_periph.h>
#include <soc/uart_periph.h>
#include <soc/gpio_struct.h>
#include <soc/uart_struct.h>
#include <soc/lpperi_struct.h>
#include <soc/rtc.h>
#include <hal/gpio_ll.h>
#include <hal/gpio_types.h>
#include <hal/uart_ll.h>
#include <hal/uart_types.h>
#include <hal/uart_hal.h>
#include <hal/rtc_io_ll.h>
#include <hal/clk_tree_ll.h>

#include <esp_err.h>
#include <lp_core_uart.h>
#include <ulp_lp_core_utils.h>

#include <esp_amp_platform.h>

#include "uart.h"

#define UART_HW_FIFO_LEN(uart_num) ((uart_num < SOC_UART_HP_NUM) ? SOC_UART_FIFO_LEN : SOC_LP_UART_FIFO_LEN)

#define UART_ERR_INT_FLAG         (UART_INTR_PARITY_ERR | UART_INTR_FRAM_ERR)
#define UART_TX_INT_FLAG          (UART_INTR_TX_DONE)
#define UART_RX_INT_FLAG          (UART_INTR_RXFIFO_FULL | UART_INTR_RXFIFO_TOUT | UART_INTR_RXFIFO_OVF)
#define UART_TOUT_THRESH_DEFAULT  (10U)
#define UART_FULL_THRESH_DEFAULT  (10U)
#define UART_TX_IDLE_NUM_DEFAULT        (0)

static const char* TAG = "UART";

static inline void gpio_matrix_in(int gpio_num, uint32_t signal_idx, bool inv)
{
    gpio_func_in_sel_cfg_reg_t reg;
    reg.in_sel = gpio_num;
    reg.in_inv_sel = inv;
    reg.sig_in_sel = 1;
    GPIO.func_in_sel_cfg[signal_idx].val = reg.val;
}

static inline void gpio_matrix_out(int gpio_num, uint32_t signal_idx, bool out_inv, bool oen_inv)
{
    gpio_func_out_sel_cfg_reg_t reg;
    reg.out_sel = signal_idx;
    reg.out_inv_sel = out_inv;
    reg.oen_inv_sel = oen_inv;
    GPIO.func_out_sel_cfg[gpio_num].val = reg.val;
}

static esp_err_t lp_core_uart_check_timeout(uart_hal_context_t hal, uint32_t intr_mask, int32_t timeout, uint32_t *ticker)
{
    if (timeout > -1) {
        /* If the timeout value is not -1, delay for 1 CPU cycle and keep track of ticks */
        ulp_lp_core_delay_cycles(1);
        *ticker = *ticker + 1;
        if (*ticker >= timeout) {
            /* Disable and clear interrupt bits */
            uart_hal_disable_intr_mask(&hal, intr_mask);
            uart_hal_clr_intsts_mask(&hal, intr_mask);

            return ESP_ERR_TIMEOUT;
        }
    }

    return ESP_OK;
}

static esp_err_t uart_config_io(gpio_num_t pin, uint32_t idx, uart_port_t uart_port)
{
    /* Skip configuration if the IO is -1 */
    if (pin < 0) {
        return ESP_OK;
    }

    const uart_periph_sig_t *upin = &uart_periph_signal[uart_port].pins[idx];

#if !SOC_LP_GPIO_MATRIX_SUPPORTED && SOC_UART_LP_NUM >= 1
    if (uart_port >= LP_UART_NUM_0 && pin != upin->default_gpio) {
        printf("%s: uart port does not suport gpio matrix use default gpio\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }
#endif

    /* Connect pins */
    gpio_dev_t *gpio_dev = GPIO_LL_GET_HW(GPIO_PORT_0);

    if (uart_port < SOC_UART_HP_NUM) {
        if (!(upin->iomux_func == -1 || upin->default_gpio == -1 || upin->default_gpio != pin)) {
            gpio_ll_iomux_out(gpio_dev, pin, upin->iomux_func, false);

            /* If the pin is input, we also have to redirect the signal,
         * in order to bypasse the GPIO matrix. */
            if (upin->input) {
                gpio_ll_iomux_in(gpio_dev, pin, upin->signal);
            }
        } else {
            gpio_ll_func_sel(gpio_dev, pin, PIN_FUNC_GPIO);

            if (idx == SOC_UART_RX_PIN_IDX) {
                    gpio_ll_pulldown_dis(gpio_dev, pin);
                    gpio_ll_pullup_en(gpio_dev, pin);

                    /* set gpio as input only */
                    gpio_ll_input_enable(gpio_dev, pin);
                    gpio_ll_output_disable(gpio_dev, pin);
                    gpio_ll_od_disable(gpio_dev, pin);

                    gpio_matrix_in(pin, UART_PERIPH_SIGNAL(uart_port, SOC_UART_RX_PIN_IDX), 0);
            } else if (idx == SOC_UART_TX_PIN_IDX) {

                gpio_ll_set_level(gpio_dev, pin, 1);
                gpio_matrix_out(pin, UART_PERIPH_SIGNAL(uart_port, SOC_UART_TX_PIN_IDX), 0, 0);

            } else if (idx == SOC_UART_RTS_PIN_IDX) {

                /* set gpio as output only */
                gpio_ll_output_enable(gpio_dev, pin);
                gpio_ll_input_disable(gpio_dev, pin);
                gpio_ll_od_disable(gpio_dev, pin);

                gpio_matrix_out(pin, UART_PERIPH_SIGNAL(uart_port, SOC_UART_RTS_PIN_IDX), 0, 0);
            } else if (idx == SOC_UART_CTS_PIN_IDX) {
                /* pull_up only */
                gpio_ll_pulldown_dis(gpio_dev, pin);
                gpio_ll_pullup_en(gpio_dev, pin);

                /* GPIO input enable */
                gpio_ll_input_enable(gpio_dev, pin);
                gpio_ll_output_disable(gpio_dev, pin);
                gpio_ll_od_disable(gpio_dev, pin);

                gpio_matrix_in(pin, UART_PERIPH_SIGNAL(uart_port, SOC_UART_CTS_PIN_IDX), 0);
            } else {
                printf("%s: configuring invalid index\n", TAG);
                return ESP_ERR_INVALID_ARG;
            }
        }
    } else {
        if (upin->input) {
            rtcio_ll_output_mode_set(pin, RTCIO_LL_OUTPUT_NORMAL);
            rtcio_ll_output_disable(pin);
            rtcio_ll_input_enable(pin);
        } else {
            rtcio_ll_output_mode_set(pin, RTCIO_LL_OUTPUT_NORMAL);
            rtcio_ll_output_enable(pin);
            rtcio_ll_input_disable(pin);
        }
        /* Enable LP clock */
        LPPERI.clk_en.lp_io_ck_en = true;
        rtcio_ll_function_select(rtc_io_num_map[pin], RTCIO_LL_FUNC_RTC);

        rtcio_ll_iomux_func_sel(rtc_io_num_map[pin], upin->iomux_func);
    }

    return ESP_OK;
}

esp_err_t uart_init(uart_port_t uart_port, uart_cfg_t cfg)
{

    uart_hal_context_t hal = {
        .dev = (uart_dev_t*)UART_LL_GET_HW(uart_port),
    };

    if (uart_port < SOC_UART_HP_NUM) {
        uart_ll_disable_intr_mask(hal.dev, UART_LL_INTR_MASK);
        uart_ll_clr_intsts_mask(hal.dev, UART_LL_INTR_MASK);
        uart_ll_clr_intsts_mask(hal.dev, UART_LL_INTR_MASK);

        uart_ll_enable_bus_clock(uart_port, true);
        uart_ll_reset_register(uart_port);

        soc_module_clk_t uart_sclk_sel = UART_SCLK_DEFAULT;
        uart_ll_set_sclk(hal.dev, uart_sclk_sel);
    } else {
        _lp_uart_ll_enable_bus_clock(0, true);
        LP_CLKRST.lpperi.lp_uart_clk_sel = 0;
    }

    /* initialise uart with default configurations */
    uart_hal_init(&hal, uart_port);

    if (uart_port < SOC_UART_HP_NUM) {
        uint32_t source_freq = CLK_LL_PLL_80M_FREQ_MHZ * MHZ;
        uart_ll_set_baudrate(hal.dev, cfg.uart_proto_cfg.baud_rate, source_freq);
    } else {
        if ((int)LP_UART_SCLK_DEFAULT == (int)SOC_MOD_CLK_RTC_FAST) {
            uint32_t source_freq = (rtc_clk_xtal_freq_get() * MHZ) >> 1;
            lp_uart_ll_set_baudrate(hal.dev, cfg.uart_proto_cfg.baud_rate, source_freq);
        } else {
            printf("%s: failed to configure the clock\n", TAG);
            return ESP_FAIL;
        }
    }

    /* Override protocol parameters from the configuration */
    uart_ll_set_parity(hal.dev, cfg.uart_proto_cfg.parity);
    uart_ll_set_data_bit_num(hal.dev, cfg.uart_proto_cfg.data_bits);
    uart_ll_set_stop_bits(hal.dev, cfg.uart_proto_cfg.stop_bits);
    uart_ll_set_tx_idle_num(hal.dev, UART_TX_IDLE_NUM_DEFAULT);
    uart_ll_set_hw_flow_ctrl(hal.dev, cfg.uart_proto_cfg.flow_ctrl, cfg.uart_proto_cfg.rx_flow_ctrl_thresh);

    /* Reset Tx/Rx FIFOs */
    uart_ll_txfifo_rst(hal.dev);
    uart_ll_rxfifo_rst(hal.dev);

    esp_err_t err = ESP_OK;

    /* Configure Tx Pin */
    err = uart_config_io(cfg.uart_pin_cfg.tx_io_num, SOC_UART_TX_PIN_IDX, uart_port);
    if (err != ESP_OK) {
        printf("%s: Failed to configure tx io: %d\n", TAG, cfg.uart_pin_cfg.tx_io_num);
        return err;
    }
    /* Configure Rx Pin */
    err = uart_config_io(cfg.uart_pin_cfg.rx_io_num, SOC_UART_RX_PIN_IDX, uart_port);
    if (err != ESP_OK) {
        printf("%s: Failed to configure rx io: %d\n", TAG, cfg.uart_pin_cfg.rx_io_num);
        return err;
    }
    /* Configure RTS Pin */
    err = uart_config_io(cfg.uart_pin_cfg.rts_io_num, SOC_UART_RTS_PIN_IDX, uart_port);
    if (err != ESP_OK) {
        printf("%s: Failed to configure rts io: %d\n", TAG, cfg.uart_pin_cfg.rts_io_num);
        return err;
    }
    /* Configure CTS Pin */
    err = uart_config_io(cfg.uart_pin_cfg.cts_io_num, SOC_UART_CTS_PIN_IDX, uart_port);
    if (err != ESP_OK) {
        printf("%s: Failed to configure cts io: %d\n", TAG, cfg.uart_pin_cfg.cts_io_num);
        return err;
    }

    return ESP_OK;
}

esp_err_t uart_write_bytes(uart_port_t uart_num, const void *src, size_t size, int32_t timeout)
{
    if (size > UART_HW_FIFO_LEN(uart_num)) {
        printf("%s: write failed, data buffer size exceeds fifo limit\n", TAG);
        return ESP_FAIL;
    }
    esp_amp_platform_intr_disable();
    uart_hal_context_t hal = {
        .dev = (uart_dev_t*)UART_LL_GET_HW(uart_num),
    };
    /* Argument sanity check */
    if (!src) {
        esp_amp_platform_intr_enable();
        /* Invalid input arguments */
        return ESP_ERR_INVALID_ARG;
    }

    /* Nothing to do if the length is 0 */
    if (size == 0) {
        esp_amp_platform_intr_enable();
        return ESP_OK;
    }

    /* Enable the Tx done interrupt */
    uint32_t intr_mask = UART_TX_INT_FLAG | UART_ERR_INT_FLAG;
    uart_hal_clr_intsts_mask(&hal, intr_mask);
    uart_hal_ena_intr_mask(&hal, intr_mask);

    /* Transmit data */
    uint32_t tx_len;
    uint32_t bytes_sent = 0;
    int32_t remaining_bytes = size;
    esp_err_t ret = ESP_OK;
    uint32_t intr_status = 0;
    uint32_t to = 0;

    while (remaining_bytes > 0) {
        /* Write to the Tx FIFO */
        tx_len = 0;
        uart_hal_write_txfifo(&hal, src + bytes_sent, remaining_bytes, &tx_len);

        if (tx_len) {
            /* We have managed to write some data to the Tx FIFO. Check Tx interrupt status */
            while (1) {
                /* Fetch the interrupt status */
                intr_status = uart_hal_get_intsts_mask(&hal);
                if (intr_status & UART_TX_INT_FLAG) {
                    /* Clear interrupt status and break */
                    uart_hal_clr_intsts_mask(&hal, intr_mask);
                    break;
                } else if ((intr_status & UART_ERR_INT_FLAG)) {

                    esp_amp_platform_intr_enable();
                    /* Transaction error. Abort */
                    return ESP_FAIL;
                }

                /* Check for transaction timeout */
                ret = lp_core_uart_check_timeout(hal, intr_mask, timeout, &to);
                if (ret == ESP_ERR_TIMEOUT) {
                    /* Timeout */
                    uart_hal_disable_intr_mask(&hal, intr_mask);
                    esp_amp_platform_intr_enable();
                    return ret;
                }
            }

            /* Update the byte counters */
            bytes_sent += tx_len;
            remaining_bytes -= tx_len;
        } else {
            /* Tx FIFO does not have empty slots. Check for transaction timeout */
            ret = lp_core_uart_check_timeout(hal, intr_mask, timeout, &to);
            if (ret == ESP_ERR_TIMEOUT) {
                /* Timeout */
                uart_hal_disable_intr_mask(&hal, intr_mask);
                esp_amp_platform_intr_enable();
                return ret;
            }
        }
    }

    /* Disable the Tx done interrupt */
    uart_hal_disable_intr_mask(&hal, intr_mask);
    esp_amp_platform_intr_enable();
    return ret;
}

int uart_read_bytes(uart_port_t uart_num, void *buf, size_t size, int32_t timeout)
{
    if (size > UART_HW_FIFO_LEN(uart_num)) {
        printf("%s: read failed, data buffer size exceeds fifo limit\n", TAG);
        return -1;
    }

    uart_hal_context_t hal = {
        .dev = (uart_dev_t*)UART_LL_GET_HW(uart_num),
    };

    /* Argument sanity check */
    if (!buf) {
        /* Invalid input arguments */
        return -1;
    }

    /* Nothing to do if the length is 0 */
    if (size == 0) {
        return 0;
    }

    /* Set the Rx interrupt thresholds */
    uart_hal_set_rx_timeout(&hal, UART_TOUT_THRESH_DEFAULT);
    uart_hal_set_rxfifo_full_thr(&hal, UART_FULL_THRESH_DEFAULT);

    /* Enable the Rx interrupts */
    uint32_t intr_mask = UART_RX_INT_FLAG | UART_ERR_INT_FLAG;
    uart_hal_clr_intsts_mask(&hal, intr_mask);
    // uart_hal_ena_intr_mask(&hal, intr_mask);

    /* Receive data */
    int rx_len = 0;
    uint32_t bytes_rcvd = 0;
    int32_t remaining_bytes = size;
    esp_err_t ret = ESP_OK;
    uint32_t intr_status = 0;
    uint32_t to = 0;

    while (remaining_bytes > 0) {
        /* Read from the Rx FIFO
         * We set rx_len to -1 to read all bytes in the Rx FIFO
         */
        int fifo_len = uart_hal_get_rxfifo_len(&hal);
        rx_len = (remaining_bytes < fifo_len) ? remaining_bytes : fifo_len;
        if (rx_len > 0) {
            uart_hal_read_rxfifo(&hal, (uint8_t *)(buf + bytes_rcvd), &rx_len);
        }

        if (rx_len) {
            /* We have some data to read from the Rx FIFO. Check Rx interrupt status */
            intr_status = uart_hal_get_intsts_mask(&hal);
            if ((intr_status & UART_INTR_RXFIFO_FULL) ||
                    (intr_status & UART_INTR_RXFIFO_TOUT)) {
                /* This is expected. Clear interrupt status and break */
                uart_hal_clr_intsts_mask(&hal, intr_mask);
                break;
            } else if ((intr_status & UART_INTR_RXFIFO_OVF)) {
                /* We reset the Rx FIFO if it overflows */
                uart_hal_clr_intsts_mask(&hal, intr_mask);
                uart_hal_rxfifo_rst(&hal);
                break;
            } else if ((intr_status & UART_ERR_INT_FLAG)) {
                /* Transaction error. Abort */
                uart_hal_clr_intsts_mask(&hal, intr_mask);
                uart_hal_disable_intr_mask(&hal, intr_mask);
                return -1;
            }

            /* Update the byte counters */
            bytes_rcvd += rx_len;
            remaining_bytes -= rx_len;
        } else {
            /* We have no data to read from the Rx FIFO. Check for transaction timeout */
            ret = lp_core_uart_check_timeout(hal, intr_mask, timeout, &to);
            if (ret == ESP_ERR_TIMEOUT) {
                break;
            }
        }
    }

    /* Disable the Rx interrupts */
    uart_hal_disable_intr_mask(&hal, intr_mask);

    /* Return the number of bytes received */
    return bytes_rcvd;
}
