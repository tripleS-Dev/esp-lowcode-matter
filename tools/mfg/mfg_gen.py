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
from pathlib import Path
import sys
from sys import exit
import esptool

from output_file_creation import *
from qr_code import *

if not os.getenv('REPOS_PATH'):
    os.environ['REPOS_PATH'] = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    print("Setting REPOS_PATH to " + os.getenv('REPOS_PATH'))

if (not os.getenv('IDF_PATH')) and os.getenv('REPOS_PATH'):
    if os.path.exists(os.path.join(os.getenv('REPOS_PATH'), 'esp-idf')):
        os.environ['IDF_PATH'] = os.path.join(os.getenv('REPOS_PATH'), 'esp-idf')
        print("Setting IDF_PATH to " + os.getenv('IDF_PATH'))

if (not os.getenv('ESP_RMAKER_PATH')) and os.getenv('REPOS_PATH'):
    if os.path.exists(os.path.join(os.getenv('REPOS_PATH'), 'esp-rainmaker')):
        os.environ['ESP_RMAKER_PATH'] = os.path.join(os.getenv('REPOS_PATH'), 'esp-rainmaker')
        print("Setting ESP_RMAKER_PATH to " + os.getenv('ESP_RMAKER_PATH'))

if (not os.getenv('ESP_SECURE_CERT_PATH')) and os.getenv('REPOS_PATH'):
    if os.path.exists(os.path.join(os.getenv('REPOS_PATH'), 'esp_secure_cert_mgr')):
        os.environ['ESP_SECURE_CERT_PATH'] = os.path.join(os.getenv('REPOS_PATH'), 'esp_secure_cert_mgr')
        print("Setting ESP_SECURE_CERT_PATH to " + os.getenv('ESP_SECURE_CERT_PATH'))

if (not os.getenv('MATTER_ONE_PATH')) and os.getenv('REPOS_PATH'):
    if os.path.exists(os.path.join(os.getenv('REPOS_PATH'), 'matter-one')):
        os.environ['MATTER_ONE_PATH'] = os.path.join(os.getenv('REPOS_PATH'), 'matter-one')
        print("Setting MATTER_ONE_PATH to " + os.getenv('MATTER_ONE_PATH'))

if os.getenv('IDF_PATH'):
    sys.path.insert(0, os.path.join(os.getenv('IDF_PATH'), 'components', 'nvs_flash', 'nvs_partition_generator'))
else:
    print("Please set the IDF_PATH environment variable.")
    exit(1)

if os.getenv('ESP_RMAKER_PATH'):
    sys.path.insert(0, os.path.join(os.getenv('ESP_RMAKER_PATH'), 'cli', 'rmaker_tools', 'rmaker_claim'))
    sys.path.insert(0, os.path.join(os.getenv('ESP_RMAKER_PATH'), 'cli', 'rmaker_cmd'))
    sys.path.insert(0, os.path.join(os.getenv('ESP_RMAKER_PATH'), 'cli', 'rmaker_lib'))
    sys.path.insert(0, os.path.join(os.getenv('ESP_RMAKER_PATH'), 'cli'))
else:
    print("Please set the ESP_RMAKER_PATH environment variable.")
    exit(1)

if os.getenv('ESP_SECURE_CERT_PATH'):
    sys.path.insert(0, os.path.join(os.getenv('ESP_SECURE_CERT_PATH'), 'tools'))
    sys.path.insert(0, os.path.join(os.getenv('ESP_SECURE_CERT_PATH'), 'tools', 'esp_secure_cert'))
else:
    print("Please set the ESP_SECURE_CERT_PATH environment variable.")
    exit(1)

if os.getenv('MATTER_ONE_PATH'):
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools'))
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools', 'qr_code_image_generator'))
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools', 'product_validator'))
else:
    print("Please set the MATTER_ONE_PATH environment variable.")
    exit(1)

from types import SimpleNamespace
import glob
import serial

import esp_idf_nvs_partition_gen.nvs_partition_gen as nvs_partition_gen
from esptool.cmds import detect_chip
from claim import get_node_mac
from claim import flash_nvs_partition_bin

from matter_one_config import *
from matter_config import *
from rainmaker_config import *
from rainmaker_claim import *
from product_validator import validate_product_data

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def run_io_validation(product_path):
    print("Running IO validation...")
    ret, err_msg, warning_msg = io_check.config_io_check(product_path)
    if ret:
        print("IO validation completed successfully.")
    else:
        print("IO validation failed")
    return ret

def get_product_info_solution_type(products_path, product):
    product_path = os.path.join(products_path, product)

    product_file = open(os.path.join(product_path, 'product_info.json'))
    product_json = json.load(product_file)
    product_file.close()

    if 'solution_type' in product_json:
        return product_json['solution_type']
    else:
        return 'zero_code'

def gen_nvs_partition_bin(filedir, output_bin_filename, output_encrypted_bin_filename, nvs_keys_bin_filename, no_unencrypted_fctry):
    if not no_unencrypted_fctry:
        nvs_args = SimpleNamespace(input=os.path.join(filedir, 'mfg_config.csv'), output=output_bin_filename, size='0x6000',
                                outdir=filedir, version=2)
        print("Generating NVS Partition Binary: " + os.path.join(filedir, output_bin_filename))
        nvs_partition_gen.generate(nvs_args)

    nvs_keys_args = SimpleNamespace(keyfile=nvs_keys_bin_filename, outdir=filedir, key_protect_hmac=False)
    print("Generating NVS Keys Binary: " + os.path.join(filedir, nvs_keys_bin_filename))
    nvs_partition_gen.generate_key(nvs_keys_args)
    os.rename(os.path.join(filedir, 'keys', nvs_keys_bin_filename), os.path.join(filedir, nvs_keys_bin_filename))
    shutil.rmtree(os.path.join(filedir, 'keys'))

    nvs_encrypted_args = SimpleNamespace(input=os.path.join(filedir, 'mfg_config.csv'),
                                         output=output_encrypted_bin_filename, size='0x6000', outdir=filedir,
                                         version=2, inputkey=os.path.join(filedir, nvs_keys_bin_filename),
                                         keygen=False, keyfile=None)
    print("Generating Encrypted NVS Partition Binary: " + os.path.join(filedir, output_encrypted_bin_filename))
    nvs_partition_gen.encrypt(nvs_encrypted_args)

def create_mfg_config_file(path, no_matter, no_rainmaker, no_signature, no_ota_decryption):
    with open(os.path.join(path, 'mfg_config.csv'), 'w+') as info_file:
        info_file.write('key,type,encoding,value')
        info_file.write('\n')

    add_matter_one_to_csv(path, no_signature, no_ota_decryption)
    if not no_matter:
        add_matter_to_csv(path)
    if not no_rainmaker:
        add_rainmaker_to_csv(path)

def create_config_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert, no_signature, no_ota_decryption):
    create_matter_one_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert, no_signature, no_ota_decryption)
    if not no_matter:
        create_matter_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert)
    if not no_rainmaker:
        create_rainmaker_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert)

def create_output_csv_file(path, mac_address, no_matter, no_rainmaker, no_signature, no_ota_decryption):
    with open(os.path.join(path, 'output.csv'), 'w+') as info_file:
        pass

    write_data_to_output_csv(path, 'mac_address', mac_address)
    write_info_file_to_output_csv(path, 'qr_code', 'qr_code.info')
    write_info_file_to_output_csv(path, 'manual_code', 'manual_code.info')
    if os.path.exists(os.path.join(path, 'device_cert.pem')):
        write_info_file_to_output_csv(path, 'device_cert', 'device_cert.pem')

    add_matter_one_to_output_csv(path, no_signature, no_ota_decryption)
    if not no_matter:
        add_matter_to_output_csv(path)
    if not no_rainmaker:
        add_rainmaker_to_output_csv(path)
    finish_output_csv(path)

def create_status_file(path, status='Success', description='Success', details = '', warnings = list()):
    with open(os.path.join(path, 'status.json'), 'w+') as info_file:
        status_info = {
            "status": status,
            "description": description,
            "details": details,
            "warnings": warnings
        }
        json.dump(status_info, info_file, indent=4)

def create_default_dir(mac_address, path):
    if path == None:
        path = str(os.path.join('devices', mac_address))
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def detect_chip_and_mac(port):
    if not port:
        print("Port does not exist")
        sys.exit(1)

    command = ['--port', port, 'chip_id']

    try:
        sys.stdout = mystdout = StringIO()
        esptool.main(command)
        sys.stdout = sys.__stdout__

    except esptool.FatalError:
        sys.stdout = sys.__stdout__
        print(sys.stdout)
        sys.exit(1)

    # Finds the first occurence of the line
    # with the MAC Address from the output.
    mac = next(filter(lambda line: 'MAC: ' in line,
                      mystdout.getvalue().splitlines()))
    chip = next(filter(lambda line: 'Detecting chip type... ' in line,
                      mystdout.getvalue().splitlines()))
    chip_name = chip.split('Detecting chip type... ')[1].replace('-', '').replace(' ', '').lower()
    mac_addr = mac.split('MAC: ')[1].replace(':', '').upper()
    print("MAC address: " + mac_addr)
    print("Chip detected: "+ chip_name)
    return mac_addr, chip_name

def get_connected_device_details(port, mac_address, node_platform, test):
    if test == False:
        print("Getting connected device details")
        if port == None:
            port = get_serial_port()
            if port is None:
                print("Connect your device")
                exit(1)
        else:
            print("Port provided is: " + port)
        if node_platform == None or mac_address == None:
            mac_address, node_platform = detect_chip_and_mac(port=port)
        mac_address = mac_address.upper().replace(' ', '').replace('-', '').replace(':', '')
    else:
        print("Getting test details")
        port = None
        node_platform = "esp32c3"
        mac_address = "0123456789AB"

    print("Chip is: " + node_platform)
    print("Mac is: " + mac_address)
    return port, mac_address, node_platform

def get_serial_port():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.usbserial*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            print("Port detected is: " + port)
            return port
        except (OSError, serial.SerialException):
            pass
    return None

def get_args():
    parser = argparse.ArgumentParser(description='Manufacturing partition generator tool for Matter One')

    parser.add_argument("--product", default='esp32c3_socket', type=str, help='Product to get the customer specific details. If not set, \'esp32c3_socket\' is used.')
    parser.add_argument('--test', action='store_true', help="Create the mfg binary for a test device. The generated binary will not work with any device.")
    parser.add_argument('--no_qrcode', action='store_true', help="Do not open the qrcode image.")
    parser.add_argument('--no_flash', action='store_true', help="Do not flash the binary.")
    parser.add_argument('--no_unencrypted_fctry', action='store_true', help="Do not generate the unencrypted fctry partition.")
    parser.add_argument('--port', default=None, type=str, help="Port if not detected automatically.")
    parser.add_argument('--mac_address', default=None, type=str, help="MAC address not detected automatically.")
    parser.add_argument('--no_claim_details', default=None, type=str, help="CN that is set in the certificate, if the device certificates are already generated.")
    parser.add_argument('--mqtt_endpoint', default=None, type=str, help="MQTT endpoint for RainMaker. If claim is performed, this is ignored. If nothing is passed, ZeroCode default is used.")
    parser.add_argument('--serial_number', default=None, type=str, help="Provide the serial_number for the device. If not set, a serial number from the auto generated uuid is used (the same one which is set as the CN in the device cert). Max length is 32 characters.")
    parser.add_argument('--device_cert_path', default=None, type=str, help="Provide the device_cert path in PEM format. If not \'no_claim_details\' is selected, and this is not set, the device_cert will not be a part of the output. ")
    parser.add_argument("--node_platform", choices=['esp32c3', 'esp32c2', 'esp32s3', 'esp32h2'], type=str, help='Platform if not detected automatically')
    parser.add_argument('--not_connected_device_details', nargs=2, help="Provide the details for a device which is not conected. Pass the node_platform and the mac_address in this order.")
    parser.add_argument('--products_path', default="products", type=str, help="Provide the path to all the products. If not set, \'products\' is used.")
    parser.add_argument('--certs_path', default="certs", type=str, help="Provide the path to common certs files. If not set, \'products\' is used.")
    parser.add_argument('--output_path', default=None, type=str, help="Provide the path to store all device-related pre-programming output files. If not set, \'products\' is used.")
    parser.add_argument('--no_matter', default=False, action='store_true', help="Don't add Matter")
    parser.add_argument('--no_rainmaker', default=False, action='store_true', help="Don't add RainMaker")
    parser.add_argument('--local_claim', default=False, action='store_true', help="Claim the device locally instead of using RainMaker")
    parser.add_argument("--deployment", default='ezc_prod', choices=['ezc_prod', 'ezc_stage', 'ezc_dev'], type=str, help='ZeroCode deployment for staging and dev. If nothing is provided `ezc_prod` is used.')
    parser.add_argument("--no_config_validation", default=False, action='store_true', help="Don't validate product config json file.")
    parser.add_argument("--no_info_validation", default=False, action='store_true', help="Don't validate product info json file.")
    parser.add_argument("--no_io_validation", default=False, action='store_true', help="Don't validate io of product_config.json file.")
    parser.add_argument("--not_save_cd_cert", default=False, action='store_true', help="Don't save cd_cert file if created")
    parser.add_argument('--no_signature', default=False, action='store_true', help="Do not create the signature file.")
    parser.add_argument('--no_ota_decryption', default=False, action='store_true', help="Do not include the OTA decryption key.")

    args = parser.parse_args()

    supported_products = []
    supported_products_path = os.path.join(os.getcwd(), args.products_path)
    for product_name in os.listdir(supported_products_path):
        supported_products.append(product_name)

    if args.product not in supported_products:
        print("Product " + args.product + " not found in " + supported_products_path)
        print("Available choices: " + str(supported_products))
        exit(1)

    if args.not_connected_device_details != None:
        node_platform = args.not_connected_device_details[0]
        mac_address = args.not_connected_device_details[1]
        port = 'no_port'
        no_flash = True
    else:
        mac_address = args.mac_address
        node_platform = args.node_platform
        port = args.port
        no_flash = args.no_flash

    if args.no_unencrypted_fctry:
        no_flash = True

    if args.no_claim_details != None:
        claim = False
        node_id = args.no_claim_details
        if args.mqtt_endpoint != None:
            mqtt_endpoint = args.mqtt_endpoint
        else:
            mqtt_endpoint = "a1bgzo5c3ypi5s-ats.iot.us-east-1.amazonaws.com"
    else:
        claim = True
        node_id = None
        mqtt_endpoint = None
    return args.product, args.test, args.no_qrcode, no_flash, args.no_unencrypted_fctry, port, mac_address, node_platform, claim, node_id, mqtt_endpoint, args.serial_number, args.device_cert_path, args.products_path, args.certs_path, args.output_path, args.no_matter, args.no_rainmaker, args.local_claim, args.deployment, args.no_config_validation, args.no_info_validation, args.no_io_validation, args.not_save_cd_cert, args.no_signature, args.no_ota_decryption

def main():
    product, test, no_qrcode, no_flash, no_unencrypted_fctry, port, mac_address, node_platform, claim, node_id, mqtt_endpoint, serial_number, device_cert_path, products_path, certs_path, output_path, no_matter, no_rainmaker, local_claim, deployment, no_config_validation, no_info_validation, no_io_validation, not_save_cd_cert, no_signature, no_ota_decryption = get_args()

    if not no_config_validation:
        solution_type = get_product_info_solution_type(products_path, product)
        is_low_code = False
        if solution_type == "low_code":
            is_low_code = True

    port, mac_address, node_platform = get_connected_device_details(port, mac_address, node_platform, test)
    path = create_default_dir(mac_address, output_path)
    product_path = os.path.join(products_path, product)

    if not no_config_validation or not no_info_validation or not no_io_validation:
        ret, description, details, warning_msg = validate_product_data(product_path, None, no_config_validation, no_info_validation, no_io_validation, is_low_code)
        if not ret:
            create_status_file(path, "Failure", description, details, warning_msg)
            print(bcolors.FAIL + f"Failed to verify product data: {description}" + bcolors.ENDC)
            print(bcolors.FAIL + f"Error message: {json.dumps(details, indent=4)}" + bcolors.ENDC)
            if warning_msg:
                print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
            exit(1)
        else:
            print(bcolors.OKGREEN + f"Successfully Validated product data" + bcolors.ENDC)
            if warning_msg:
                print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + f"Skipping product data validation" + bcolors.ENDC)

    esp_secure_cert_file_name = mac_address + '_esp_secure_cert.bin'
    esp_secure_cert_flash_address = '0xD000'
    fctry_partition_file_name = mac_address + '_fctry.bin'
    fctry_partition_flash_address = '0x1F2000'
    fctry_partition_encrypted_file_name = mac_address + '_encrypted_fctry.bin'
    nvs_keys_partition_file_name = mac_address + '_nvs_keys.bin'

    if claim:
        if local_claim:
            node_id, mqtt_endpoint = local_claim_for_matter(path, mac_address, node_platform, products_path, product, certs_path, esp_secure_cert_file_name, no_matter, no_rainmaker, deployment)
        else:
            node_id, mqtt_endpoint = rainmaker_claim_for_matter(path, mac_address, node_platform, products_path, product, certs_path, esp_secure_cert_file_name, no_matter, no_rainmaker, deployment)
    else:
        add_device_cert_to_files(path, device_cert_path)

    create_mfg_config_file(path, no_matter, no_rainmaker, no_signature, no_ota_decryption)
    create_config_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert, no_signature, no_ota_decryption)
    create_output_csv_file(path, mac_address, no_matter, no_rainmaker, no_signature, no_ota_decryption)

    gen_nvs_partition_bin(path, fctry_partition_file_name, fctry_partition_encrypted_file_name, nvs_keys_partition_file_name, no_unencrypted_fctry)

    if test == False and no_flash == False:
        if claim:
            flash_nvs_partition_bin(port, os.path.join(path, esp_secure_cert_file_name), esp_secure_cert_flash_address)
        flash_nvs_partition_bin(port, os.path.join(path, fctry_partition_file_name), fctry_partition_flash_address)
        if no_qrcode == False:
            with open(os.path.join(path, 'qr_code_url.info'), 'r') as info_file:
                display_qrcode_web(info_file.read())
    else:
        print("Not flashing since test mfg was created or no_flash or no_unencrypted_fctry was set")

    create_status_file(path, "Success", "Successfully created files", "", warning_msg)

if __name__ == '__main__':
    main()
