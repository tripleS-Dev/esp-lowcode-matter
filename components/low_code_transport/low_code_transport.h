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

/**
 * @file low_code_transport.h
 * @brief Communication transport layer for data exchange between cores
 *
 * This component implements the transport layer for communication between the main core
 * and the LP core using RPMSG (Remote Processor Messaging) protocol. It handles data
 * serialization, transmission, and callback management.
 */

#pragma once

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Register transport layer callbacks
 *
 * This function registers the internal callback functions that will be called when data
 * is received from the other core.
 *
 * This needs to be called at the beginning. It is called in system_setup() by default.
 * @return int 0 on success, negative value on error
 */
int low_code_transport_register_callbacks(void);

#ifdef __cplusplus
}
#endif
