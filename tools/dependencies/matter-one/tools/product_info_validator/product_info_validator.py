# coding=utf-8
import argparse
import os
import sys
import time
import json
import subprocess
import shutil

from pydantic import BaseModel, StrictInt, StrictStr, field_validator, model_validator, ValidationError
from typing import Literal, Optional

from pid_info_get import get_pid_details

if not os.getenv('REPOS_PATH'):
    os.environ['REPOS_PATH'] = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    print("Setting REPOS_PATH to " + os.getenv('REPOS_PATH'))

if (not os.getenv('MATTER_ONE_PATH')) and os.getenv('REPOS_PATH'):
    if os.path.exists(os.path.join(os.getenv('REPOS_PATH'), 'matter-one')):
        os.environ['MATTER_ONE_PATH'] = os.path.join(os.getenv('REPOS_PATH'), 'matter-one')
        print("Setting MATTER_ONE_PATH to " + os.getenv('MATTER_ONE_PATH'))

if os.getenv('MATTER_ONE_PATH'):
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools'))
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools', 'product_config_validator'))
else:
    print("Please set the MATTER_ONE_PATH environment variable.")
    exit(1)

from data_handler.error_handling import error_handling

espressif_vid = 4891
cert_id = None
pid = None
vid = None
device_type_id = None
origin_vid = None
origin_pid = None

targets_connection_type = {
    "wifi": ["esp32c2", "esp32c3", "esp32c6", "esp32", "esp32s3"],
    "thread": ["esp32h2", "esp32c6"]
}

def create_status_file(path, status='Success', description='Success', details='', warning_msg=''):
    with open(os.path.join(path, 'status.json'), 'w+') as info_file:
        status_info = {
            "status": status,
            "description": description,
            "details": details,
            "warning_msg": warning_msg
        }
        json.dump(status_info, info_file, indent=4)

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class ProductInfo(BaseModel,extra='forbid'):
    config_version: Literal[3]
    vendor_id: StrictInt
    product_id: StrictInt
    origin_vendor_id: Optional[Literal[espressif_vid]] = None
    origin_product_id: Optional[StrictInt] = None
    # TODO: device_type_id should be verified against the cd_cert
    device_type_id: StrictInt
    vendor_name: StrictStr
    product_name: StrictStr
    hw_ver: StrictInt
    hw_ver_str: StrictStr
    chip: Literal["esp32", "esp32c3", "esp32c2", "esp32h2", "esp32c6", "esp32s3"]
    connection_type: Literal["wifi", "thread"]
    module: StrictStr
    flash_size: Literal["2MB", "4MB"]
    secure_boot: Literal["enabled", "disabled"]
    product_type: Literal["socket", "light", "window_covering", "switch", "all", "hosted", "contact_sensor", "temperature_sensor", "occupancy_sensor"]
    solution_type: Optional[Literal["low_code", "zero_code"]] = None

    @model_validator(mode='after')
    def check_connection_size(self) -> 'ProductInfo':
        if self.connection_type not in targets_connection_type.keys():
            raise ValueError("connection_type is invalid")
        if self.chip not in targets_connection_type[self.connection_type]:
            raise ValueError("{} does not support the connection_type: {}".format(self.chip, self.connection_type))
        return self

    @model_validator(mode='after')
    def check_flash_size(self) -> 'ProductInfo':
        if self.flash_size == "2MB" and self.chip != "esp32c2":
            raise ValueError("Only esp32c2 chip supports 2MB flash size")
        return self

    @model_validator(mode='after')
    def check_secure_boot(self) -> 'ProductInfo':
        if self.secure_boot == "disabled" and self.product_type != "light":
            raise ValueError("Disabling secure boot is only allowed for `light` product type")
        return self

    @model_validator(mode='after')
    def check_vid(self) -> 'ProductInfo':
        global vid
        if (self.vendor_id == self.origin_vendor_id and self.vendor_id != espressif_vid) or (self.vendor_id != vid):
            raise ValueError("Vendor ID of product_info.json does not match with the cd_cert")
        elif self.origin_vendor_id != None and self.origin_vendor_id != espressif_vid:
            raise ValueError("Origin Vendor ID should be 0x131B, but instead found: {}".format(self.origin_vendor_id))
        return self

    @model_validator(mode='after')
    def check_pid(self) -> 'ProductInfo':
        if (self.vendor_id == espressif_vid and self.product_id != pid) or (self.origin_vendor_id != None and self.origin_product_id != origin_pid):
            raise ValueError("Origin Product Id in product info and cd_cert do not match")
        return self


def cert_get_value(line):
    value = line.split(",")[-1].split(":")[1].lstrip("w.").replace('"', '').replace(" ", '')
    return value

# used to parse the cd_cert data
def verify_cd_cert_data(cert_path):
    global espressif_vid, cert_id, pid, vid, device_type_id, origin_pid, origin_vid

    # Check if chip-cert is in path or not before actually running it
    chip_cert_path = shutil.which('chip-cert')
    if chip_cert_path == None:
        return False, "CD Cert Verification Failed", "Unable to find chip-cert in PATH", ""

    command = "chip-cert print-cd {}".format(cert_path)
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        i = 0
        if result is not None:
            i = i + 1
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if "tag[Context Specific]: 0x4" in line:
                    cert_id = cert_get_value(line)
                elif "tag[Anonymous]: 0x100, type: Unsigned Fixed Point (0x04)" in line:
                    pid = int(cert_get_value(line))
                elif "tag[Context Specific]: 0x1" in line:
                    vid = int(cert_get_value(line))
                elif "tag[Context Specific]: 0x3" in line:
                    device_type_id = int(cert_get_value(line))
                elif "tag[Context Specific]: 0x9" in line:
                    origin_vid = int(cert_get_value(line))
                elif "tag[Context Specific]: 0xa" in line:
                    origin_pid = int(cert_get_value(line))
            if cert_id == None:
                return False, "CD Cert Verification Failed", "Couldn't find the cert id", ""
            if pid == None:
                return False, "CD Cert Verification Failed", "Couldn't find the pid", ""
            if vid == None:
                return False, "CD Cert Verification Failed", "Couldn't find the vid", ""
            if device_type_id == None:
                return False, "CD Cert Verification Failed", "Couldn't find the device_type_id", ""
            if vid != espressif_vid and origin_vid == None:
                return False, "CD Cert Verification Failed", "origin vendor id not found in cd_cert file", ""
            if origin_vid != None and origin_pid == None:
                return False, "CD Cert Verification Failed", "origin product id not found in cd_cert file", ""
            if origin_vid == None and vid == espressif_vid:
                origin_vid = vid
                origin_pid = pid

            return True, "Success", "Successfully verified CD cert data", ""
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def is_valid_cert_file_path(cert_path):
    if not cert_path.endswith('.der'):
        raise argparse.ArgumentTypeError("CD Cert not a valid format")
    if not os.path.exists(cert_path):
        raise argparse.ArgumentTypeError("CD Cert path not valid")
    return cert_path

def is_valid_product_info_file_path(product_info_path):
    if not os.path.exists(product_info_path):
        raise argparse.ArgumentTypeError("Product info file doesn't exist")
    return product_info_path

def get_args():
    parser = argparse.ArgumentParser(description='Verify product info')
    parser.add_argument('--cert_path', type=is_valid_cert_file_path, required=True, help='Path to valid cd_cert file')
    parser.add_argument('--secret_client_id', type=str, default=None, help='Required to access the pid_vid allocation sheet')
    parser.add_argument('--product_info_path', type=is_valid_product_info_file_path, required=True, help='Product info file')
    parser.add_argument('--output_path', default="output", type=str, help="Provide the path to store the output files. If not set, \'output\' is used.")
    parser.add_argument("--skip_excel_verification", default=False, action='store_true', help="Does not verify against excel pid allocation sheet")

    args = parser.parse_args()
    return args.cert_path, args.secret_client_id, args.product_info_path, args.output_path, args.skip_excel_verification

def verify_product_info(cert_path, secret_client_id, product_info_path, skip_excel_verification):
    warning_msg = ""

    ret, description, details, warning_msg = verify_cd_cert_data(cert_path)
    if not ret:
        return False, description, details, warning_msg

    if not skip_excel_verification:
        if secret_client_id == None:
            return False, "Secret Client ID is Required", "secret_client_id is required to access the pid_vid allocation sheet", warning_msg
        # get the data from the spreadsheet
        i = 0
        while True:
            try:
                hex_origin_pid = "0x{:04X}".format(origin_pid)
                details = get_pid_details(hex_origin_pid, False, secret_client_id)
                if details == '{}':
                    return False, "PID Not Found in Database", f"Unable to find PID: {hex_origin_pid} in database", warning_msg
                break

            except:
                time.sleep(0.1) # 100 ms delay before retrying
                i = i + 1
                if i > 5:
                    return False, "Unable to access database", "Database Access Failed in product_info_validator", warning_msg

        # parsing the received data
        try:
            database_data = json.loads(details)
            database_cert_id = None
            if 'Pre-Provisioning' not in database_data:
                return False, "Product ID Not Found in Pre-Provisioning", "Product ID Not Found in Pre-Provisioning", warning_msg
            if 'ESP-ZeroCode' in database_data:
                database_cert_id = database_data['ESP-ZeroCode']['Cert ID'].replace(' ', '')
            else:
                warning_msg = f"Origin product id: {hex_origin_pid} not found in ESP-ZeroCode subsheet"

        except json.JSONDecodeError as e:
            return False, "JSON Syntax Error", f"Invalid JSON format received from database: {str(e)}", warning_msg

        database_hex_csa_vid = database_data['Pre-Provisioning']['CSA VID']
        database_csa_vid = int(database_hex_csa_vid, 0)

        if vid != database_csa_vid:
            return False, "VID Mismatch", f"CSA VID: {database_hex_csa_vid} in database does not match with cd_cert vid: {hex(vid)}", warning_msg

        if database_cert_id != None and database_cert_id != cert_id:
            return False, "Cert ID Mismatch", f"For CSA VID: {database_hex_csa_vid} and Origin PID: {hex_origin_pid}, Cert ID of database is: {database_cert_id} and Cert ID found in cd_cert is: {cert_id}, which do not match", warning_msg

    # validate the product_info.json
    try:
        with open(product_info_path) as product_info_file:
            product_info = ProductInfo(**json.loads(product_info_file.read()))
            return True, "Product Info file valid", f"Successfully Validated the product_info file: {product_info_path}", warning_msg

    except json.JSONDecodeError as e:
        return False, "Invalid Product Info JSON Syntax", str(e), warning_msg

    except ValueError as e:
        with open(product_info_path) as json_file:
            return False, "Failed to verify the product_info.json", error_handling(e, json.loads(json_file.read())), warning_msg

if __name__ == '__main__':
    cert_path, secret_client_id, product_info_path, output_path, skip_excel_validation = get_args()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ret, description, details, warning_msg = verify_product_info(cert_path, secret_client_id, product_info_path, skip_excel_validation)

    if not ret:
        create_status_file(output_path, "Failure", description, details, warning_msg)
        print(bcolors.FAIL + f"Verification failed: {description}" + bcolors.ENDC)
        if warning_msg:
            print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
        print(details)
        sys.exit(1)

    create_status_file(output_path, "Success", description, details, warning_msg)
    print(bcolors.OKGREEN + f"Verification successful: {description}" + bcolors.ENDC)
    if warning_msg:
        print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
    
