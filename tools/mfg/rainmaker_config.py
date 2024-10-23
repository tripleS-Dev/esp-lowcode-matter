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
from os import path
import sys
from sys import exit
import logging
import pyqrcode

from output_file_creation import *
from claim import gen_hex_str

def add_rainmaker_to_csv(path):
    with open(os.path.join(path, 'mfg_config.csv'), 'a') as info_file:
        info_file.write('rmaker_creds,namespace,,')
        info_file.write('\n')
        info_file.write('node_id,file,binary,' + os.path.join(path, 'node_id.info'))
        info_file.write('\n')
        info_file.write('mqtt_host,file,binary,' + os.path.join(path, 'mqtt_endpoint.info'))
        info_file.write('\n')
        info_file.write('http_host,file,binary,' + os.path.join(path, 'http_host.info'))
        info_file.write('\n')
        info_file.write('random,file,hex2bin,' + os.path.join(path, 'random.info'))
        info_file.write('\n')

def add_rainmaker_to_output_csv(path):
    write_info_file_to_output_csv(path, 'node_id', 'node_id.info')
    write_info_file_to_output_csv(path, 'mqtt_endpoint', 'mqtt_endpoint.info')
    write_info_file_to_output_csv(path, 'http_host', 'http_host.info')
    write_info_file_to_output_csv(path, 'random', 'random.info')
    write_info_file_to_output_csv(path, 'qr_code_url', 'qr_code_url.info')

def add_rainmaker_data_to_files(path, node_info, mqtt_endpoint, http_host, hex_str, qr_code, manual_code, no_matter, no_rainmaker):
    with open(os.path.join(path, 'node_id.info'), 'w+') as info_file:
        info_file.write(node_info)
    with open(os.path.join(path, 'mqtt_endpoint.info'), 'w+') as info_file:
        info_file.write(mqtt_endpoint)
    with open(os.path.join(path, 'http_host.info'), 'w+') as info_file:
        info_file.write(http_host)
    with open(os.path.join(path, 'random.info'), 'w+') as info_file:
        info_file.write(hex_str)

    if no_matter:
        with open(os.path.join(path, 'qr_code.info'), 'w+') as info_file:
            info_file.write(qr_code)
        with open(os.path.join(path, 'qr_code_url.info'), 'w+') as info_file:
            info_file.write('https://rainmaker.espressif.com/qrcode.html?data={}'.format(qr_code))
        with open(os.path.join(path, 'manual_code.info'), 'w+') as info_file:
            info_file.write(manual_code)

def get_rainmaker_setup_codes(node_platform, random):
    device_name_suffix = random[122:128]
    pop = random[0:8]
    if node_platform == "esp32" or node_platform == "esp32c3":
        transport = "ble"
    else:
        transport = "softap"

    qr_code = "{\"ver\":\"v1\",\"name\":\"PROV_" + device_name_suffix + "\",\"pop\":\"" + pop + "\",\"transport\":\"" + transport + "\"}"
    manual_code = pop

    print("QR code is: " + qr_code)
    print("Manual code is: " + manual_code)
    url = 'https://rainmaker.espressif.com/qrcode.html?data={}'.format(qr_code)
    print("QR code URL: " + url)
    return qr_code, manual_code

def qr_code_generate_image(qr_code, path):
    qr_code_payload = pyqrcode.create(qr_code)
    qr_code_payload.png(os.path.join(path, 'qr_code.png'), scale=6)

def create_rainmaker_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert):
    log = logging.getLogger("CLI_LOGS")
    log.setLevel(logging.ERROR)

    http_host = "api.node.zerocode.rainmaker.espressif.com"

    print("RainMaker node_id: " + node_id)
    print("RainMaker mqtt_endpoint: " + mqtt_endpoint)
    print("RainMaker http_host: " + http_host)

    hex_str = gen_hex_str()

    qr_code = None
    manual_code = None
    if no_matter:
        qr_code, manual_code = get_rainmaker_setup_codes(node_platform, hex_str)
        qr_code_generate_image(qr_code, path)

    add_rainmaker_data_to_files(path, node_id, mqtt_endpoint, http_host, hex_str, qr_code, manual_code, no_matter, no_rainmaker)
    print("Created Rainmaker files")
