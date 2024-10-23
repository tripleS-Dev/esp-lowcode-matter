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
from io import StringIO
import sys
from sys import exit
import shutil

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

from output_file_creation import *

def add_matter_one_to_csv(path, no_signature, no_ota_decryption):
    with open(os.path.join(path, 'mfg_config.csv'), 'a') as info_file:
        info_file.write('matter_one,namespace,,')   # NOTE: Keeping this `matter_one` for backward compatibility
        info_file.write('\n')
        info_file.write('configuration,file,binary,' + str(os.path.join(path, 'configuration.info')))
        info_file.write('\n')
        if not no_signature:
            info_file.write('signature,file,binary,' + str(os.path.join(path, 'signature.info')))
            info_file.write('\n')
        if not no_ota_decryption:
            info_file.write('ota_decrypt_key,file,binary,' + str(os.path.join(path, 'ota_decrypt_key.pem')))
            info_file.write('\n')
        info_file.write('data_model,file,binary,' + str(os.path.join(path, 'data_model.bin')))
        info_file.write('\n')

def add_matter_one_to_output_csv(path, no_signature, no_ota_decryption):
    write_info_file_to_output_csv(path, 'configuration', 'configuration.info')
    if not no_signature:
        write_info_file_to_output_csv(path, 'verification_data', 'verification_data.txt')
        write_info_file_to_output_csv(path, 'signature', 'signature.info')
    if not no_ota_decryption:
        write_info_file_to_output_csv(path, 'ota_decrypt_key', 'ota_decrypt_key.pem')
    # write_info_file_to_output_csv(path, 'data_model', 'data_model.bin')

def get_configuration(path):
    configuration = None
    with open(os.path.join(path, 'configuration.info'), 'r') as file:
        configuration = file.read().replace('\n', '')
    return configuration

def create_verification_data_file(path, device_id, node_platform, port, test):
    configuration = get_configuration(path)
    with open(os.path.join(path, 'verification_data.txt'), 'w+') as info_file:
        info_file.write(device_id)
        info_file.write(configuration)

def get_signature(path, certs_path):
    with open(os.path.join(os.getcwd(), certs_path, 'software_licence_private_key.pem'), 'rb') as pem_in:
        pem_data = pem_in.read()
    private_key = load_pem_private_key(pem_data, None, default_backend())

    with open(os.path.join(path, 'verification_data.txt'), 'r') as data_in:
        verification_data = data_in.read()

    signature = private_key.sign(
        data=verification_data.encode('utf-8'),
        padding=padding.PKCS1v15(),
        algorithm=hashes.SHA256()
    )
    return signature.hex()

def create_signature_file(path, certs_path, device_id, node_platform, port, test):
    create_verification_data_file(path, device_id, node_platform, port, test)
    signature = get_signature(path, certs_path)
    with open(os.path.join(path, 'signature.info'), 'w+') as info_file:
        info_file.write(signature)

def temp_copy_files(path, products_path, certs_path, product, no_ota_decryption):
    product_path = os.path.join(os.getcwd(), products_path, product)
    print("Getting product_config json for: " + product)

    with open(os.path.join(product_path, 'product_config.json'), 'r') as info_file:
        lines = info_file.readlines()
    combined_lines = ""
    for line in lines:
        combined_lines += line.strip().replace(' ', '')
    with open(os.path.join(path, 'configuration.info'), 'w+') as info_file:
        info_file.writelines(combined_lines)

    if os.path.exists(os.path.join(product_path, 'device_manual.md')):
        shutil.copyfile(os.path.join(product_path, 'device_manual.md'), os.path.join(path, 'device_manual.md'))

    if os.path.exists(os.path.join(product_path, 'data_model.bin')):
        shutil.copyfile(os.path.join(product_path, 'data_model.bin'), os.path.join(path, 'data_model.bin'))

    if not no_ota_decryption:
        ota_decryption_key_name = os.path.join(os.getcwd(), certs_path, 'ota_decryption_private_key.pem')
        shutil.copyfile(ota_decryption_key_name, os.path.join(path, 'ota_decrypt_key.pem'))

def create_matter_one_files(path, products_path, certs_path, device_id, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert, no_signature, no_ota_decryption):
    temp_copy_files(path, products_path, certs_path, product, no_ota_decryption)
    if not no_signature:
        create_signature_file(path, certs_path, device_id, node_platform, port, test)
    print("Created Matter One files")
