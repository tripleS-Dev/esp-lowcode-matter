// Copyright 2024 Espressif Systems (Shanghai) PTE LTD
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @file rmt.h
 * @brief RMT (Remote Control) peripheral driver for LP core
 *
 * This component provides functionality to control the RMT peripheral on the Low Power (LP) core.
 * It is primarily used for generating precise timing signals, such as those needed for WS2812 LED control.
 */

#pragma once

#include <stdbool.h>
#include <stdint.h>
#include "esp_mac.h"
#include "hal/rmt_ll.h"
#include "hal/rmt_hal.h"
#include "hal/gpio_hal.h"
#include "hal/gpio_ll.h"
#include "hal/clk_tree_ll.h"
#include "hal/clk_tree_hal.h"
#include "soc/gpio_num.h"
#include "soc/gpio_periph.h"
#include "soc/rmt_periph.h"
#include "soc/rtc.h"
#include "sdkconfig.h"

#define RMT_DEFAULT_GROUP            (0)
#define RMT_DEFAULT_TX_CHANNEL       (0)
#define RMT_DEFAULT_CLK_RESOLUTION   XTAL_CLK_FREQ
// #define RMT_DEFAULT_CLK_RESOLUTION   RTC_FAST_CLK_FREQ_APPROX

#define RMT_DEFAULT_CLK_SRC          RMT_CLK_SRC_XTAL
// #define RMT_DEFAULT_CLK_SRC          RMT_CLK_SRC_RC_FAST

// For ESP32C6 Only
#define CONFIG_BLINK_GPIO               (8)
#define BLINK_GPIO                      CONFIG_BLINK_GPIO

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Hard-coded RMTMEM structure
 */
typedef struct {
    struct {
        rmt_symbol_word_t symbols[48];
    } channels[4];
} rmt_block_mem_t;

extern rmt_block_mem_t RMTMEM;

/**
 * @brief RMT channel configuration structure
 */
struct rmt_channel_t {
    size_t clkResolutionHz;         /**< Clock resolution in Hz */
    unsigned int realClkResolutionHz; /**< Actual clock resolution after divider */
    size_t groupClkResolutionHz;    /**< Group clock resolution in Hz */
    size_t channalId;               /**< Channel ID */
    size_t gpioPin;                 /**< GPIO pin number */
    rmt_symbol_word_t bit0;         /**< RMT symbol for bit 0 */
    rmt_symbol_word_t bit1;         /**< RMT symbol for bit 1 */
    size_t readlDiv;                /**< Clock divider */
    bool msbFirst;                  /**< True if MSB is transmitted first */
};

typedef struct rmt_channel_t     rmt_channel_t;

/**
 * @brief Send bytes using RMT
 *
 * @param dataBuffer Pointer to data buffer to send
 * @param numBits Number of bits to send
 * @param channel Pointer to RMT channel configuration
 * @return bool true if successful, false otherwise
 */
bool rmt_send_bytes(void* dataBuffer, size_t numBits, rmt_channel_t* channel);

/**
 * @brief Configure RMT transmit channel
 *
 * @param channel Pointer to RMT channel configuration
 * @return bool true if successful, false otherwise
 */
bool rmt_config_tx_channel(rmt_channel_t* channel);

/**
 * @brief Create default transmit channel with standard configuration
 *
 * @param defaultChannel Pointer to store default channel configuration
 * @return bool true if successful, false otherwise
 */
bool rmt_create_default_tx_channel(rmt_channel_t* defaultChannel);

/**
 * @brief Initialize RMT device
 *
 * @return bool true if successful, false otherwise
 */
bool rmt_init_device(void);

/**
 * @brief Deinitialize RMT device
 *
 * @return bool true if successful, false otherwise
 */
bool rmt_deinit_device(void);

#ifdef __cplusplus
}
#endif
