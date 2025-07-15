/*
 * SPDX-FileCopyrightText: 2025-2026 Espressif Systems (Shanghai) Co Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <stdio.h>
#include <uart.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @file occupancy_sensor_ld2420.h
 * @brief API for the LD2420 occupancy sensor.
 *
 * This file defines the interface for initializing and interacting with the LD2420
 * occupancy sensor over UART.
 */

/**
 * @brief Handle for LD2420 occupancy sensor.
 */
typedef void* occupancy_sensor_ld2420_handle_t;

/**
 * @brief Configuration structure for LD2420 occupancy sensor.
 */
typedef struct {
    uart_port_t uart_num;   /*!< UART port used to communicate with the sensor */
    int tx_pin;             /*!< UART TX pin */
    int rx_pin;             /*!< UART RX pin */
    int ot_pin;             /*!< Optional control pin for the sensor (OT pin) */
} occupancy_sensor_ld2420_cfg_t;

/**
 * @brief Data format returned in normal mode.
 */
typedef struct {
    uint8_t occupied;       /*!< 1 if motion is detected, 0 otherwise */
    uint16_t range;         /*!< Range to detected target (in cm) */
} occupancy_sensor_ld2420_normal_mode_data_t;

/**
 * @brief Data format returned in report mode.
 */
typedef struct {
    uint8_t occupied;               /*!< 1 if motion is detected, 0 otherwise */
    uint16_t target_distance;       /*!< Distance to the target (in cm) */
    uint16_t zone_noise_level[16];  /*!< Noise level reported for each of the 16 zones */
} occupancy_sensor_ld2420_report_mode_data_t;

/**
 * @brief Initialize LD2420 sensor.
 *
 * @param[in] cfg Pointer to sensor configuration structure.
 * @return Sensor handle on success, NULL on failure.
 */
occupancy_sensor_ld2420_handle_t occupancy_sensor_ld2420_init(occupancy_sensor_ld2420_cfg_t *cfg);

/**
 * @brief Get firmware version of the sensor.
 *
 * @param[in] handle Sensor handle.
 * @param[out] buffer Buffer to hold the version string.
 * @param[in] size Size of the buffer.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_get_firmware_version(occupancy_sensor_ld2420_handle_t handle, char *buffer, size_t size);

/**
 * @brief Set minimum detection distance.
 *
 * @param[in] handle Sensor handle.
 * @param[in] minimum_distance Minimum distance in cm.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_set_minimum_distance(occupancy_sensor_ld2420_handle_t handle, uint16_t minimum_distance);

/**
 * @brief Set maximum detection distance.
 *
 * @param[in] handle Sensor handle.
 * @param[in] maximum_distance Maximum distance in cm.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_set_maximum_distance(occupancy_sensor_ld2420_handle_t handle, uint16_t maximum_distance);

/**
 * @brief Set delay after which absence is reported.
 *
 * @param[in] handle Sensor handle.
 * @param[in] delay_s Delay in seconds.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_set_absence_report_delay(occupancy_sensor_ld2420_handle_t handle, uint16_t delay_s);

/**
 * @brief Set trigger threshold for a specific gate (zone).
 *
 * @param[in] handle Sensor handle.
 * @param[in] gate_index Index of the gate (0-15).
 * @param[in] threshold Trigger threshold.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_set_gate_trigger_threshold(occupancy_sensor_ld2420_handle_t handle, uint8_t gate_index, uint16_t threshold);

/**
 * @brief Set hold threshold for a specific gate (zone).
 *
 * @param[in] handle Sensor handle.
 * @param[in] gate_index Index of the gate (0-15).
 * @param[in] threshold Hold threshold.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_set_gate_hold_threshold(occupancy_sensor_ld2420_handle_t handle, uint8_t gate_index, uint16_t threshold);

/**
 * @brief Switch sensor to normal mode.
 *
 * In this mode, only basic presence and range information is provided.
 *
 * @param[in] handle Sensor handle.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_enter_normal_mode(occupancy_sensor_ld2420_handle_t handle);

/**
 * @brief Read data from sensor in normal mode.
 *
 * @param[in] handle Sensor handle.
 * @param[out] data Pointer to structure to receive data.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_read_normal_data(occupancy_sensor_ld2420_handle_t handle, occupancy_sensor_ld2420_normal_mode_data_t *data);

/**
 * @brief Switch sensor to report mode.
 *
 * In this mode, detailed target and noise zone information is available.
 *
 * @param[in] handle Sensor handle.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_enter_report_mode(occupancy_sensor_ld2420_handle_t handle);

/**
 * @brief Read data from sensor in report mode.
 *
 * @param[in] handle Sensor handle.
 * @param[out] data Pointer to structure to receive report data.
 * @return 0 on success, non-zero on failure.
 */
int occupancy_sensor_ld2420_read_report_data(occupancy_sensor_ld2420_handle_t handle, occupancy_sensor_ld2420_report_mode_data_t *data);

#ifdef __cplusplus
}
#endif
