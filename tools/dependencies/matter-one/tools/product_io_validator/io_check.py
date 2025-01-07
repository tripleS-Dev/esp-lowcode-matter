# Copyright 2022 Espressif Systems (Shanghai) PTE LTD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import argparse
import sys
from sys import exit

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

esp_device = None
esp_module = None
io_data = None
conf_io_pins = list()
conf_adc_pins = list()

def get_args():
    parser = argparse.ArgumentParser(description="IO validation for matter-one")
    parser.add_argument("--product_path", default="", type=str, help="Provide path for the product to validate")
    parser.add_argument("--output_path", default = "output", type = str, help="Provide output path for the product")
    args = vars(parser.parse_args())
    return args['product_path'], args['output_path']

def create_status_file(path, status='Success', description='Success', details = '', warnings = list()):
    with open(os.path.join(path, 'status.json'), 'w+') as info_file:
        status_info = {
            "status": status,
            "description": description,
            "details": details,
            "warnings": warnings    
        }
        json.dump(status_info, info_file, indent=4)

# NOTE: The suffixes mentioned below denote the flash size ,temperature rating and different certifications of the module which does not affect the pin mappings, hence these suffixes can be removed.
def remove_suffix(string):
    suffixes = ["-H2", "-H4", "-H8", "U-H2", "U-H4", "U-H8", "-N2", "-N4", "-N8", "U-N2", "U-N4", "U-N8", "H2", "H4", "H8", "N4", "N8", "H4X"]
    for suffix in suffixes:
        if string.endswith(suffix):
            return string[:-len(suffix)]
    return string

#  TODO: Add adc validation

def get_led_data(driver):
    details = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['gpio_config']['gpio_num'])
        for key in driver['gpio_config']:
            if ('_io' in key or 'gpio' in key) and key != 'gpio_num':
                details = f"Unexpected key '{key}' in gpio_config for LED driver "
                ret = False
    elif driver['name'] == 'ws2812':
        conf_io_pins.append(driver['ws2812_config']['ctrl_io'])
        for key in driver['ws2812_config']:
            if ('_io' in key or 'gpio' in key) and key != 'ctrl_io':
                details = f"Unexpected key '{key}' in ws2812_config for LED driver "
                ret = False
    elif driver['name'] == 'pwm':
        pwm_gpio_keys = ['gpio_red', 'gpio_green', 'gpio_blue', 'gpio_cold_or_cct', 'gpio_warm_or_brightness']
        for key in pwm_gpio_keys:
            if driver['pwm_config'][key] != -1:
                conf_io_pins.append(driver['pwm_config'][key])
        for key in driver['pwm_config']:
            if ('_io' in key or 'gpio' in key) and key not in pwm_gpio_keys:
                details = f"Unexpected key '{key}' in pwm_config for LED driver "
                ret = False
    elif driver['name'] in ['bp5758d', 'bp1658cj', 'sm2135e', 'sm2135eh', 'sm2235egh', 'sm2335egh', 'kp18058']:
        config_name = f"{driver['name']}_config"
        conf_io_pins.append(driver[config_name]['gpio_clock'])
        conf_io_pins.append(driver[config_name]['gpio_sda'])
        for key in driver[config_name]:
            if ('_io' in key or 'gpio' in key) and key not in ['gpio_clock', 'gpio_sda']:
                details = f"Unexpected key '{key}' in {config_name} for LED driver "
                ret = False
    else:
        details = f"Unknown LED driver name '{driver['name']}' "
        ret = False

    return ret, details

def get_button_data(driver):
    details = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['gpio_config']['gpio_num'])
        for key in driver['gpio_config']:
            if ('_io' in key or 'gpio' in key) and key != 'gpio_num':
                details = f"Unexpected key '{key}' in gpio_config for Button driver "
                ret = False
    elif driver['name'] == 'hosted':
        ret = True
    else:
        details = f"Unknown Button driver name '{driver['name']}' "
        ret = False

    return ret, details
    
def get_relay_data(driver):
    details = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['gpio_config']['gpio_num'])
        for key in driver['gpio_config']:
            if ('_io' in key or 'gpio' in key) and key != 'gpio_num':
                details = f"Unexpected key '{key}' in gpio_config for Relay driver "
                ret = False
    elif driver['name'] == 'hosted':
        ret = True
    else:
        details = f"Unknown Relay driver name '{driver['name']}' "
        ret = False
    return ret, details

def get_roller_blind_data(driver):
    details = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['gpio_config']['up_relay_gpio'])
        conf_io_pins.append(driver['gpio_config']['down_relay_gpio'])
        if driver['calibration_config']['calibration_type'] == 1:
            conf_io_pins.append(driver['calibration_config']['detect_gpio'])
        for key in driver['gpio_config']:
            if ('_io' in key or 'gpio' in key) and key not in ['up_relay_gpio', 'down_relay_gpio']:
                details = f"Unexpected key '{key}' in gpio_config for Roller Blind driver "
                return False, details
        for key in driver['calibration_config']:
            if ('_io' in key or 'gpio' in key) and key != 'detect_gpio':
                details = details + ", " + f"Unexpected key '{key}' in calibration_config for Roller Blind driver "
                ret = False
    elif driver['name'] == 'hosted':
        ret = True
    else:
        details = f"Unknown Roller Blind driver name '{driver['name']}' "
        ret = False
    return ret, details

def get_zero_detect_data(driver):
    details = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['capture_gpio_num'])
        for key in driver:
            if ('_io' in key or 'gpio' in key) and key != 'capture_gpio_num':
                details = f"Unexpected key '{key}' in Zero Detect driver "
                ret = False
    else:
        details = f"Unknown Zero Detect driver name '{driver['name']}' "
        ret = False
    return ret, details

def get_contact_sensor_data(driver):
    err_msg = ""
    ret = True
    if driver['name'] == 'gpio':
        conf_io_pins.append(driver['gpio_config']['gpio_num'])
        for key in driver['gpio_config']:
            if ('_io' in key or 'gpio' in key) and key != 'gpio_num':
                err_msg = f"Unexpected key '{key}' in gpio_config for Contact Sensor driver "
                print(f"Error: Unexpected key '{key}' in gpio_config for Contact Sensor driver")
                ret = False
    else:
        err_msg = f"Unknown Contact Sensor driver name '{driver['name']}' "
        print(f"Error: Unknown Contact Sensor driver name '{driver['name']}'")
        ret = False

    return ret, err_msg

# TODO: Add temp_sensor validation

def get_driver_data(drivers):
    details = ""
    ret = True
    for driver in drivers:
        if driver['type'] == 'ezc.driver.led':
            ret, details = get_led_data(driver)
        elif driver['type'] == 'ezc.driver.button':
            ret, details = get_button_data(driver)
        elif driver['type'] == 'ezc.driver.relay':
            ret, details = get_relay_data(driver)
        elif driver['type'] == 'ezc.driver.roller_blind':
            ret, details = get_roller_blind_data(driver)
        elif driver['type'] == 'ezc.driver.zero_detect':
            ret, details = get_zero_detect_data(driver)
        elif driver['type'] == 'ezc.driver.temp_sensor':
            ret = True
            err_msg = ""
        elif driver['type'] == 'ezc.driver.contact_sensor':
            ret, err_msg = get_contact_sensor_data(driver)
        else:
            details = f"Unknown driver type '{driver['type']}' "
            ret = False
        if not ret:
            return ret, details

    return ret, details

def get_io_data(data):
    ret = False
    esp_module_name = remove_suffix(esp_module)
    for j in range(len(data)):
        if esp_module_name == data[j]["id"]:
            ret = True
            global io_data
            io_data = data[j]
            break
    return ret
    
def verify_driver_data():
    details = ""
    warning_msg = list()
    io_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'io_data.json')
    if os.path.exists(io_data_file):
        io_data_file = open(io_data_file)
        data = json.loads(io_data_file.read())
        io_data_file.close()
    else:
        details = "IO data does not exist "
        return False, details, warning_msg

    ret = True

    for i in range(len(data["esp_device"])):
        if data["esp_device"][i]["id"] == esp_device:
            _ret = get_io_data(data["esp_device"][i]["list"])

    if not _ret:
        details = "ESP Module specified in product_info.json does not exist. "
        return False, details, warning_msg

    for item in conf_io_pins:
        if not item in io_data["gpio_pins"]:
            details = f"The IO pin {item} is not supported in the chip: {esp_device}, module:{esp_module}"
            return False, details, warning_msg
        if item in io_data["strapping_pins"]:
            warning_msg.append(f"The GPIO pin {item} is a strapping in the chip: {esp_device}, module: {esp_module}, this may cause unexpected bootup behavior")
        if "only_input_pins" in io_data and item in io_data["only_input_pins"]:
            warning_msg.append(f"The IO pin {item} is an only input pin in the chip {esp_device}, module:{esp_module}")

    for item in conf_adc_pins:
        if not item in io_data["adc_connections"]:
            details = f"The ADC pin {item} is not supported in the chip: {esp_device}, module:{esp_module} "
            return False, details, warning_msg
        if item in io_data["strapping_pins"]:
            warning_msg.append(f"The ADC pin {item} is a strapping in the chip: {esp_device}, module:{esp_module}")

    return ret, details, warning_msg

def config_io_check(product_path):
    warning_msg = list()
    product_info_path = str(os.path.join(product_path, 'product_info.json'))
    product_config_path = str(os.path.join(product_path, 'product_config.json'))

    if not os.path.exists(product_info_path):
        return False, "Failure", "Product PATH does not exist", warning_msg

    info_json_file = open(product_info_path)
    data = json.loads(info_json_file.read())
    info_json_file.close()
    global esp_device
    esp_device = data['chip']
    global esp_module
    esp_module = data['module']

    config_json_file = open(product_config_path)
    data = json.loads(config_json_file.read())
    config_json_file.close()
    ret, details = get_driver_data(data['driver'])
    if not ret:
        return False, "Failure", details, warning_msg

    ret, details, warning_msg = verify_driver_data()
    if not ret:
        return False, "Failure", details, warning_msg

    return True, "Success", details, warning_msg

if __name__ == '__main__':
    product_path, output_path = get_args()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ret, description, details, warning_msg = config_io_check(product_path)

    if not ret:
        create_status_file(output_path, 'Failure', 'IO validation Failed. Check details for more info', details, warning_msg)
        print(bcolors.FAIL + f"IO validation failed for the product: {product_path}" + bcolors.ENDC)
        print(bcolors.FAIL + f"Error Message: {details}" + bcolors.ENDC)
        print(bcolors.FAIL + f"Description: {description}" + bcolors.ENDC)
        if warning_msg:
            print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
        sys.exit(1)
    
    create_status_file(output_path, "Success", "Success", "", warning_msg)
    print(bcolors.OKGREEN + f"Successfully Validated IO for product: {product_path}" + bcolors.ENDC)
    if warning_msg:
        print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
