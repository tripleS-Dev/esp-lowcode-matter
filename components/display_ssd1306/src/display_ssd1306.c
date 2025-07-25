/*
 * SPDX-FileCopyrightText: 2015-2023 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "i2c_master.h"
#include "display_ssd1306.h"
#include "string.h" // for memset

#define SSD1306_WRITE_CMD           (0x00)
#define SSD1306_WRITE_DAT           (0x40)

#define COORDINATE_SWAP(x1, x2, y1, y2)  { int16_t temp = x1; x1 = x2, x2 = temp; \
                                                   temp = y1; y1 = y2; y2 = temp; }

#define DISPLAY_BUFFER(dev) ((uint8_t (*)[SSD1306_HEIGHT / 8])((dev)->data_buf + 1))
#define CMD_BUF(dev) ((dev)->cmd_buf + 1)

static const char *TAG = "display_ssd1306";

typedef struct {
    uint16_t dev_addr;
    int i2c_port;
    ssd1306_i2c_write_t write;
    uint8_t cmd_buf[SSD1306_CMD_LEN + 1];
    uint8_t data_buf[SSD1306_WIDTH * (SSD1306_HEIGHT / 8) + 1];
} ssd1306_dev_t;

static uint32_t _pow(uint8_t m, uint8_t n)
{
    uint32_t result = 1;
    while (n--) {
        result *= m;
    }
    return result;
}

static esp_err_t ssd1306_write_data(display_ssd1306_handle_t dev, const uint8_t *const data, const uint16_t data_len)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    esp_err_t ret;

    if (device->write == NULL) {
        return ESP_FAIL;
    }
    ret = device->write(device->i2c_port, device->dev_addr, data, data_len, -1);
    return ret;
}

static esp_err_t ssd1306_write_cmd(display_ssd1306_handle_t dev, const uint8_t *const data, const uint16_t data_len)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    esp_err_t ret;

    if (data_len > SSD1306_CMD_LEN) {
        printf("%s: cmd size is too long\n", TAG);
        return ESP_FAIL;
    }

    device->cmd_buf[0] = SSD1306_WRITE_CMD;
    memcpy(CMD_BUF(device), data, data_len);

    if (device->write == NULL) return ESP_FAIL;
    ret = device->write(device->i2c_port, device->dev_addr, device->cmd_buf, data_len + 1, -1 /* wait forever */);
    return ret;
}

static inline esp_err_t ssd1306_write_cmd_byte(display_ssd1306_handle_t dev, const uint8_t cmd)
{
    return ssd1306_write_cmd(dev, &cmd, 1);
}

void ssd1306_fill_rectangle(display_ssd1306_handle_t dev, uint8_t chXpos1,
                            uint8_t chYpos1, uint8_t chXpos2, uint8_t chYpos2, uint8_t chDot)
{
    uint8_t chXpos, chYpos;

    for (chXpos = chXpos1; chXpos <= chXpos2; chXpos++) {
        for (chYpos = chYpos1; chYpos <= chYpos2; chYpos++) {
            ssd1306_fill_point(dev, chXpos, chYpos, chDot);
        }
    }
}

void ssd1306_draw_num(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos,
                      uint32_t chNum, uint8_t chLen, uint8_t chSize)
{
    uint8_t i;
    uint8_t chTemp, chShow = 0;

    for (i = 0; i < chLen; i++) {
        chTemp = (chNum / _pow(10, chLen - i - 1)) % 10;
        if (chShow == 0 && i < (chLen - 1)) {
            if (chTemp == 0) {
                ssd1306_draw_char(dev, chXpos + (chSize / 2) * i, chYpos,
                                  ' ', chSize, 1);
                continue;
            } else {
                chShow = 1;
            }
        }
        ssd1306_draw_char(dev, chXpos + (chSize / 2) * i, chYpos,
                          chTemp + '0', chSize, 1);
    }
}

void ssd1306_draw_char(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos,
                       uint8_t chChr, uint8_t chSize, uint8_t chMode)
{
    uint8_t i, j;
    uint8_t chTemp, chYpos0 = chYpos;

    chChr = chChr - ' ';
    for (i = 0; i < chSize; i++) {
        if (chSize == 12) {
            if (chMode) {
                chTemp = c_chFont1206[chChr][i];
            } else {
                chTemp = ~c_chFont1206[chChr][i];
            }
        } else {
            if (chMode) {
                chTemp = c_chFont1608[chChr][i];
            } else {
                chTemp = ~c_chFont1608[chChr][i];
            }
        }

        for (j = 0; j < 8; j++) {
            if (chTemp & 0x80) {
                ssd1306_fill_point(dev, chXpos, chYpos, 1);
            } else {
                ssd1306_fill_point(dev, chXpos, chYpos, 0);
            }
            chTemp <<= 1;
            chYpos++;

            if ((chYpos - chYpos0) == chSize) {
                chYpos = chYpos0;
                chXpos++;
                break;
            }
        }
    }
}

void display_ssd1306_draw_string(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos,
                         const uint8_t *pchString, uint8_t chSize, uint8_t chMode)
{
    while (*pchString != '\0') {
        if (chXpos > (SSD1306_WIDTH - chSize / 2)) {
            chXpos = 0;
            chYpos += chSize;
            if (chYpos > (SSD1306_HEIGHT - chSize)) {
                chYpos = chXpos = 0;
                display_ssd1306_clear_screen(dev, 0x00);
            }
        }
        ssd1306_draw_char(dev, chXpos, chYpos, *pchString, chSize, chMode);
        chXpos += chSize / 2;
        pchString++;
    }
}

void ssd1306_fill_point(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos, uint8_t chPoint)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    uint8_t chPos, chBx, chTemp = 0;

    if (chXpos >= SSD1306_WIDTH || chYpos >= SSD1306_HEIGHT) {
        printf("%s: out of bound: chXpos: %d, chYpos: %d\n", TAG, chXpos, chYpos);
        return;
    }
    chPos = 7 - chYpos / 8;
    chBx = chYpos % 8;
    chTemp = 1 << (7 - chBx);

    if (chPoint) {
        (DISPLAY_BUFFER(device))[chXpos][chPos] |= chTemp;
    } else {
        (DISPLAY_BUFFER(device))[chXpos][chPos] &= ~chTemp;
    }
}

void ssd1306_draw_1616char(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos, uint8_t chChar)
{
    uint8_t i, j;
    uint8_t chTemp = 0, chYpos0 = chYpos, chMode = 0;

    for (i = 0; i < 32; i++) {
        chTemp = c_chFont1612[chChar - 0x30][i];
        for (j = 0; j < 8; j++) {
            chMode = chTemp & 0x80 ? 1 : 0;
            ssd1306_fill_point(dev, chXpos, chYpos, chMode);
            chTemp <<= 1;
            chYpos++;
            if ((chYpos - chYpos0) == 16) {
                chYpos = chYpos0;
                chXpos++;
                break;
            }
        }
    }
}

void ssd1306_draw_3216char(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos, uint8_t chChar)
{
    uint8_t i, j;
    uint8_t chTemp = 0, chYpos0 = chYpos, chMode = 0;

    for (i = 0; i < 64; i++) {
        chTemp = c_chFont3216[chChar - 0x30][i];
        for (j = 0; j < 8; j++) {
            chMode = chTemp & 0x80 ? 1 : 0;
            ssd1306_fill_point(dev, chXpos, chYpos, chMode);
            chTemp <<= 1;
            chYpos++;
            if ((chYpos - chYpos0) == 32) {
                chYpos = chYpos0;
                chXpos++;
                break;
            }
        }
    }
}

void ssd1306_draw_bitmap(display_ssd1306_handle_t dev, uint8_t chXpos, uint8_t chYpos,
                         const uint8_t *pchBmp, uint8_t chWidth, uint8_t chHeight)
{
    uint16_t i, j, byteWidth = (chWidth + 7) / 8;

    for (j = 0; j < chHeight; j++) {
        for (i = 0; i < chWidth; i++) {
            if (*(pchBmp + j * byteWidth + i / 8) & (128 >> (i & 7))) {
                ssd1306_fill_point(dev, chXpos + i, chYpos + j, 1);
            }
        }
    }
}

void ssd1306_draw_line(display_ssd1306_handle_t dev, int16_t chXpos1, int16_t chYpos1, int16_t chXpos2, int16_t chYpos2)
{
    // 16-bit variables allowing a display overflow effect
    int16_t x_len = abs(chXpos1 - chXpos2);
    int16_t y_len = abs(chYpos1 - chYpos2);

    if (y_len < x_len) {
        if (chXpos1 > chXpos2) {
            COORDINATE_SWAP(chXpos1, chXpos2, chYpos1, chYpos2);
        }
        int16_t len = x_len;
        int16_t diff = y_len;

        do {
            if (diff >= x_len) {
                diff -= x_len;
                if (chYpos1 < chYpos2) {
                    chYpos1++;
                } else {
                    chYpos1--;
                }
            }

            diff += y_len;
            ssd1306_fill_point(dev, chXpos1++, chYpos1, 1);
        } while (len--);
    }

    else {
        if (chYpos1 > chYpos2) {
            COORDINATE_SWAP(chXpos1, chXpos2, chYpos1, chYpos2);
        }
        int16_t len = y_len;
        int16_t diff = x_len;

        do {
            if (diff >= y_len) {
                diff -= y_len;
                if (chXpos1 < chXpos2) {
                    chXpos1++;
                } else {
                    chXpos1--;
                }
            }

            diff += x_len;
            ssd1306_fill_point(dev, chXpos1, chYpos1++, 1);
        } while (len--);
    }
}

esp_err_t ssd1306_init(display_ssd1306_handle_t dev)
{
    esp_err_t ret;

    ssd1306_write_cmd_byte(dev, 0xAE); //--turn off oled panel
    ssd1306_write_cmd_byte(dev, 0x40); //--set start line address  Set Mapping RAM Display Start Line (0x00~0x3F)
    ssd1306_write_cmd_byte(dev, 0x81); //--set contrast control register
    ssd1306_write_cmd_byte(dev, 0xCF); // Set SEG Output Current Brightness
    ssd1306_write_cmd_byte(dev, 0xA1); //--Set SEG/Column Mapping
    ssd1306_write_cmd_byte(dev, 0xC0); //Set COM/Row Scan Direction
    ssd1306_write_cmd_byte(dev, 0xA6); //--set normal display
    ssd1306_write_cmd_byte(dev, 0xA8); //--set multiplex ratio(1 to 64)
    ssd1306_write_cmd_byte(dev, 0x3f); //--1/64 duty
    ssd1306_write_cmd_byte(dev, 0xd5); //--set display clock divide ratio/oscillator frequency
    ssd1306_write_cmd_byte(dev, 0x80); //--set divide ratio, Set Clock as 100 Frames/Sec
    ssd1306_write_cmd_byte(dev, 0xD9); //--set pre-charge period
    ssd1306_write_cmd_byte(dev, 0xF1); //Set Pre-Charge as 15 Clocks & Discharge as 1 Clock
    ssd1306_write_cmd_byte(dev, 0xDA); //--set com pins hardware configuration
    ssd1306_write_cmd_byte(dev, 0xDB); //--set vcomh
    ssd1306_write_cmd_byte(dev, 0x40); //Set VCOM Deselect Level
    ssd1306_write_cmd_byte(dev, 0x8D); //--set Charge Pump enable/disable
    ssd1306_write_cmd_byte(dev, 0x14); //--set(0x10) disable
    ssd1306_write_cmd_byte(dev, 0xA4); // Disable Entire Display On (0xa4/0xa5)
    ssd1306_write_cmd_byte(dev, 0xA6); // Disable Inverse Display On (0xa6/a7)

    const uint8_t cmd[2] = {0x20, 1}; //-- set vertical adressing mode
    ssd1306_write_cmd(dev, cmd, sizeof(cmd));

    uint8_t cmd2[3] = {0x21, 0, 127};
    ssd1306_write_cmd(dev, cmd2, sizeof(cmd2)); //--set column address to zero
    cmd2[0] = 0x22;
    cmd2[2] = 7;
    ssd1306_write_cmd(dev, cmd2, sizeof(cmd2)); //--set row address to zero

    ret = ssd1306_write_cmd_byte(dev, 0xAF); //--turn on oled panel

    display_ssd1306_clear_screen(dev, 0x00);
    return ret;
}

static int display_ssd1306_i2c_write(int i2c_port, uint16_t dev_addr, uint8_t *data, uint16_t data_len, int timeout)
{
    int timeout_tick = 0;
    if (timeout == -1) {
        timeout_tick = -1;
    } else {
        timeout_tick = timeout * 16000;
    }
    esp_err_t err = i2c_master_write_to_device(i2c_port, dev_addr, data, data_len, timeout_tick);
    if (err != ESP_OK) {
        printf("%s: i2c write failed. err=%d\n", TAG, err);
        return -1;
    }
    return 0;
}

display_ssd1306_handle_t display_ssd1306_i2c_create(uint16_t dev_addr, int i2c_port)
{
    ssd1306_dev_t *dev = (ssd1306_dev_t *) calloc(1, sizeof(ssd1306_dev_t));
    if (!dev) {
        printf("%s: Failed to allocate memory for ssd1306 handle\n", TAG);
        return NULL;
    }
    dev->dev_addr = dev_addr;
    dev->i2c_port = i2c_port;
    dev->write = display_ssd1306_i2c_write;
    ssd1306_init((display_ssd1306_handle_t) dev);
    return (display_ssd1306_handle_t) dev;
}

void ssd1306_delete(display_ssd1306_handle_t dev)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    free(device);
}

esp_err_t display_ssd1306_refresh_gram(display_ssd1306_handle_t dev)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    device->data_buf[0] = SSD1306_WRITE_DAT;
    return ssd1306_write_data(dev, device->data_buf, SSD1306_DATA_LEN + 1);
}

void display_ssd1306_clear_screen(display_ssd1306_handle_t dev, uint8_t chFill)
{
    ssd1306_dev_t *device = (ssd1306_dev_t *) dev;
    memset(DISPLAY_BUFFER(device), chFill, SSD1306_DATA_LEN);
}
