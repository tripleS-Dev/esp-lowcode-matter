#include "stdio.h"
#include "stdint.h"
#include "stdlib.h"
#include "stdbool.h"
#include "lp_sw_timer.h"
#include "led_driver.h"
#include "light_driver.h"
#include "color_format.h"

#include "soc/gpio_num.h"
#include "ulp_lp_core_print.h"

typedef struct {
    uint8_t red;
    uint8_t green;
    uint8_t blue;
    uint8_t cold;
    uint8_t warm;
} light_channel_t;

typedef struct {
    light_effect_type_t type; /**< type of light effect */
    light_work_mode_t mode; /**< working mode of this effect */
    RGB_color_t RGB; /**< color for the effect */
    uint32_t cct; /**< color temperature of the effect */
    uint8_t max_brightness; /**< max brightness */
    uint8_t min_brightness; /**< min brightness */
    int speed;
    int total_ms;
    int rounds; /* used by effect timer handler */
    lp_sw_timer_handle_t timer; /* timer */
} light_effect_t;

typedef struct {
    light_device_type_t dev_type;
    light_dev_if_t dev;
    light_work_mode_t work_mode;
    light_channel_comb_t channel_comb;
    light_channel_t channel;
    uint8_t min_brightness;
    uint8_t max_brightness;
    uint8_t cur_brightness;
    uint8_t cur_level;
    HS_color_t cur_hs; /* current hue & saturation */
    uint32_t cur_cct; /* current temperature */
    light_effect_t cur_effect; /* current effect */
} light_driver_t;

static light_driver_t g_light;

static void light_driver_device_led_init(void)
{
    g_light.dev.init = led_driver_init;
    g_light.dev.deinit = led_driver_deinit;
    g_light.dev.set_channel = led_driver_set_channel;
    g_light.dev.regist_channel = led_driver_regist_channel;
    g_light.dev.hw_fade_start = led_driver_channel_fade_start;
    g_light.dev.hw_fade_end = led_driver_channel_fade_end;
}

int light_driver_init(light_driver_config_t *config)
{
    if (config->max_brightness > 100 || config->min_brightness < 0 || config->min_brightness > config->max_brightness) {
        printf("Invalid brightness: max=%d, min=%d\r\n", config->max_brightness, config->min_brightness);
        return -1;
    }

    if (config->channel_comb <= LIGHT_CHANNEL_COMB_INVALID || config->channel_comb >= LIGHT_CHANNEL_COMB_MAX) {
        printf("Invalid light channel combination: %d\r\n", config->channel_comb);
        return -1;
    }

    g_light.channel_comb = config->channel_comb;

   /* guess from CH settings */
    switch (config->channel_comb) {
    case LIGHT_CHANNEL_COMB_1CH_C:
    case LIGHT_CHANNEL_COMB_1CH_W:
    case LIGHT_CHANNEL_COMB_2CH_CW:
        g_light.work_mode = LIGHT_WORK_MODE_WHITE;
        break;
    case LIGHT_CHANNEL_COMB_3CH_RGB:
    case LIGHT_CHANNEL_COMB_5CH_RGBCW:
        g_light.work_mode = LIGHT_WORK_MODE_COLOR;
        break;
    default:
        break;
    }

    switch (config->device_type) {
    case LIGHT_DEVICE_TYPE_LED:
        printf("Light: LED\r\n");
        light_driver_device_led_init();

        if (g_light.dev.init() != 0) {
            printf("Failed to init device\r\n");
            g_light.dev.deinit();
        }

        switch (config->channel_comb) {
        case LIGHT_CHANNEL_COMB_1CH_C:
            g_light.channel.cold = LED_CHANNEL_COLD;
            g_light.dev.regist_channel(LED_CHANNEL_COLD, config->io_conf.led_io.cold);
            break;
        case LIGHT_CHANNEL_COMB_1CH_W:
            g_light.channel.warm = LED_CHANNEL_WARM;
            g_light.dev.regist_channel(LED_CHANNEL_WARM, config->io_conf.led_io.warm);
            break;
        case LIGHT_CHANNEL_COMB_2CH_CW:
            g_light.channel.cold = LED_CHANNEL_COLD;
            g_light.channel.warm = LED_CHANNEL_WARM;
            g_light.dev.regist_channel(LED_CHANNEL_COLD, config->io_conf.led_io.cold);
            g_light.dev.regist_channel(LED_CHANNEL_WARM, config->io_conf.led_io.warm);
            break;
        case LIGHT_CHANNEL_COMB_3CH_RGB:
            g_light.channel.red = LED_CHANNEL_RED;
            g_light.channel.green = LED_CHANNEL_GREEN;
            g_light.channel.blue = LED_CHANNEL_BLUE;
            g_light.dev.regist_channel(LED_CHANNEL_RED, config->io_conf.led_io.red);
            g_light.dev.regist_channel(LED_CHANNEL_GREEN, config->io_conf.led_io.green);
            g_light.dev.regist_channel(LED_CHANNEL_BLUE, config->io_conf.led_io.blue);
            break;
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            g_light.channel.red = LED_CHANNEL_RED;
            g_light.channel.green = LED_CHANNEL_GREEN;
            g_light.channel.blue = LED_CHANNEL_BLUE;
            g_light.channel.cold = LED_CHANNEL_COLD;
            g_light.channel.warm = LED_CHANNEL_WARM;
            g_light.dev.regist_channel(LED_CHANNEL_RED, config->io_conf.led_io.red);
            g_light.dev.regist_channel(LED_CHANNEL_GREEN, config->io_conf.led_io.green);
            g_light.dev.regist_channel(LED_CHANNEL_BLUE, config->io_conf.led_io.blue);
            g_light.dev.regist_channel(LED_CHANNEL_COLD, config->io_conf.led_io.cold);
            g_light.dev.regist_channel(LED_CHANNEL_WARM, config->io_conf.led_io.warm);
            break;
        default:
            printf("Unsupported channel setting\r\n");
            break;
        }
        break;
    default:
        printf("Invalid device\r\n");
        break;
    }

    return 0;
}

void light_driver_deinit(void)
{
    g_light.dev.deinit();
}

/**
 * @brief 
 * when switching from color mode to white mode number of LED beads changes from 3 to 2, the total intensity is lower
 * followings are very simple placeholder functions to scale down the channel output to avoid intensity jitter when
 * work mode switch from COLOR to WHITE
 * 
 * @param: scale [0, 100] light intensity
*/
static void process_color_limit(RGB_color_t *RGB_dst, RGB_color_t *RGB_src, uint8_t scale)
{
    /* NOTE: RGB range: [0, 255] */
    RGB_dst->red = RGB_src->red * scale / 255 / 3;
    RGB_dst->blue = RGB_src->blue * scale / 255 /3;
    RGB_dst->green = RGB_src->green * scale / 255 / 3;
}

static void process_cct_limit(CW_white_t *CW_dst, CW_white_t *CW_src, uint8_t scale)
{
    /* NOTE: CW range: [0, 100] */
    CW_dst->cold = CW_src->cold * scale / 100 / 2;
    CW_dst->warm = CW_src->warm * scale / 100 / 2;
}

/**
 * light_driver_update() is the single place to take effect of previous changes to g_light.cur_xxx 
 * light_driver_set_xxx() function simply change g_light.cur_xxx, but light_driver_update() update the underlying device
 * g_light.cur_xxx are un-normalized values, and light_driver_update() should process channel limits first and then write to device
*/
static int light_driver_update(void)
{
    /* check current color mode */
    /* if in color mode, set rgb channel only; if in white mode, set cw channel only */
    switch (g_light.work_mode) {
    case LIGHT_WORK_MODE_COLOR:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_3CH_RGB:
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            RGB_color_t RGB = {0};
            if (g_light.cur_level) {
                // NOTE: hsv_to_rgb has scale down the RGB based on cur_brightness, process_color_limit should not do again
                hsv_to_rgb(g_light.cur_hs, g_light.cur_brightness, &RGB);
                printf("cur_hue: %d, cur_sat: %d, cur_bright: %d, r:%d, g:%d, b:%d\r\n", g_light.cur_hs.hue, g_light.cur_hs.saturation, g_light.cur_brightness, RGB.red, RGB.green, RGB.blue);
                process_color_limit(&RGB, &RGB, 100);
            }
            /* write to device */
            g_light.dev.set_channel(g_light.channel.red, RGB.red);
            g_light.dev.set_channel(g_light.channel.green, RGB.green);
            g_light.dev.set_channel(g_light.channel.blue, RGB.blue);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    case LIGHT_WORK_MODE_WHITE:
        int brightness = 0;
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_1CH_C:
            if (g_light.cur_level) {
                brightness = g_light.cur_brightness;
            }
            g_light.dev.set_channel(g_light.channel.cold, brightness);
            break;
        case LIGHT_CHANNEL_COMB_1CH_W:
            if (g_light.cur_level) {
                brightness = g_light.cur_brightness;
            }
            g_light.dev.set_channel(g_light.channel.warm, brightness);
            break;
        case LIGHT_CHANNEL_COMB_2CH_CW:
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            CW_white_t CW = {0};
            if (g_light.cur_level) {
                temp_to_cw(g_light.cur_cct, &CW);
                process_cct_limit(&CW, &CW, g_light.cur_brightness);
            }
            g_light.dev.set_channel(g_light.channel.cold, CW.cold);
            g_light.dev.set_channel(g_light.channel.warm, CW.warm);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    default:
        printf("Invalid light mode");
    }
    return 0;
}


static int light_driver_update_effect(int brightness)
{
    // printf("%s(%d)\r\n", __func__, brightness);

    /* check current color mode */
    /* if in color mode, set rgb channel only; if in white mode, set cw channel only */
    switch (g_light.cur_effect.mode) {
    case LIGHT_WORK_MODE_COLOR:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_3CH_RGB:
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            RGB_color_t RGB;
            process_color_limit(&RGB, &g_light.cur_effect.RGB, brightness);
            g_light.dev.set_channel(g_light.channel.red, RGB.red);
            g_light.dev.set_channel(g_light.channel.green, RGB.green);
            g_light.dev.set_channel(g_light.channel.blue, RGB.blue);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    case LIGHT_WORK_MODE_WHITE:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_1CH_C:
            g_light.dev.set_channel(g_light.channel.cold, brightness);
            break;
        case LIGHT_CHANNEL_COMB_1CH_W:
            g_light.dev.set_channel(g_light.channel.warm, brightness);
            break;
        case LIGHT_CHANNEL_COMB_2CH_CW:
            CW_white_t CW;
            temp_to_cw(g_light.cur_effect.cct, &CW);
            process_cct_limit(&CW, &CW, brightness);
            g_light.dev.set_channel(g_light.channel.cold, CW.cold);
            g_light.dev.set_channel(g_light.channel.warm, CW.warm);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    default:
        printf("Invalid light mode");
    }
    return 0;
}

int light_driver_set_brightness(uint8_t val)
{
    printf("%s(%d)\r\n", __func__, val);

    g_light.cur_brightness = val;
    return light_driver_update();
}

int light_driver_set_power(uint8_t val)
{
    printf("%s:(%d)\r\n", __func__, val);
    g_light.cur_level = val;
    return light_driver_update();
}

int light_driver_set_hue(uint16_t val)
{
    printf("%s(%d)\r\n", __func__, val);

    if (g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_C
                || g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_W
                || g_light.channel_comb == LIGHT_CHANNEL_COMB_2CH_CW) {
        printf("%s: hue not supported by %d\r\n", __func__, g_light.channel_comb);
        return -1;
    }

    g_light.cur_hs.hue = val;
    return light_driver_update();
}

int light_driver_set_saturation(uint8_t val)
{
    printf("%s(%d)\r\n", __func__, val);

    if (g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_C
                || g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_W
                || g_light.channel_comb == LIGHT_CHANNEL_COMB_2CH_CW) {
        printf("%s: saturation not supported by %d\r\n", __func__, g_light.channel_comb);
        return -1;
    }

    g_light.cur_hs.saturation = val;
    return light_driver_update();
}

int light_driver_set_temperature(uint32_t val)
{
    printf("%s(%ld)\r\n", __func__, val);

    if (g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_C
                || g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_W) {
        printf("%s: temp not supported by %d\r\n", __func__, g_light.channel_comb);
        return -1;
    }

    g_light.cur_cct = val;
    return light_driver_update();
}

int light_driver_set_color_mode(uint8_t val)
{
    int ret = 0;
    printf("%s(%d)\r\n", __func__, val);

    if (val != LIGHT_WORK_MODE_COLOR && val != LIGHT_WORK_MODE_WHITE) {
        printf("%s: Unrecognized work mode\r\n", __func__);
        return -1;
    }

    if (val == LIGHT_WORK_MODE_COLOR) {
        if (g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_C
                    || g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_W
                    || g_light.channel_comb == LIGHT_CHANNEL_COMB_2CH_CW) {
            printf("%s: temp not supported by work mode %d\r\n", __func__, g_light.channel_comb);
            return -1;
        }
    }

    if (val == LIGHT_WORK_MODE_WHITE) {
        if (g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_C
                    || g_light.channel_comb == LIGHT_CHANNEL_COMB_1CH_W) {
            printf("%s: temp not supported by work mode %d\r\n", __func__, g_light.channel_comb);
            return -1;
        }
    }

    /* first turn off light */
    uint8_t old_level = g_light.cur_level;
    g_light.cur_level = 0;
    ret |= light_driver_update();

    /* then change color mode and turn on light */
    g_light.work_mode = val;
    g_light.cur_level = old_level;
    ret |= light_driver_update();

    return ret;
}

static void light_driver_channel_fade_start(uint8_t channel, uint8_t start, uint8_t end, uint32_t speed)
{
    switch (g_light.dev_type) {
    case LIGHT_DEVICE_TYPE_LED:
        g_light.dev.hw_fade_start(channel, start, end, speed);
        break;
    default:
        break;
    }
}

static void light_driver_channel_fade_end(uint8_t channel)
{
    switch (g_light.dev_type) {
    case LIGHT_DEVICE_TYPE_LED:
        g_light.dev.hw_fade_end(channel);
        g_light.dev.set_channel(channel, 0); // TODO: set duty to 0 when fade ends
        break;
    default:
        break;
    }
}

static void light_driver_effect_fade_start(uint8_t start, uint8_t end, uint32_t speed)
{
    // printf("%s(%d, %d, %d)\r\n", __func__, start, end, speed);

    /* check current color mode */
    /* if in color mode, set rgb channel only; if in white mode, set cw channel only */
    switch (g_light.cur_effect.mode) {
    case LIGHT_WORK_MODE_COLOR:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_3CH_RGB:
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            RGB_color_t RGB_start = {0}, RGB_end = {0};
            process_color_limit(&RGB_start, &g_light.cur_effect.RGB, start);
            process_color_limit(&RGB_end, &g_light.cur_effect.RGB, end);
            light_driver_channel_fade_start(g_light.channel.red, RGB_start.red, RGB_end.red, speed);
            light_driver_channel_fade_start(g_light.channel.green, RGB_start.green, RGB_end.green, speed);
            light_driver_channel_fade_start(g_light.channel.blue, RGB_start.blue, RGB_end.blue, speed);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    case LIGHT_WORK_MODE_WHITE:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_1CH_C:
            light_driver_channel_fade_start(g_light.channel.cold, start, end, speed);
            break;
        case LIGHT_CHANNEL_COMB_1CH_W:
            light_driver_channel_fade_start(g_light.channel.warm, start, end, speed);
            break;
        case LIGHT_CHANNEL_COMB_2CH_CW:
            CW_white_t CW_start={0}, CW_end={0};
            temp_to_cw(g_light.cur_effect.cct, &CW_start);
            process_cct_limit(&CW_start, &CW_start, start);
            temp_to_cw(g_light.cur_effect.cct, &CW_end);
            process_cct_limit(&CW_end, &CW_end, end);
            light_driver_channel_fade_start(g_light.channel.cold, CW_start.cold, CW_end.cold, speed);
            light_driver_channel_fade_start(g_light.channel.warm, CW_start.warm, CW_end.warm, speed);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    default:
        printf("Invalid light mode");
    }
}

// TODO: similar to light_driver_effect_fade_start()
void light_driver_effect_fade_end(void)
{
    /* check current color mode */
    /* if in color mode, set rgb channel only; if in white mode, set cw channel only */
    switch (g_light.cur_effect.mode) {
    case LIGHT_WORK_MODE_COLOR:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_3CH_RGB:
        case LIGHT_CHANNEL_COMB_5CH_RGBCW:
            light_driver_channel_fade_end(g_light.channel.red);
            light_driver_channel_fade_end(g_light.channel.green);
            light_driver_channel_fade_end(g_light.channel.blue);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    case LIGHT_WORK_MODE_WHITE:
        switch (g_light.channel_comb) {
        case LIGHT_CHANNEL_COMB_1CH_C:
            light_driver_channel_fade_end(g_light.channel.cold);
            break;
        case LIGHT_CHANNEL_COMB_1CH_W:
            light_driver_channel_fade_end(g_light.channel.warm);
            break;
        case LIGHT_CHANNEL_COMB_2CH_CW:
            light_driver_channel_fade_end(g_light.channel.cold);
            light_driver_channel_fade_end(g_light.channel.warm);
            break;
        default:
            printf("%s:%d: Incompatible work mode %d with channel comb %d\r\n", __func__, __LINE__, g_light.work_mode, g_light.channel_comb);
            break;
        }
        break;
    default:
        printf("Invalid light mode");
    }
}

static void light_effect_handler(lp_sw_timer_handle_t timer_handle, void *arg)
{
    switch (g_light.cur_effect.type) {
    case LIGHT_EFFECT_BLINK:
        int brightness = g_light.cur_effect.max_brightness;
        if (g_light.cur_effect.rounds % 2 == 0) {
            brightness = g_light.cur_effect.min_brightness;
        }
        light_driver_update_effect(brightness);
        break;
    case LIGHT_EFFECT_BREATHE:
        int start_brightness = g_light.cur_effect.max_brightness;
        int end_brightness = g_light.cur_effect.min_brightness;
        if (g_light.cur_effect.rounds % 2 == 0) {
            start_brightness = g_light.cur_effect.min_brightness;
            end_brightness = g_light.cur_effect.max_brightness;
        }
        // printf("%s:%d: start:%d, end:%d\r\n", __func__, __LINE__, start_brightness, end_brightness);
        light_driver_update_effect(start_brightness);
        light_driver_effect_fade_start(start_brightness, end_brightness, g_light.cur_effect.speed / 2);
        break;
    default:
        break;
    }

    /* increase counter & check whether delete timer */
    g_light.cur_effect.rounds++;

    /* if total_ms == 0, repeat infinitely until timer is deleted */
    if (g_light.cur_effect.total_ms == 0) {
        return;
    }

    if (g_light.cur_effect.rounds >= 2 * g_light.cur_effect.total_ms / g_light.cur_effect.speed) {
        light_driver_effect_stop();
        printf("%s: end of effect\r\n", __func__);
    }
}


void light_driver_effect_start(light_effect_config_t *config, int speed, int total_ms)
{
    printf("%s(config, %d, %d)\r\n", __func__, speed, total_ms);

    g_light.cur_effect.type = config->type;
    switch (config->mode) {
    case LIGHT_WORK_MODE_COLOR:
        g_light.cur_effect.RGB = config->color.RGB;
        break;
    case LIGHT_WORK_MODE_WHITE:
        g_light.cur_effect.cct = config->color.cct;
        break;
    default:
        break;
    }

    g_light.cur_effect.max_brightness = config->max_brightness;
    g_light.cur_effect.min_brightness = config->min_brightness;
    g_light.cur_effect.mode = config->mode;
    g_light.cur_effect.total_ms = total_ms;
    g_light.cur_effect.speed = speed;

    /* each time we start a new effect, stop the previous effect */
    lp_sw_timer_delete(g_light.cur_effect.timer);
    light_driver_effect_stop();

    lp_sw_timer_config_t timer_cfg = {
        .arg = NULL,
        .handler = light_effect_handler,
        .periodic = true,
        .timeout_ms = speed / 2, /* change brightness every half period */
    };
    lp_sw_timer_handle_t timer = lp_sw_timer_create(&timer_cfg);

    /* timer */
    g_light.cur_effect.timer = timer;
    g_light.cur_effect.rounds = 0; /* reset effect rounds to 0 */

    printf("effect(type=%d, max=%d, min=%d, speed=%d, total_ms=%d, timer=%p)\r\n", 
        g_light.cur_effect.type, g_light.cur_effect.max_brightness, g_light.cur_effect.min_brightness,
        g_light.cur_effect.speed, g_light.cur_effect.total_ms, g_light.cur_effect.timer);

    lp_sw_timer_start(g_light.cur_effect.timer);

    /* execute the first effect: set to max brightness */
    switch (g_light.cur_effect.type) {
    case LIGHT_EFFECT_BLINK:
        light_driver_update_effect(100);
        break;
    case LIGHT_EFFECT_BREATHE:
        light_driver_update_effect(100);
        light_driver_effect_fade_start(g_light.cur_effect.max_brightness,
                        g_light.cur_effect.min_brightness,
                        g_light.cur_effect.speed / 2);
        break;
    default:
        break;
    }
}

void light_driver_effect_stop(void)
{
    /* set power also set brightness to cur_brightness */
    lp_sw_timer_delete(g_light.cur_effect.timer);
    light_driver_effect_fade_end();
    light_driver_set_power(g_light.cur_level);
}
