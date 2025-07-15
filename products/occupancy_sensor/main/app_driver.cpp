// Copyright 2025 Espressif Systems (Shanghai) PTE LTD
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

#include <stdio.h>

#include <system.h>
#include <button_driver.h>
#include <light_driver.h>
#include <occupancy_sensor_ld2420.h>

#include "app_priv.h"

static const char *TAG = "app_driver";

#define BUTTON_GPIO_NUM ((gpio_num_t)9)
#define INDICATOR_GPIO_NUM ((gpio_num_t)8)

/* Using HP UART PORT 1 */
#define LD2420_UART_PORT_NUM    UART_NUM_1
#define LD2420_RX_GPIO_NUM     (gpio_num_t)GPIO_NUM_2
#define LD2420_TX_GPIO_NUM     (gpio_num_t)GPIO_NUM_3

static occupancy_sensor_ld2420_handle_t handle;

static void app_driver_trigger_factory_reset_button_callback(void *arg, void *data)
{
    /* Update by sending event */
    low_code_event_t event = {
        .event_type = LOW_CODE_EVENT_FACTORY_RESET
    };

    low_code_event_to_system(&event);
    printf("%s: Factory reset triggered\n", TAG);
}

void app_driver_report_occupancy_sensor_state(bool occupancy_state)
{
    low_code_feature_data_t feature = {
        .details = {
            .endpoint_id = 1,
            .feature_id = LOW_CODE_FEATURE_ID_OCCUPANCY_SENSOR_VALUE
        },
        .value = {
            .type = LOW_CODE_VALUE_TYPE_UNSIGNED_INTEGER,
            .value_len = sizeof(uint8_t),
            .value = (uint8_t*)&occupancy_state
        },
    };

    low_code_feature_update_to_system(&feature);
}

/*
 * Read the occupancy state from the sensor.
 * Also report the updated value to the system
 *
 * Note: The function signature must match the required timer callback format,
 * so `timer_handle` and `user_data` are included but intentionally unused.
 */
void app_driver_read_and_report_feature(system_timer_handle_t timer_handle, void *user_data)
{
    occupancy_sensor_ld2420_normal_mode_data_t data;

    if (occupancy_sensor_ld2420_read_normal_data(handle, &data)) {
        printf("%s: LD2420 unable to fetch data\n", TAG);
        return ;
    }

    /* Reporting Occupancy State */
    app_driver_report_occupancy_sensor_state(data.occupied);
}

int app_driver_init()
{
    printf("%s: Initializing driver\n", TAG);

    /* Initialize button */
    button_config_t btn_cfg = {
        .gpio_num = BUTTON_GPIO_NUM,
        .pullup_en = 1,
        .active_level = 0,
    };
    button_handle_t btn_handle = button_driver_create(&btn_cfg);
    if (!btn_handle) {
        printf("%s: Failed to create the button", TAG);
        return -1;
    }

    /* Register callback to factory reset the device on button long press */
    button_driver_register_cb(btn_handle, BUTTON_LONG_PRESS_UP, app_driver_trigger_factory_reset_button_callback, NULL);

    /* Initialise the light indicator */
    light_driver_config_t light_cfg = {
        .device_type = LIGHT_DEVICE_TYPE_WS2812,
        .channel_comb = LIGHT_CHANNEL_COMB_3CH_RGB,
        .io_conf = {
            .ws2812_io = {
                .ctrl_io = INDICATOR_GPIO_NUM,
            },
        },
        .min_brightness = 0,
        .max_brightness = 100,
    };
    light_driver_init(&light_cfg);

    /* Configure the LD2420 Occupancy Sensor */
    occupancy_sensor_ld2420_cfg_t ld2420_cfg = {
        .uart_num = LD2420_UART_PORT_NUM,
        .tx_pin = LD2420_TX_GPIO_NUM,
        .rx_pin = LD2420_RX_GPIO_NUM,
    };
    handle = occupancy_sensor_ld2420_init(&ld2420_cfg);
    if (!handle) {
        printf("%s: Failed to initialise the LD2420 occupancy sensor\n", TAG);
        return -1;
    }

    /* Reading the firmware version to ensure the LD2420 sensor is functioning correctly */
    char firmware_version[10];
    int ret = occupancy_sensor_ld2420_get_firmware_version(handle, firmware_version, sizeof(firmware_version));
    if (!ret) {
        printf("%s: LD2420 firmware version: %s\n", TAG, firmware_version);
    } else {
        printf("%s: LD2420 failed to get the firmware version\n", TAG);
        return -1;
    }

    /* Configure LD2420 to enter in normal mode */
    if (occupancy_sensor_ld2420_enter_normal_mode(handle)) {
        printf("%s: LD2420 failed to enter into normal mode\n", TAG);
        return -1;
    }

    /*
     * Create a timer that will call `app_driver_read_and_report_feature`
     * periodically every 2 sec.
     */
    system_timer_handle_t timer = system_timer_create(app_driver_read_and_report_feature, NULL, 2000, true);
    if (!timer) {
        printf("%s: Failed to create timer\n", TAG);
        return -1;
    }

    system_timer_start(timer);

    return 0;
}

int app_driver_feature_update()
{
    printf("%s: Feature update\n", TAG);

    /* Nothing to do here. The device reports the feature data by itself. */
    return 0;
}

int app_driver_event_handler(low_code_event_t *event)
{
    /* Get the events. Approriate indicators should be shown to the user based on the event. */
    printf("%s: Received event: %d\n", TAG, event->event_type);
    light_effect_config_t effect_config = {
        .type = LIGHT_EFFECT_INVALID,
        .mode = LIGHT_WORK_MODE_COLOR, /* Since it is a single channel LED */
        .max_brightness = 100,
        .min_brightness = 10
    };

    /* Handle the events from low_code_event_type_t */
    switch (event->event_type) {
        case LOW_CODE_EVENT_SETUP_MODE_START:
            printf("%s: Setup mode started\n", TAG);
            /* Start Indication */
            effect_config.type = LIGHT_EFFECT_BLINK;
            light_driver_effect_start(&effect_config, 2000, 120000);
            break;
        case LOW_CODE_EVENT_SETUP_MODE_END:
            printf("%s: Setup mode ended\n", TAG);
            /* Stop Indication */
            light_driver_effect_stop();
            break;
        case LOW_CODE_EVENT_SETUP_DEVICE_CONNECTED:
            printf("%s: Device connected during setup\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_STARTED:
            printf("%s: Setup process started\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_SUCCESSFUL:
            printf("%s: Setup process successful\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_FAILED:
            printf("%s: Setup process failed\n", TAG);
            break;
        case LOW_CODE_EVENT_NETWORK_CONNECTED:
            printf("%s: Network connected\n", TAG);
            break;
        case LOW_CODE_EVENT_NETWORK_DISCONNECTED:
            printf("%s: Network disconnected\n", TAG);
            break;
        case LOW_CODE_EVENT_OTA_STARTED:
            printf("%s: OTA update started\n", TAG);
            break;
        case LOW_CODE_EVENT_OTA_STOPPED:
            printf("%s: OTA update stopped\n", TAG);
            break;
        case LOW_CODE_EVENT_READY:
            printf("%s: Device is ready\n", TAG);
            break;
        case LOW_CODE_EVENT_IDENTIFICATION_START:
            printf("%s: Identification started\n", TAG);
            break;
        case LOW_CODE_EVENT_IDENTIFICATION_STOP:
            printf("%s: Identification stopped\n", TAG);
            break;
        case LOW_CODE_EVENT_TEST_MODE_LOW_CODE:
            printf("%s: Low code test mode is triggered for subtype: %d\n", TAG, (int)*((int*)(event->event_data)));
            break;
        case LOW_CODE_EVENT_TEST_MODE_COMMON:
            printf("%s: common test mode triggered\n", TAG);
            break;
        case LOW_CODE_EVENT_TEST_MODE_BLE:
            printf("%s: ble test mode triggered\n", TAG);
            break;
        case LOW_CODE_EVENT_TEST_MODE_SNIFFER:
            printf("%s: sniffer test mode triggered\n", TAG);
            break;
        default:
            printf("%s: Unhandled event type: %d\n", TAG, event->event_type);
            break;
    }

    return 0;
}
