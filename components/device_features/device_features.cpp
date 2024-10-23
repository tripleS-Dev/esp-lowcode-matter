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

#include <string.h>

#include <device_features.h>

static const char *TAG = "device_features";

// callbacks to send from external to internal
static device_feature_send_event_t external_send_event_cb = NULL;
static device_feature_feature_update_t external_send_update_cb = NULL;
static device_feature_feature_update_t low_code_feature_update_cb = NULL;
static device_feature_send_event_t low_code_send_event_cb = NULL;

device_feature_get_event_t get_event_external_from_internal = NULL;
device_feature_get_feature_t get_feature_external_from_internal = NULL;

int device_features_external_from_internal_event_update(device_feature_event_t *event)
{
    if (!event) {
        printf("%s: Device features event cannot be null\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }

    if (low_code_send_event_cb) {
        low_code_send_event_cb(event);
    }
    return ESP_OK;
}

int device_features_external_to_internal_event_update(device_feature_event_t *event)
{
    if (external_send_event_cb) {
        return external_send_event_cb(event);
    }
    return ESP_OK;
}

int device_features_external_from_internal_feature_update(device_feature_data_t *data)
{
    // TODO: Call customer prototype function here
    if (!data) {
        printf("%s: Device features data cannot be null\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }

    if (low_code_feature_update_cb) {
        low_code_feature_update_cb(data);
    }
    return ESP_OK;
}

int device_features_external_to_internal_feature_update(device_feature_data_t *device_feature)
{
    if (external_send_update_cb) {
        external_send_update_cb(device_feature);
    }
    return ESP_OK;
}

int device_feature_transport_register_callback(device_feature_callback_list_t *callbacks)
{
    if (!callbacks) {
        printf("%s: Device features callback list cannot be null\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }
    if (!callbacks->send_event_cb || !callbacks->send_update_cb) {
        printf("%s: Device features callback cannot be null\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }

    if (external_send_event_cb || external_send_update_cb) {
        printf("%s: Device features external callback already registered\n", TAG);
        return ESP_ERR_INVALID_STATE;
    }

    external_send_event_cb = callbacks->send_event_cb;
    external_send_update_cb = callbacks->send_update_cb;
    get_event_external_from_internal  = callbacks->get_event;
    get_feature_external_from_internal = callbacks->get_feature;

    return ESP_OK;
}

int device_feature_get_event()
{
    if (get_event_external_from_internal) {
        return get_event_external_from_internal();
    }
    return ESP_FAIL;
}

int device_feature_get_feature()
{
    if (get_feature_external_from_internal) {
        return get_feature_external_from_internal();
    }
    return ESP_FAIL;
}

int device_feature_low_code_register_callback(device_feature_feature_update_t feature_update_cb, device_feature_send_event_t send_event_cb)
{
    if (!feature_update_cb || !send_event_cb) {
        printf("%s: feature_update_cb or send_event_cb cannot be null\n", TAG);
        return ESP_ERR_INVALID_ARG;
    }

    if (low_code_send_event_cb || low_code_feature_update_cb) {
        printf("%s: Device features external callback already registered\n", TAG);
        return ESP_ERR_INVALID_STATE;
    }

    low_code_send_event_cb = send_event_cb;
    low_code_feature_update_cb = feature_update_cb;

    return ESP_OK;
}
