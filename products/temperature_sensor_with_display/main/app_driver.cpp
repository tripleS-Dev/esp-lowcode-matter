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

#include <stdio.h>
#include <string.h>

#include <low_code.h>
#include <system.h>
#include <i2c_master.h>
#include <temperature_sensor_sht30.h>
#include <display_ssd1306.h>
#include <button_driver.h>

#include "app_priv.h"

#define BUTTON_GPIO_NUM (gpio_num_t)9

#define I2C_PORT   I2C_NUM_0
#define I2C_SCL_IO (gpio_num_t)1
#define I2C_SDA_IO (gpio_num_t)2

static const char *TAG = "app_driver";

static display_ssd1306_handle_t ssd1306_handle;

static bool setup_started = false;

static void app_driver_trigger_factory_reset_button_callback(void *arg, void *data)
{
    /* Update by sending event */
    low_code_event_t event = {
        .event_type = LOW_CODE_EVENT_FACTORY_RESET
    };

    low_code_event_to_system(&event);
    printf("%s: Factory reset triggered\n", TAG);
}

static void app_driver_report_temperature(float temp)
{
    int16_t temperature = temp * 100;
    /* Update the feature */
    low_code_feature_data_t update_data = {
        .details = {
            .endpoint_id = 1,
            .feature_id = LOW_CODE_FEATURE_ID_TEMPERATURE_SENSOR_VALUE
        },
        .value = {
            .type = LOW_CODE_VALUE_TYPE_INTEGER,
            .value_len = sizeof(int16_t),
            .value = (uint8_t*)&temperature,
        },
    };

    low_code_feature_update_to_system(&update_data);
}

/* Note: We're using the SSD1315 display, but the SSD1306 driver is sufficiently general to support it as well. */
static void app_driver_update_display(char *msg)
{
    char *newline_ptr = strchr(msg, '\n');
    char *line_2 = NULL;

    display_ssd1306_clear_screen(ssd1306_handle, 0x00);

    if (newline_ptr != NULL) {
        size_t len = newline_ptr - msg;

        // Create a local buffer of exact length + 1 for null-terminator
        char line_1[len + 1];
        strncpy(line_1, msg, len);
        line_1[len] = '\0';  // Null-terminate

        line_2 = newline_ptr + 1;

        display_ssd1306_draw_string(ssd1306_handle, 40, 35, (const uint8_t *)line_1, 14, 1);

        if (*line_2 != '\0') {
            display_ssd1306_draw_string(ssd1306_handle, 40, 50, (const uint8_t *)line_2, 14, 1);
        }

    } else {
        // No newline: just draw the whole message
        display_ssd1306_draw_string(ssd1306_handle, 40, 35, (const uint8_t *)msg, 14, 1);
    }

    display_ssd1306_refresh_gram(ssd1306_handle);
}

/*
 * Read the temperature from the sensor and show the readings on the display.
 * Also report the updated value to the system
 *
 * Note: The function signature must match the required timer callback format,
 * so `timer_handle` and `user_data` are included but intentionally unused.
 */
void app_driver_read_and_report_feature(system_timer_handle_t timer_handle, void *user_data)
{
    float temperature = 0.0;
    char temperature_str[10] = {0};

    /* Reading temperature */
    temperature_sensor_sht30_get_celsius(I2C_PORT, &temperature);

    /* Update the display */
    sprintf(temperature_str, "%d.%02d C", (int)temperature, ((int)(temperature * 100) % 100));
    app_driver_update_display((char*)temperature_str);
    system_delay_ms(100);

    /* Report the temperature */
    app_driver_report_temperature(temperature);

    /* When in setup mode alternate between showing temperature and setup status */
    if (setup_started) {
        system_delay_ms(1000);
        app_driver_update_display((char*)"Setup\nMode");
    }
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
        printf("%s: Failed to create the button\n", TAG);
        return -1;
    }

    /* Register callback to factory reset the device on button long press */
    button_driver_register_cb(btn_handle, BUTTON_LONG_PRESS_UP, app_driver_trigger_factory_reset_button_callback, NULL);

    /* Initialize I2C */
    int ret = i2c_master_init(I2C_PORT, I2C_SCL_IO, I2C_SDA_IO);
    if (ret) {
        printf("%s: Failed to initialise master i2c\n", TAG);
        return -1;
    }

    /* Initialize display driver */
    ssd1306_handle = display_ssd1306_i2c_create(SSD1306_I2C_ADDRESS, I2C_PORT);
    if (!ssd1306_handle) {
        printf("%s: Failed to create the ssd1306 display handle\n", TAG);
        return -1;
    }
    app_driver_update_display((char*)"");

    /* Initialize temperature sensor */
    ret = temperature_sensor_sht30_init(I2C_PORT);
    if (ret) {
        printf("%s: Failed to initialise sht30 temperature sensor\n", TAG);
        return -1;
    }

    /*
     * Create a timer that will call `app_driver_read_and_report_feature`
     * periodically every 10 sec.
     */
    system_timer_handle_t timer = system_timer_create(app_driver_read_and_report_feature, NULL, 10000, true);
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
    printf("%s: Received event: %d\n", TAG, event->event_type);

    switch (event->event_type) {
        case LOW_CODE_EVENT_SETUP_MODE_START:
            printf("%s: Setup mode started\n", TAG);
            /*
             * In the `app_driver_read_and_report_feature` function,
             * "Setup Mode" is displayed, alternating with the temperature reading
             * based on the value of `setup_started`
             */
            setup_started = true;
            break;
        case LOW_CODE_EVENT_SETUP_MODE_END:
            printf("%s: Setup mode ended\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_DEVICE_CONNECTED:
            printf("%s: Device connected during setup\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_STARTED:
            printf("%s: Setup process started\n", TAG);
            break;
        case LOW_CODE_EVENT_SETUP_SUCCESSFUL: 
            printf("%s: Setup process successful\n", TAG);
            setup_started = false;
            app_driver_update_display((char*)"Setup\nSuccess");
            system_delay(2);
            break;
        case LOW_CODE_EVENT_SETUP_FAILED:
            printf("%s: Setup process failed\n", TAG);
            setup_started = false;
            app_driver_update_display((char*)"Setup\nFailed");
            system_delay(2);
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
