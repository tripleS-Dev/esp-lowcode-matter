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

#include <system.h>
#include <low_code.h>

#include "app_priv.h"

static const char *TAG = "app_main";

static void setup()
{
    /* Register callbacks */
    low_code_register_callbacks(feature_update_from_system, event_from_system);

    /* Initialize driver */
    app_driver_init();
}

static void loop()
{
    /* The corresponding callbacks are called if data is received from system */
    low_code_get_feature_update_from_system();
    low_code_get_event_from_system();
}

static uint16_t s_xy_cache_x = 0xFFFF;
static uint16_t s_xy_cache_y = 0xFFFF;

int feature_update_from_system(low_code_feature_data_t *data)
{
    /* Get the device feature updates */
    uint16_t endpoint_id = data->details.endpoint_id;
    uint32_t feature_id = data->details.feature_id;

    if (endpoint_id == 1) {
        if (feature_id == LOW_CODE_FEATURE_ID_POWER) {  // Power
            bool power_value = *(bool *)data->value.value;
            printf("%s: Feature update: power: %d\n", TAG, power_value);
            app_driver_set_light_state(power_value);
        } else if (feature_id == LOW_CODE_FEATURE_ID_BRIGHTNESS) {  // Brightness
            uint8_t brightness = *(uint8_t *)data->value.value;
            printf("%s: Feature update: brightness: %d\n", TAG, brightness);
            app_driver_set_light_brightness(brightness);
        } else if (feature_id == LOW_CODE_FEATURE_ID_COLOR_TEMPERATURE) {  // Color temperature
            uint16_t color_temp = *(uint16_t *)data->value.value;
            printf("%s: Feature update: color temperature: %d\n", TAG, color_temp);
            app_driver_set_light_temperature(color_temp);
        } else if (feature_id == LOW_CODE_FEATURE_ID_HUE) {  // Hue
            uint8_t hue = *(uint8_t *)data->value.value;
            printf("%s: Feature update: hue: %d\n", TAG, hue);
            app_driver_set_light_hue(hue);
        } else if (feature_id == LOW_CODE_FEATURE_ID_SATURATION) {  // Saturation
            uint8_t saturation = *(uint8_t *)data->value.value;
            printf("%s: Feature update: saturation: %d\n", TAG, saturation);
            app_driver_set_light_saturation(saturation);
        } else if (feature_id == LOW_CODE_FEATURE_ID_COLOR_X) {
            s_xy_cache_x = *(uint16_t *)data->value.value;

        } else if (feature_id == LOW_CODE_FEATURE_ID_COLOR_Y) {
            s_xy_cache_y = *(uint16_t *)data->value.value;
        } 

        /* 두 좌표가 모두 준비되면 변환‑출력 */
        if (s_xy_cache_x != 0xFFFF && s_xy_cache_y != 0xFFFF) {
            app_driver_set_light_xy(s_xy_cache_x, s_xy_cache_y);
            s_xy_cache_x = s_xy_cache_y = 0xFFFF;   // (선택) 다음 세트 준비
        }
    }

    return 0;
}

int event_from_system(low_code_event_t *event)
{
    /* Handle the events from low_code_event_type_t */
    return app_driver_event_handler(event);
}

extern "C" int main()
{
    printf("%s: Starting low code\n", TAG);

    /* Pre-Initializations: This should be called first and should always be present */
    system_setup();
    setup();

    /* Loop */
    while (1) {
        system_loop();
        loop();
    }
    return 0;
}
