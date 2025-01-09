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
 * @file lp_sw_timer.h
 * @brief Software timer implementation for LP core
 *
 * This component provides a software timer implementation for the Low Power (LP) core,
 * supporting both periodic and one-shot timer functionality with millisecond resolution.
 */

#pragma once

#include "stdbool.h"

#ifdef __cplusplus
extern "C" {
#endif

/** @brief Handle type for the software timer */
typedef void *lp_sw_timer_handle_t;

/** @brief Callback function type for timer events */
typedef void (* lp_sw_timer_cb_t)(lp_sw_timer_handle_t timer_handle, void *user_data);

/**
 * @brief Configuration structure for software timer
 */
typedef struct {
    bool periodic;              /** Set true for auto-reload timer, false for one-shot */
    int timeout_ms;             /** Timeout period in milliseconds */
    lp_sw_timer_cb_t handler;   /** Callback function to be called when timer expires */
    void *arg;                  /** User data to pass to callback function */
} lp_sw_timer_config_t;

/**
 * @brief Create a new software timer
 *
 * @param config Pointer to timer configuration structure
 * @return lp_sw_timer_handle_t Handle to the created timer, NULL if creation failed
 */
lp_sw_timer_handle_t lp_sw_timer_create(lp_sw_timer_config_t *config);

/**
 * @brief Delete a software timer
 *
 * @param timer_handle Handle of the timer to delete
 * @return int 0 on success, negative value on error
 */
int lp_sw_timer_delete(lp_sw_timer_handle_t timer_handle);

/**
 * @brief Start a software timer
 *
 * @param timer_handle Handle of the timer to start
 * @return int 0 on success, negative value on error
 */
int lp_sw_timer_start(lp_sw_timer_handle_t timer_handle);

/**
 * @brief Stop a software timer
 *
 * @param timer_handle Handle of the timer to stop
 * @return int 0 on success, negative value on error
 */
int lp_sw_timer_stop(lp_sw_timer_handle_t timer_handle);

/**
 * @brief Run the timer system
 *
 * This function should be called periodically to process timer events.
 * It checks for expired timers and calls their callbacks.
 */
void lp_sw_timer_run(void);

#ifdef __cplusplus
}
#endif
