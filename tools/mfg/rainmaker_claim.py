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

import json
import os
from os import path
import sys
from sys import exit
import logging
import shutil
import uuid

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

from matter_config import get_product_info_details

from rmaker_tools.rmaker_claim.claim_config import claim_config_set_base_url
from claim import set_claim_initiate_data, claim_initiate
from claim import generate_private_key, generate_private_ecc_key
from claim import gen_host_csr, claim_verify
from claim import get_mqtt_endpoint

from local_claim import local_dac_gen
from tlv_format import *

from utils import convert_x509_cert_from_pem_to_der

def convert_private_key_from_pem_to_der(pem_file, out_der_file):
    with open(pem_file, 'rb') as f:
        pem_data = f.read()

    pem_key = load_pem_private_key(pem_data, None, default_backend())

    der_key = pem_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    with open(out_der_file, 'wb') as f:
        f.write(der_key)

def split_device_cert(device_cert: str) -> tuple:
    """
    In case of matter claiming, claim_verify API returns device_cert and ca_cert in one string
    This function splits them separate

    :param device_cert: device_cert and ca_cert strings concatenated back-to-back
    :type device_cert: str

    :return: device_cert and ca_cert
    :rtype: tuple[str, str]
    """
    indices = [index for index in range(len(device_cert)) if device_cert[index:].startswith("-----BEGIN CERTIFICATE-----")]
    if len(indices) > 1:
        split_device_cert = device_cert[:indices[1]]
        split_ca_cert = device_cert[indices[1]:]
    else:
        split_device_cert = device_cert
        split_ca_cert = ""
    return split_device_cert, split_ca_cert

def set_claim_deployment_url(deployment):
    base_url = "https://esp-claiming.rainmaker.espressif.com/"
    if deployment == 'ezc_prod':
        base_url = "https://esp-claiming.rainmaker.espressif.com/"
    elif deployment == 'ezc_stage':
        base_url = "https://ptmbyy1yyj.execute-api.us-east-1.amazonaws.com/staging/"
    elif deployment == 'ezc_dev':
        base_url = "https://fdpzpm7a6a.execute-api.us-east-1.amazonaws.com/dev/"

    claim_config_set_base_url(base_url)

def get_device_id(mac_address, node_platform):
    # Perform claim initiate request
    claim_init_resp = claim_initiate(set_claim_initiate_data(mac_address, node_platform))
    device_id = str(json.loads(claim_init_resp.text)['node_id'])
    return device_id

def generate_private_key_and_csr(products_path, product, device_id, no_matter, no_rainmaker):
    # Generate Private Key on host
    if no_matter:
        private_key, private_key_bytes = generate_private_key()
        subjectPairs={}
    else:
        private_key, private_key_bytes = generate_private_ecc_key()
        # Get Origin VID, PID
        _, _, cert_vendor_id, cert_product_id, _, _, _, _, _  = get_product_info_details(products_path, product)
        # Generate CSR
        # CHIP OID for vendor id
        VENDOR_ID = '1.3.6.1.4.1.37244.2.1'
        # CHIP OID for product id
        PRODUCT_ID = '1.3.6.1.4.1.37244.2.2'
        subjectPairs={
            VENDOR_ID:hex(cert_vendor_id)[2:].upper().zfill(4),
            PRODUCT_ID:hex(cert_product_id)[2:].upper().zfill(4)
        }
    csr = gen_host_csr(private_key, common_name=device_id, subjectPairs=subjectPairs)
    if not csr:
        raise Exception("CSR Not Generated. Claiming Failed")
    return private_key_bytes, csr

def get_device_cert_and_ca_cert_rainmaker(csr, certs_path, no_matter, no_rainmaker):
    # Getting the CSR signed by claiming service
    print("Attempting to claim device: RainMaker")
    # Perform claim verify request
    claim_verify_resp = claim_verify(claim_verify_data={"csr": csr}, matter=(not no_matter))
    # Get certificate from claim verify response
    cert_resp = json.loads(claim_verify_resp.text)['certificate']
    device_cert, ca_cert = split_device_cert(cert_resp)
    return device_cert, ca_cert

def get_device_cert_and_ca_cert_local(csr, certs_path, no_matter, no_rainmaker):
    print("Attempting to claim device: Local")
    device_cert, ca_cert = local_dac_gen(csr, certs_path)
    return device_cert, ca_cert

def add_claim_data_to_files(path, device_cert, device_key, ca_cert):
    with open(os.path.join(path, 'device_cert.pem'), 'w+') as info_file:
        info_file.write(device_cert)
    with open(os.path.join(path, 'device_key.pem'), 'wb+') as info_file:
        info_file.write(device_key)
    with open(os.path.join(path, 'ca_cert.pem'), 'w+') as info_file:
        info_file.write(ca_cert)

    convert_x509_cert_from_pem_to_der(os.path.join(path, 'device_cert.pem'), os.path.join(path, 'device_cert.der'))
    convert_private_key_from_pem_to_der(os.path.join(path, 'device_key.pem'), os.path.join(path, 'device_key.der'))
    convert_x509_cert_from_pem_to_der(os.path.join(path, 'ca_cert.pem'), os.path.join(path, 'ca_cert.der'))

def add_device_cert_to_files(path, device_cert_path):
    if device_cert_path:
        shutil.copyfile(device_cert_path, os.path.join(path, 'device_cert.pem'))
    else:
        print("Not adding device cert")

def gen_esp_secure_cert_partition_bin(path, esp_secure_cert_file_name, node_platform):
    tlv_priv_key = tlv_priv_key_t(tlv_priv_key_type_t.ESP_SECURE_CERT_DEFAULT_FORMAT_KEY, os.path.join(path, 'device_key.der'), None)
    generate_partition_no_ds(tlv_priv_key, os.path.join(path, 'device_cert.der'), os.path.join(path, 'ca_cert.der'), node_platform, os.path.join(path, esp_secure_cert_file_name))

def claim_create_files(path, device_cert, device_key, ca_cert, esp_secure_cert_file_name, node_platform):
    add_claim_data_to_files(path, device_cert, device_key, ca_cert)
    gen_esp_secure_cert_partition_bin(path, esp_secure_cert_file_name, node_platform)
    print("Generated esp_secure_cert partition: " + str(os.path.join(path, esp_secure_cert_file_name)))

def rainmaker_claim_for_matter(path, mac_address, node_platform, products_path, product, certs_path, esp_secure_cert_file_name, no_matter, no_rainmaker, deployment):
    print("Starting certificate claiming")
    set_claim_deployment_url(deployment)
    device_id = get_device_id(mac_address, node_platform)
    device_key, csr = generate_private_key_and_csr(products_path, product, device_id, no_matter, no_rainmaker)
    device_cert, ca_cert = get_device_cert_and_ca_cert_rainmaker(csr, certs_path, no_matter, no_rainmaker)
    mqtt_endpoint = get_mqtt_endpoint()

    claim_create_files(path, device_cert, device_key, ca_cert, esp_secure_cert_file_name, node_platform)
    return device_id, mqtt_endpoint

def local_claim_for_matter(path, mac_address, node_platform, products_path, product, certs_path,  esp_secure_cert_file_name, no_matter, no_rainmaker, deployment):
    print("Starting local certificate claiming")

    device_id = str(uuid.uuid4())
    device_key, csr = generate_private_key_and_csr(products_path, product, device_id, no_matter, no_rainmaker)
    device_cert, ca_cert = get_device_cert_and_ca_cert_local(csr, certs_path, no_matter, no_rainmaker)
    mqtt_endpoint = ""

    claim_create_files(path, device_cert, device_key, ca_cert, esp_secure_cert_file_name, node_platform)
    return device_id, mqtt_endpoint
