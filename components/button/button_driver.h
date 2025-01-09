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
 * @file button_driver.h
 * @brief Button driver component for handling button inputs on both HP and LP GPIO
 *
 * This component provides functionality to handle button inputs using either High Power (HP)
 * or Low Power (LP) GPIO configurations. It supports button press detection and callback mechanisms.
 */

#pragma once

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/** @brief Button callback function type */
typedef void (* button_cb_t)(void *button_handle, void *usr_data);

/** @brief Button handle type */
typedef void *button_handle_t;

/** @brief Button event type */
typedef enum {
    BUTTON_PRESS_DOWN = 0,     /**< Button press down event */
    BUTTON_PRESS_UP,           /**< Button press up event */
    BUTTON_SINGLE_CLICK,       /**< Button single click event */
    BUTTON_LONG_PRESS_START,   /**< Button long press start event */
    BUTTON_LONG_PRESS_UP,      /**< Button long press up event */
    BUTTON_EVENT_MAX,          /**< Maximum number of button events */
} button_event_t;

/** @brief Button configuration structure */
typedef struct {
    uint16_t long_press_time;      /**< Trigger time(ms) for long press, if 0 default to BUTTON_LONG_PRESS_TIME_MS */
    uint16_t short_press_time;     /**< Trigger time(ms) for click, if 0 default to BUTTON_SHORT_PRESS_TIME_MS */
    int gpio_num;                  /**< GPIO number */
    uint8_t pullup_en:1;           /**< Enable GPIO pullup */
    uint8_t pulldown_en:1;         /**< Enable GPIO pulldown */
    uint8_t active_level: 1;       /**< GPIO level when press down */
} button_config_t;

/**
 * @brief Create a button
 *
 * @param config pointer of button configuration, must corresponding the button type
 *
 * @return A handle to the created button, or NULL in case of error.
 */
button_handle_t button_driver_create(const button_config_t *config);

/**
 * @brief Delete a button
 *
 * @param btn_handle A button handle to delete
 *
 * @return 0 on success, negative value on error
 */
int button_driver_delete(button_handle_t btn_handle);

/**
 * @brief Register the button event callback function.
 *
 * @param btn_handle A button handle to register
 * @param event Button event
 * @param cb Callback function.
 * @param usr_data user data
 *
 * @return 0 on success, negative value on error
 */
int button_driver_register_cb(button_handle_t btn_handle, button_event_t event, button_cb_t cb, void *usr_data);

/**
 * @brief Unregister all the callbacks associated with the event.
 *
 * @param btn_handle A button handle to unregister
 * @param event Button event
 *
 * @return 0 on success, negative value on error
 */
int button_driver_unregister_cb(button_handle_t btn_handle, button_event_t event);

#ifdef __cplusplus
}
#endif
