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

#pragma once

#include <stdio.h>
#include <cstdint>

// TODO: Remove this error list from here and create low_code_utils which has all the standard error
/* Definitions for error constants. */
#define ESP_OK          0       /*!< esp_err_t value indicating success (no error) */
#define ESP_FAIL        -1      /*!< Generic esp_err_t code indicating failure */

#define ESP_ERR_NO_MEM              0x101   /*!< Out of memory */
#define ESP_ERR_INVALID_ARG         0x102   /*!< Invalid argument */
#define ESP_ERR_INVALID_STATE       0x103   /*!< Invalid state */
#define ESP_ERR_INVALID_SIZE        0x104   /*!< Invalid size */
#define ESP_ERR_NOT_FOUND           0x105   /*!< Requested resource not found */
#define ESP_ERR_NOT_SUPPORTED       0x106   /*!< Operation or feature not supported */
#define ESP_ERR_TIMEOUT             0x107   /*!< Operation timed out */
#define ESP_ERR_INVALID_RESPONSE    0x108   /*!< Received response was invalid */
#define ESP_ERR_INVALID_CRC         0x109   /*!< CRC or checksum was invalid */
#define ESP_ERR_INVALID_VERSION     0x10A   /*!< Version was invalid */
#define ESP_ERR_INVALID_MAC         0x10B   /*!< MAC address was invalid */
#define ESP_ERR_NOT_FINISHED        0x10C   /*!< Operation has not fully completed */
#define ESP_ERR_NOT_ALLOWED         0x10D   /*!< Operation is not allowed */


#define ESP_ERR_WIFI_BASE           0x3000  /*!< Starting number of WiFi error codes */
#define ESP_ERR_MESH_BASE           0x4000  /*!< Starting number of MESH error codes */
#define ESP_ERR_FLASH_BASE          0x6000  /*!< Starting number of flash error codes */
#define ESP_ERR_HW_CRYPTO_BASE      0xc000  /*!< Starting number of HW cryptography module error codes */
#define ESP_ERR_MEMPROT_BASE        0xd000  /*!< Starting number of Memory Protection API error codes */


typedef enum {
    DEVICE_FEATURES_VALUE_TYPE_INVALID = 0,
    DEVICE_FEATURES_VALUE_TYPE_BOOLEAN,
    DEVICE_FEATURES_VALUE_TYPE_INTEGER,
    DEVICE_FEATURES_VALUE_TYPE_UNSIGNED_INTEGER,
    DEVICE_FEATURES_VALUE_TYPE_FLOAT,
    DEVICE_FEATURES_VALUE_TYPE_UINT8,
    DEVICE_FEATURES_VALUE_TYPE_INT16,
    DEVICE_FEATURES_VALUE_TYPE_UINT16,
    DEVICE_FEATURES_VALUE_TYPE_STRING,
    DEVICE_FEATURES_VALUE_TYPE_OCTET_STRING,
    DEVICE_FEATURES_VALUE_TYPE_ARRAY,
    DEVICE_FEATURES_VALUE_TYPE_CUSTOM,
} device_feature_value_type_t;

typedef struct device_feature_value {
    device_feature_value_type_t type;
    int value_len;
    uint8_t *value;
} device_feature_value_t;

typedef struct device_feature_details {
    /** Transport layer should not use these */
    uint8_t type;
    uint16_t endpoint_id;
    uint32_t cluster_id;
    uint32_t attribute_id;
    uint32_t command_id;
} device_feature_details_t;

typedef struct device_feature_data {
    device_feature_details_t details;
    device_feature_value_t value;
    void *priv_data;
} device_feature_data_t;

typedef enum {
    DEVICE_FEATURES_EVENT_INVALID = 0,
    DEVICE_FEATURES_EVENT_SETUP_MODE_START,
    DEVICE_FEATURES_EVENT_SETUP_MODE_END,
    DEVICE_FEATURES_EVENT_SETUP_DEVICE_CONNECTED,
    DEVICE_FEATURES_EVENT_SETUP_STARTED,
    DEVICE_FEATURES_EVENT_SETUP_SUCCESSFUL,
    DEVICE_FEATURES_EVENT_SETUP_FAILED,
    DEVICE_FEATURES_EVENT_NETWORK_CONNECTED,
    DEVICE_FEATURES_EVENT_NETWORK_DISCONNECTED,
    DEVICE_FEATURES_EVENT_OTA_STARTED,
    DEVICE_FEATURES_EVENT_OTA_STOPPED,
    DEVICE_FEATURES_EVENT_READY,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_START,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_STOP,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_BLINK,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_BREATHE,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_OKAY,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_CHANNEL_CHANGE,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_FINISH_EFFECT,
    DEVICE_FEATURES_EVENT_IDENTIFICATION_STOP_EFFECT,
    DEVICE_FEATURES_EVENT_TEST_MODE_LOW_CODE,
    DEVICE_FEATURES_EVENT_TEST_MODE_COMMON,
    DEVICE_FEATURES_EVENT_TEST_MODE_BLE,
    DEVICE_FEATURES_EVENT_TEST_MODE_SNIFFER,
    DEVICE_FEATURES_EVENT_FACTORY_RESET,
    DEVICE_FEATURES_EVENT_FORCED_ROLLBACK,
    DEVICE_FEATURES_EVENT_BLE_ADVERTISE,
} device_feature_event_type_t;

typedef struct device_feature_event {
    device_feature_event_type_t event_type;
    int event_data_size;
    void *event_data;
} device_feature_event_t;

// TODO: Put this struct and func prototype def in another suitable file so that
// it is not exposed to the customer
typedef int (*device_feature_send_event_t)(device_feature_event_t *event);
typedef int (*device_feature_feature_update_t)(device_feature_data_t *data);

typedef int (*device_feature_get_event_t)();
typedef int (*device_feature_get_feature_t)();

typedef struct device_feature_callback_list {
    device_feature_send_event_t send_event_cb;
    device_feature_feature_update_t send_update_cb;
    device_feature_get_event_t get_event;
    device_feature_get_feature_t get_feature;
} __attribute__((packed)) device_feature_callback_list_t;

int device_feature_transport_register_callback(device_feature_callback_list_t *callbacks);
int device_feature_low_code_register_callback(device_feature_feature_update_t send_update_cb, device_feature_send_event_t send_event_cb);

int device_features_external_to_internal_feature_update(device_feature_data_t *device_feature);
int device_features_external_from_internal_feature_update(device_feature_data_t *data);
int device_features_external_to_internal_event_update(device_feature_event_t *event);
int device_features_external_from_internal_event_update(device_feature_event_t *event);

int device_feature_get_event();
int device_feature_get_feature();


