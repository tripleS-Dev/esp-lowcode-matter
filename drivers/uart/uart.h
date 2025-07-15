/*
 * SPDX-FileCopyrightText: 2023-2025 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdbool.h>

#include <soc/gpio_num.h>
#include <hal/uart_types.h>

#include <esp_err.h>

/**
 * @brief UART IO pins configuration
 */
typedef struct {
    gpio_num_t tx_io_num;               /*!< GPIO pin for UART Tx signal */
    gpio_num_t rx_io_num;               /*!< GPIO pin for UART Rx signal */
    gpio_num_t rts_io_num;              /*!< GPIO pin for UART RTS signal */
    gpio_num_t cts_io_num;              /*!< GPIO pin for UART CTS signal */
} uart_pin_cfg_t;

/**
 * @brief UART protocol configuration
 */
typedef struct {
    int baud_rate;                      /*!< UART baud rate */
    uart_word_length_t data_bits;       /*!< UART byte size */
    uart_parity_t parity;               /*!< UART parity mode */
    uart_stop_bits_t stop_bits;         /*!< UART stop bits */
    uart_hw_flowcontrol_t flow_ctrl;    /*!< UART HW flow control mode (cts/rts) */
    uint8_t rx_flow_ctrl_thresh;        /*!< UART HW RTS threshold */
} uart_proto_cfg_t;

/**
 * @brief UART configuration parameters
 */
typedef struct {
    uart_pin_cfg_t uart_pin_cfg;        /*!< UART pin configuration */
    uart_proto_cfg_t uart_proto_cfg;    /*!< UART protocol configuration */
} uart_cfg_t;

/**
 * @brief initialise the UART peripheral
 *
 * @param uart_port     uart port to use. Supports HP UART ports like UART_NUM_1 and LP UART ports like LP_UART_NUM_0.
 * @param cfg           lp_core_uart_cfg_t configuration for uart
 *
 * @return esp_err_t    ESP_OK when successful
 *
 */
esp_err_t uart_init(uart_port_t uart_num, uart_cfg_t cfg);

/**
 * @brief Read data from the UART port
 *
 * This function will read data from the Rx FIFO. If a timeout value is configured, then this function will timeout once the number of CPU cycles expire.
 *
 * @param uart_num      UART port number
 * @param buf           data buffer address
 * @param size          data length to send
 * @param timeout       Operation timeout in CPU cycles. Set to -1 to wait forever.
 *
 * @return              - (-1) Error
 *                      - OTHERS (>=0) The number of bytes read from the Rx FIFO
 */
int uart_read_bytes(uart_port_t uart_num, void *buf, size_t size, int32_t timeout);

/**
 * @brief Write data to the UART port
 *
 * This function will write data to the Tx FIFO. If a timeout value is configured, this function will timeout once the number of CPU cycles expire.
 *
 * @param uart_num      UART port number
 * @param src           data buffer address
 * @param size          data length to send
 * @param timeout       Operation timeout in CPU cycles. Set to -1 to wait forever.
 *
 * @return esp_err_t    ESP_OK when successful
 */
esp_err_t uart_write_bytes(uart_port_t uart_num, const void *src, size_t size, int32_t timeout);

#ifdef __cplusplus
}
#endif
