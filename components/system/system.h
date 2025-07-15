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
 * @file system.h
 * @brief System utilities component for LP core
 *
 * This component provides core system functionality for the Low Power (LP) core,
 * including GPIO operations, timing functions, and basic system control operations.
 */

#pragma once

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief System software timer handle.
 */
typedef void *system_timer_handle_t;

/**
 * @brief Callback function type for timer events
 */
typedef void (* system_timer_cb_t)(system_timer_handle_t timer_handle, void *user_data);

/**
 * @brief Pin mode configuration options
 */
typedef enum {
    INPUT,    /**< Configure pin as input */
    OUTPUT    /**< Configure pin as output */
} pin_mode_t;

/**
 * @brief Pin level states
 */
typedef enum {
    LOW = 0,  /**< Pin level low (0V) */
    HIGH,     /**< Pin level high (3.3V/5V) */
} pin_level_t;

/**
 * @brief Main system loop function
 *
 * This function should be called repeatedly in the main loop.
 * It handles system tasks and updates.
 */
void system_loop();

/**
 * @brief System initialization function
 *
 * This function should be called once during system startup.
 * It initializes system components and sets up required configurations.
 */
void system_setup();

/**
 * @brief Update system timers
 *
 * This function updates all system timers and should be called periodically.
 * @note This function is called by system_loop()
 */
void system_timer_update();

/**
 * @brief Put the system to sleep for specified duration
 *
 * This is same as system_delay()
 *
 * @param seconds Number of seconds to sleep
 */
void system_sleep(uint32_t seconds);

/**
 * @brief Delay system execution for specified duration
 *
 * @param seconds Number of seconds to delay
 */
void system_delay(uint32_t seconds);

/**
 * @brief Millisecond delay function
 *
 * @param ms Number of milliseconds to delay
 */
void system_delay_ms(uint32_t ms);

/**
 * @brief Microsecond delay function
 *
 * @param us Number of microseconds to delay
 */
void system_delay_us(uint32_t us);

/**
 * @brief Get current system time in milliseconds
 *
 * This is the time since the system was booted.
 * @return uint32_t Current system time in milliseconds
 */
uint32_t system_get_time();

/**
 * @brief Create system timer
 *
 * @param callback Callback function to execute when timer expires
 * @param arg   Argument to pass to callback
 * @param timeout_ms timer period, in microseconds
 * @param periodic Whether timer needs to be periodic or one-shot
 *
 * @return sytem_timer_handle if successful else NULL
 */
system_timer_handle_t system_timer_create(system_timer_cb_t callback, void *arg, int timeout_ms, bool periodic);

/**
 * @brief Start system timer
 *
 * @param handle system_timer_handle_t created using system_timer_create
 *
 * @return
 *      - 0 on success
 *      - -1 on failure
 */
int system_timer_start(system_timer_handle_t handle);

/**
 * @brief Stop system timer
 *
 * @param handle system_timer_handle_t created using system_timer_create
 *
 * @return
 *      - 0 on success
 *      - -1 on failure
 */
int system_timer_stop(system_timer_handle_t handle);

/**
 * @brief Delete system timer
 *
 * @param handle system_timer_handle_t created using system_timer_create
 *
 * @return
 *      - 0 on success
 *      - -1 on failure
 */
int system_timer_delete(system_timer_handle_t handle);

/**
 * @brief Enable software interrupt
 *
 * Enables the software interrupt mechanism for the system.
 * This is needed for components like button driver to work.
 */
void system_enable_software_interrupt();

/**
 * @brief Configure GPIO pin mode
 *
 * @param gpio_num GPIO pin number
 * @param mode Pin mode (INPUT or OUTPUT)
 */
void system_set_pin_mode(int gpio_num, pin_mode_t mode);

/**
 * @brief Set digital output level
 *
 * @param gpio_num GPIO pin number
 * @param level Output level (HIGH or LOW)
 */
void system_digital_write(int gpio_num, pin_level_t level);

/**
 * @brief Read digital input level
 *
 * @param gpio_num GPIO pin number
 * @return int 1 for HIGH, 0 for LOW
 */
int system_digital_read(int gpio_num);

#ifdef __cplusplus
}
#endif
