// Copyright 2022 Espressif Systems (Shanghai) CO LTD
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License

#include <string.h>

#include <ulp_lp_core_utils.h>

#include "occupancy_sensor_ld2420.h"

#define BAUDRATE 115200

#define VERSION_BUF_SIZE 15
#define RECEIVE_BUFFER_SIZE 50
#define UART_RECEIVE_TIMEOUT 500 // in ms

#define CONFIGURATION_MODE_BUF_SIZE 18
#define CONFIGURATION_MODE_RETURN_COMMAND 0x01FF
#define LEAVE_CONFIGURATION_MODE_RETURN_COMMAND 0x01FE
#define CONFIGURE_SYSTEM_PARAM_RETURN_COMMAND 0x0112
#define VERSION_RETURN_COMMAND 0x0100
#define WRITE_REGISTER_RETURN_COMMAND 0x0101
#define READ_REGISTER_RETURN_COMMAND 0x0102

#define CHIP_ADDRESS 0x0040

#define REPORT_MODE 0x00000004
#define NORMAL_MODE 0x00000040
#define DEBUG_MODE  0x00000400

#define MINIMUM_DISTANCE_REGISTER 0x0000
#define MAXIMUM_DISTANCE_REGISTER 0x0001

#define ABSENCE_REPORT_DELAY_REGISTER 0x0004

#define TRIGGER_THRESHOLD_REGISTER 0x0010
#define HOLD_THRESHOLD_REGISTER 0x0020

#define MAX_GATE 0x0F
#define MIN_DISTANCE 0 // (in m)
#define MAX_DISTANCE 15 // (in m)
#define MAX_ABSENCE_REPORT_DELAY  0xFFFF // (in sec)
#define MAX_TRIGGER_THRESHOLD  232 // (in db)
#define MAX_HOLD_THRESHOLD  232 // (in db)

static const char *TAG = "occupancy_sensor_ld2420";

typedef struct {
    uart_port_t uart_num;
    int ot_pin;
} ld2420_driver_t;

static ld2420_driver_t ld2420[CONFIG_MAX_LD2420_OCCUPANCY_SENSOR];
static int ld2420_count = 0;

static const uint8_t preamble_cmd[] = {0xFD, 0xFC, 0xFB, 0xFA};
static const uint8_t postamble_cmd[] = {0x04, 0x03, 0x02, 0x01};
static const uint8_t enter_configuration_mode_cmd[] = {0x04, 0x00, 0xFF, 0x00, 0x01, 0x00};
static const uint8_t leave_configuration_mode_cmd[] = {0x02, 0x00, 0xFE, 0x00};

static const uint8_t firmware_version_cmd[] = {0x02, 0x00, 0x00, 0x00};

static const uint8_t report_data_preamble_cmd[] = {0xF4, 0xF3, 0xF2, 0xF1};
static const uint8_t report_data_postamble_cmd[] = {0xF8, 0xF7, 0xF6, 0xF5};

static void ld2420_write_bytes(ld2420_driver_t *handle, uint8_t *data, size_t size)
{
    uart_write_bytes(handle->uart_num, data, size, 500);
}

static int ld2420_read_return_command(ld2420_driver_t *handle, uint8_t *buf, size_t size, uint16_t *return_command, uint16_t *success_command, uint16_t *buf_size)
{
    uint8_t rx_buffer[RECEIVE_BUFFER_SIZE];
    int rx_len = uart_read_bytes(handle->uart_num, rx_buffer, sizeof(rx_buffer), 500);
    if (!rx_len) {
        printf("%s: No data received\n", TAG);
        return -1;
    }

    int start = -1;
    for (int i = 0; i <= sizeof(rx_buffer) - sizeof(preamble_cmd); i++) {
        if (!memcmp(&rx_buffer[i], preamble_cmd, sizeof(preamble_cmd))) {
            start = i;
            break;
        }
    }
    if (start < 0) {
        printf("%s: No valid preamble cmd found\n", TAG);
        return -1;
    }

    uint16_t index = start + sizeof(preamble_cmd);
    uint16_t command_frame_size = rx_buffer[index + 1] << 8 | rx_buffer[index];

    index += 2;
    *return_command = rx_buffer[index + 1] << 8 | rx_buffer[index];

    index += 2;
    *success_command = rx_buffer[index + 1] << 8 | rx_buffer[index];

    // since 2 + 2 bytes are used for return command and success_command respectively
    if (command_frame_size - 4 > size) {
        printf("%s: Buffer overflow\n", TAG);
        return -1;
    }
    index += 2;
    int result_data_size = command_frame_size - 4;
    if (result_data_size) {
        memcpy(buf, &rx_buffer[index], command_frame_size - 4);
        *buf_size = command_frame_size - 4;
    }
    index += result_data_size;

    if (memcmp(&rx_buffer[index], postamble_cmd, sizeof(postamble_cmd))) {
        printf("%s: Invalid postamble in received command\n", TAG);
        return -1;
    }
    return 0;
}

static void send_command_preamble(ld2420_driver_t *handle)
{
    ld2420_write_bytes(handle, preamble_cmd, sizeof(preamble_cmd));
}

static void send_command_postamble(ld2420_driver_t *handle)
{
    ld2420_write_bytes(handle, postamble_cmd, sizeof(postamble_cmd));
}

static void send_command(ld2420_driver_t *handle, uint8_t *buffer, size_t size)
{
    send_command_preamble(handle);
    ld2420_write_bytes(handle, buffer, size);
    send_command_postamble(handle);
    ulp_lp_core_delay_us(25000);
}

static int enter_configuration_mode(ld2420_driver_t *handle)
{
    send_command(handle, enter_configuration_mode_cmd, sizeof(enter_configuration_mode_cmd)); 

    uint8_t rx_buffer[CONFIGURATION_MODE_BUF_SIZE] = {0};
    uint16_t return_command, success_command, buf_size;
    if (ld2420_read_return_command(handle, rx_buffer, sizeof(rx_buffer), &return_command, &success_command, &buf_size)) {
        printf("%s: Failed to read buffer\n", TAG);
        return -1;
    }
    if (return_command != CONFIGURATION_MODE_RETURN_COMMAND) {
        printf("%s: Received invalid configuration mode return command\n", TAG);
        return -1;
    }
    if (success_command) {
        printf("%s: Failed to enter configuration mode\n", TAG);
        return -1;
    }
    return 0;
}

static int leave_configuration_mode(ld2420_driver_t *handle)
{
    send_command(handle, leave_configuration_mode_cmd, sizeof(leave_configuration_mode_cmd));

    uint16_t return_command, success_command, buf_size;
    if (ld2420_read_return_command(handle, NULL, 0, &return_command, &success_command, &buf_size)) {
        printf("%s: Failed to read buffer when leaving configuration mode\n", TAG);
        return -1;
    }
    if (return_command != LEAVE_CONFIGURATION_MODE_RETURN_COMMAND) {
        printf("%s: Received invalid leave configuration return command\n", TAG);
        return -1;
    }
    if (success_command) {
        printf("%s: Failed to leave configuration mode\n", TAG);
        return -1;
    }

    return 0;
}

int occupancy_sensor_ld2420_get_firmware_version(occupancy_sensor_ld2420_handle_t handle, char *buffer, size_t size)
{
    if (!enter_configuration_mode(handle)) {
        ulp_lp_core_delay_us(50000);
        send_command(handle, firmware_version_cmd, sizeof(firmware_version_cmd));

        uint8_t rx_buffer[VERSION_BUF_SIZE];
        uint16_t return_command, success_command, buf_size;
        if (ld2420_read_return_command(handle, rx_buffer, sizeof(rx_buffer), &return_command, &success_command, &buf_size)) {
            printf("%s: Failed to read buffer\n", TAG);
            return -1;
        }
        if (return_command != VERSION_RETURN_COMMAND) {
            printf("%s: Received invalid version return command\n", TAG);
            return -1;
        }
        if (success_command) {
            printf("%s: Failed to read version\n", TAG);
            return -1;
        }
        uint16_t version_size = rx_buffer[1] << 8 | rx_buffer[0];
        if (version_size + 1 > size) {
            printf("%s: buffer size not enough to store firmware version\n", TAG);
            return -1;
        }
        memcpy(buffer, &rx_buffer[2], version_size);
        buffer[version_size] = '\0';
        leave_configuration_mode(handle);
    } else {
        return -1;
    }
    return 0;
}

static int ld2420_write_register(ld2420_driver_t *handle, uint16_t address, uint16_t data)
{
    uint16_t chip_address = CHIP_ADDRESS;
    uint8_t buf [10] = {0x08, 0x00, 0x01, 0x00};
    memcpy(&buf[4], &chip_address, sizeof(chip_address));
    memcpy(&buf[6], &address, sizeof(address));
    memcpy(&buf[8], &data, sizeof(data));

    send_command(handle, buf, sizeof(buf));

    uint16_t return_command, success_command, buf_size;
    if (ld2420_read_return_command(handle, NULL, 0, &return_command, &success_command, &buf_size)) {
        printf("%s: Failed to read buffer when setting minimum distance\n", TAG);
        return -1;
    }
    if (return_command != WRITE_REGISTER_RETURN_COMMAND) {
        printf("%s: Recevied invalid write register return command\n", TAG);
        return -1;
    }
    if (success_command) {
        printf("%s: Failed to write register address: %04x\n", TAG, address);
        return -1;
    }
    return 0;
}

int occupancy_sensor_ld2420_set_minimum_distance(occupancy_sensor_ld2420_handle_t handle, uint16_t minimum_distance)
{
    if (minimum_distance > MAX_DISTANCE) {
        printf("%s: Invalid minimum distance value passed\n", TAG);
        return -1;
    }

    if (ld2420_write_register(handle, MINIMUM_DISTANCE_REGISTER, minimum_distance)) {
        printf("%s: Failed to configure the minimum distance\n", TAG);
        return -1;
    }

    return 0;
}

int occupancy_sensor_ld2420_set_maximum_distance(occupancy_sensor_ld2420_handle_t handle, uint16_t maximum_distance)
{
    if (maximum_distance > MAX_DISTANCE) {
        printf("%s: Invalid maximum distance value passed\n", TAG);
        return -1;
    }

    if (ld2420_write_register(handle, MAXIMUM_DISTANCE_REGISTER, maximum_distance)) {
        printf("%s: Failed to configure the maximum distance\n", TAG);
        return -1;
    }

    return 0;
}

int occupancy_sensor_ld2420_set_absence_report_delay(occupancy_sensor_ld2420_handle_t handle, uint16_t delay_s)
{
    if (ld2420_write_register(handle, ABSENCE_REPORT_DELAY_REGISTER, delay_s)) {
        printf("%s: Failed to configure the absence report delay\n", TAG);
        return -1;
    }
    return 0;
}

int occupancy_sensor_ld2420_set_gate_trigger_threshold(occupancy_sensor_ld2420_handle_t handle, uint8_t gate_index, uint16_t threshold)
{
    if (gate_index > MAX_GATE) {
        printf("%s: Invalid gate index passed\n", TAG);
        return -1;
    }
    if (threshold > MAX_TRIGGER_THRESHOLD) {
        printf("%s: Invalid trigger threshold value\n", TAG);
        return -1;
    }

    if (ld2420_write_register(handle, TRIGGER_THRESHOLD_REGISTER + gate_index, threshold)) {
        printf("%s: Failed to configure the gate trigger threshold\n", TAG);
        return -1;
    }

    return 0;
}

int occupancy_sensor_ld2420_set_gate_hold_threshold(occupancy_sensor_ld2420_handle_t handle, uint8_t gate_index, uint16_t threshold)
{
    if (gate_index > MAX_GATE) {
        printf("%s: Invalid gate index passed\n", TAG);
        return -1;
    }
    if (threshold > MAX_HOLD_THRESHOLD) {
        printf("%s: Invalid hold threshold value\n", TAG);
        return -1;
    }

    if (ld2420_write_register(handle, HOLD_THRESHOLD_REGISTER + gate_index, threshold)) {
        printf("%s: Failed to configure the gate hold threshold\n", TAG);
        return -1;
    }

    return 0;
}

static int ld2420_configure_system_parameter(ld2420_driver_t *handle, uint16_t param, uint32_t param_val)
{
    uint8_t buf[10] = {0x08, 0x00, 0x12, 0x00};
    memcpy(&buf[4], &param, sizeof(param));
    memcpy(&buf[6], &param_val, sizeof(param_val));
    send_command(handle, buf, sizeof(buf));
    uint16_t return_command, success_command, buf_size;
    if (ld2420_read_return_command(handle, NULL, 0, &return_command, &success_command, &buf_size)) {
        printf("%s: Failed to read buffer when configuring system parameter\n", TAG);
        return -1;
    }
    if (return_command != CONFIGURE_SYSTEM_PARAM_RETURN_COMMAND) {
        printf("%s: Recevied invalid configure system parameter return command\n", TAG);
        return -1;
    }
    if (success_command) {
        printf("%s: Failed to configure system parameter: %d\n", TAG, param);
        return -1;
    } 
    return 0;
}

int occupancy_sensor_ld2420_enter_normal_mode(occupancy_sensor_ld2420_handle_t handle)
{
    return ld2420_configure_system_parameter(handle, 0, NORMAL_MODE);
}

int occupancy_sensor_ld2420_read_normal_data(occupancy_sensor_ld2420_handle_t handle, occupancy_sensor_ld2420_normal_mode_data_t *data)
{
    ld2420_driver_t *sensor_info = (ld2420_driver_t*) handle;
    uint8_t rx_buffer[30];
    int rx_len = uart_read_bytes(sensor_info->uart_num, rx_buffer, sizeof(rx_buffer) - 1, UART_RECEIVE_TIMEOUT);
    if (!rx_len) {
        printf("%s: %s No data received\n", TAG, __FUNCTION__);
        return -1;
    }
    rx_buffer[sizeof(rx_buffer) - 1] = '\0';

    const char *on_ptr = strstr(rx_buffer, "ON");
    const char *off_ptr = strstr(rx_buffer, "OFF");
    const char *range_ptr = strstr(rx_buffer, "Range ");

    if ((on_ptr || off_ptr) && range_ptr) {
        // Move past "Range " (6 characters) to the number
        data->range = atoi(range_ptr + 6);
        data->occupied = on_ptr ? 1 : 0;
    } else {
        printf("%s: %s Invalid or incomplete data.\n", TAG, __FUNCTION__);
        return -1;
    }
    return 0;
}

int occupancy_sensor_ld2420_enter_report_mode(occupancy_sensor_ld2420_handle_t handle)
{
    return ld2420_configure_system_parameter(handle, 0, REPORT_MODE);
} 

int occupancy_sensor_ld2420_read_report_data(occupancy_sensor_ld2420_handle_t handle, occupancy_sensor_ld2420_report_mode_data_t *data)
{
    if (!data) {
        printf("%s: invalid data handle passed\n", TAG);
        return -1;
    }

    ld2420_driver_t *sensor_info = (ld2420_driver_t*) handle;
    uint8_t rx_buffer[90];
    int rx_len = uart_read_bytes(sensor_info->uart_num, rx_buffer, sizeof(rx_buffer), 500);
    if (!rx_len) {
        printf("%s: %s No data received\n", TAG, __FUNCTION__);
        return -1;
    }
    int start = -1;
    for (int i = 0; i <= sizeof(rx_buffer) - sizeof(report_data_preamble_cmd); i++) {
        if (!memcmp(&rx_buffer[i], report_data_preamble_cmd, sizeof(report_data_preamble_cmd))) {
            start = i;
            break;
        }
    }
    if (start < 0) {
        printf("%s: No valid report data preamble cmd found\n", TAG);
        return -1;
    }
    int index = start + 4;

    uint16_t buf_len = rx_buffer[index + 1] << 8 | rx_buffer[index];
    if (buf_len != 35) {
        printf("%s: Invalid buffer length received\n", TAG);
        return -1;
    }
    index += 2;

    data->occupied = rx_buffer[index];
    index += 1;

    data->target_distance = rx_buffer[index + 1] << 8 | rx_buffer[index];
    index += 2;

    // copy 32 bytes of zone noise level data
    memcpy(data->zone_noise_level, &rx_buffer[index], 32);
    index += 32;

    if (memcmp(&rx_buffer[index], report_data_postamble_cmd, sizeof(report_data_postamble_cmd))) {
        printf("%s: Invalid report data postamble in received command\n", TAG);
        return -1;
    }

    return 0;
}

occupancy_sensor_ld2420_handle_t occupancy_sensor_ld2420_init(occupancy_sensor_ld2420_cfg_t *cfg)
{
    if (ld2420_count >= CONFIG_MAX_LD2420_OCCUPANCY_SENSOR) {
        printf("Increase CONFIG_MAX_LD2420_OCCUPANCY_SENSOR to configure more LD2420 sensors\n");
        return NULL;
    }

    /* uart driver configuration */
    uart_cfg_t uart_cfg = {
        .uart_pin_cfg = {
            .tx_io_num = cfg->tx_pin,
            .rx_io_num = cfg->rx_pin,
            .rts_io_num = -1,
            .cts_io_num = -1,
        },
        .uart_proto_cfg = {
            .baud_rate = BAUDRATE,
            .data_bits = UART_DATA_8_BITS,
            .parity = UART_PARITY_DISABLE,
            .stop_bits = UART_STOP_BITS_1,
            .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
            .rx_flow_ctrl_thresh = 0,
        },
    };

    /* initialise the uart drvier */
    int ret = uart_init(cfg->uart_num, uart_cfg);
    if (ret) {
        printf("%s: Failed to initialise the UART driver\n", TAG);
        return NULL;
    }

    ld2420[ld2420_count].uart_num = cfg->uart_num;
    ld2420[ld2420_count].ot_pin = cfg->ot_pin;
    ld2420_count++;
    return (void*)&ld2420[ld2420_count - 1]; 
}
