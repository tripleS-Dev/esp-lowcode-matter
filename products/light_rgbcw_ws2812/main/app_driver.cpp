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

#include <light_driver.h>

#include "app_priv.h"

#include <math.h>

#define WS2812_CTRL_IO ((gpio_num_t)8)

static const char *TAG = "app_driver";

int app_driver_init()
{
    printf("%s: Initializing light driver\n", TAG);
    light_driver_config_t cfg = {
        .device_type = LIGHT_DEVICE_TYPE_WS2812,
        .channel_comb = LIGHT_CHANNEL_COMB_3CH_RGB,
        .io_conf = {
            .ws2812_io = {
                .ctrl_io = WS2812_CTRL_IO,
            },
        },
        .min_brightness = 0,
        .max_brightness = 100,
    };
    light_driver_init(&cfg);
    light_driver_set_power(true);
    light_driver_set_hue(100);
    light_driver_set_saturation(100);
    light_driver_set_brightness(100);
    return 0;
}

int app_driver_set_light_state(bool state)
{
    printf("%s: Setting light state: %s\n", TAG, state ? "ON" : "OFF");
    return light_driver_set_power(state);
}

int app_driver_set_light_brightness(uint8_t brightness)
{
    brightness = brightness * 100 / 255;
    printf("%s: Setting light brightness: %d\n", TAG, brightness);
    return light_driver_set_brightness(brightness);
}

int app_driver_set_light_hue(uint8_t hue)
{
    hue = hue * 360 / 255;
    printf("%s: Setting light hue: %d\n", TAG, hue);
    return light_driver_set_hue(hue);
}

int app_driver_set_light_saturation(uint8_t saturation)
{
    saturation = saturation * 100 / 255;
    printf("%s: Setting light saturation: %d\n", TAG, saturation);
    return light_driver_set_saturation(saturation);
}

int app_driver_set_light_temperature(uint16_t temperature)
{
    temperature = 1000000 / temperature;
    printf("%s: Setting light temperature: %d\n", TAG, temperature);
    return light_driver_set_temperature(temperature);
}

/* 도 → 0‑360 정수, 퍼센트 → 0‑100 정수로 바꿔 주는 작은 헬퍼                   */
static inline uint16_t hue_deg_to_u16(double h)
{
    /* fmod() 결과가 음수로 나올 수 있음 → 0‥360 로 감싸기                   */
    if (h < 0)            h += 360.0;
    else if (h >= 360.0)  h = fmod(h, 360.0);
    return (uint16_t)(h + 0.5);               /* 반올림 */
}

static inline uint8_t sat_frac_to_u8(double s)
{
    if (s < 0) s = 0;
    if (s > 1) s = 1;
    return (uint8_t)(s * 100.0 + 0.5);        /* 0‥1 → 0‥100, 반올림 */
}

void app_driver_set_light_xy(uint16_t x16, uint16_t y16)
{
    /* 1) 16‑bit → 정규화 */
    double x = x16 / 65535.0;
    double y = y16 / 65535.0;
    if (y <= 1e-6 || x + y > 1.0) return;     /* 방어 코드 */

    /* 2) CIE xyY (Y=1) → 선형 sRGB */
    double X = x / y;
    double Y = 1.0;
    double Z = (1.0 - x - y) / y;

    double r =  3.2406*X - 1.5372*Y - 0.4986*Z;
    double g = -0.9689*X + 1.8758*Y + 0.0415*Z;
    double b =  0.0557*X - 0.2040*Y + 1.0570*Z;

    /* 음수 제거 */
    if (r < 0) r = 0;
    if (g < 0) g = 0;
    if (b < 0) b = 0;

    /* sRGB 값이 1.0을 넘으면 전체를 동일 비율로 스케일해 클리핑 방지           */
    double max_rgb = fmax(r, fmax(g, b));
    if (max_rgb > 1.0) {
        r /= max_rgb;
        g /= max_rgb;
        b /= max_rgb;
    }

    /* 3) RGB → HSV */
    double max = fmax(r, fmax(g, b));
    double min = fmin(r, fmin(g, b));
    double delta = max - min;

    /* Hue 계산 (deg) */
    double H = 0.0;
    if (delta > 1e-6) {
        if (max == r)        H = 60.0 * fmod((g - b) / delta, 6.0);
        else if (max == g)   H = 60.0 * (((b - r) / delta) + 2.0);
        else                 H = 60.0 * (((r - g) / delta) + 4.0);
    }
    /* fmod 결과 보정 */
    if (H < 0.0) H += 360.0;

    /* Saturation (0‑1) */
    double S = (max <= 1e-6) ? 0.0 : (delta / max);

    /* 4) 드라이버 호출 */
    light_driver_set_hue(hue_deg_to_u16(H));   /* 0‑360° → uint16_t */
    light_driver_set_saturation(sat_frac_to_u8(S)); /* 0‑1 → 0‑100% */
}



int app_driver_event_handler(low_code_event_t *event)
{
    /* Get the events. Approriate indicators should be shown to the user based on the event. */
    printf("%s: Received event: %d\n", TAG, event->event_type);
    light_effect_config_t effect_config = {
        .type = LIGHT_EFFECT_INVALID,
        .mode = LIGHT_WORK_MODE_COLOR,
        .max_brightness = 100,
        .min_brightness = 10
    };

    /* Handle the events */
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