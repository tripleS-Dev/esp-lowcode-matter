import os
from os import path
import sys
from sys import exit
import argparse
import json

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
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools', 'product_info_validator'))
    sys.path.insert(0, os.path.join(os.getenv('MATTER_ONE_PATH'), 'tools', 'product_io_validator'))
else:
    print("Please set the MATTER_ONE_PATH environment variable.")
    exit(1)

from json_validator import verify_product_config
from product_info_validator import verify_product_info
from io_check import config_io_check

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def is_valid_product_path(product_path):
    if not os.path.exists(product_path):
        raise argparse.ArgumentTypeError("Product path does not exist")
    return str(product_path)

def create_status_file(path, status='Success', description='Success', details = '', warnings = list()):
    with open(os.path.join(path, 'status.json'), 'w+') as info_file:
        status_info = {
            "status": status,
            "description": description,
            "details": details,
            "warnings": warnings
        }
        json.dump(status_info, info_file, indent=4)

def get_args():
    parser = argparse.ArgumentParser(description='Product data validator')
    parser.add_argument("--product_path", default="", type=is_valid_product_path, required=True, help="Provide path for the product to validate")
    parser.add_argument('--secret_client_id', default=None, type=str, help='Required to access the pid_vid allocation sheet')
    parser.add_argument('--output_path', default="output", type=str, help="Provide the path to store the output files. If not set, \'output\' is used.")
    parser.add_argument("--no_config_validation", default=False, action='store_true', help="Don't validate product_config")
    parser.add_argument("--no_info_validation", default=False, action='store_true', help="Don't validate product_info")
    parser.add_argument("--no_io_validation", default=False, action='store_true', help="Don't validate io of product_config.json")

    args = parser.parse_args()
    return args.product_path, args.secret_client_id, args.output_path, args.no_config_validation, args.no_info_validation, args.no_io_validation

def validate_product_data(product_path, secret_client_id, no_config_validation, no_info_validation, no_io_validation, is_low_code):
    details = "Success"
    warning_msg = list()
    description = ""
    ret = True

    product_info_path = os.path.join(product_path, 'product_info.json')
    product_config_path = os.path.join(product_path, 'product_config.json')
    cert_path = os.path.join(product_path, 'cd_cert.der')

    for filename in os.listdir(product_path):
        if filename.endswith('.der') and 'cd_cert' in filename:
            cert_path = os.path.join(product_path, filename)
            break

    if not no_config_validation:
        if not os.path.exists(product_config_path):
            return False, "Product path not valid", "product_config.json is not present", warning_msg

        ret, description, details, warning = verify_product_config(product_config_path, is_low_code)
        if warning:
            warning_msg.append(warning)
        if not ret:
            return ret, description, details, warning_msg

    if not no_info_validation:
        if not os.path.exists(cert_path):
            return False, "Product path not valid", "cd_cert is not present", warning_msg
        if not os.path.exists(product_info_path):
            return False, "Product path not valid", "product_info is not present", warning_msg

        # NOTE: Not validating the product info against excel sheet.
        ret, description, details, warning = verify_product_info(cert_path, secret_client_id, product_info_path, True)
        if warning:
            warning_msg.append(warning)
        if not ret:
           return ret, description, details,  warning_msg

    if not no_io_validation:
       if not os.path.exists(product_info_path):
            return False, "Product path not valid", "product_info is not present", warning_msg
       if not os.path.exists(product_config_path):
            return False, "Product path not valid", "product_config.json is not present", warning_msg

       ret, description, details, warning = config_io_check(product_path)
       if warning:
           warning_msg.append(warning)
       if not ret:
           return ret, description, details, warning_msg

    return ret, description, details, warning_msg

if __name__ == '__main__':
    product_path, secret_client_id, output_path, no_config_validation, no_info_validation, no_io_validation = get_args()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ret, description, details, warning_msg = validate_product_data(product_path, secret_client_id, no_config_validation, no_info_validation, no_io_validation)

    if not ret:
        create_status_file(output_path, "Failure", description, details, warning_msg)
        print(bcolors.FAIL + f"Failed to verify product data: {description}" + bcolors.ENDC)
        print(bcolors.FAIL + f"Error message: {json.dumps(details, indent=4)}" + bcolors.ENDC)
        if warning_msg:
            print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
        exit(1)

    print(bcolors.OKGREEN + f"Successfully Validated product data" + bcolors.ENDC)
    if warning_msg:
        print(bcolors.WARNING + f"Warnings: {warning_msg}" + bcolors.ENDC)
    create_status_file(output_path, "Success", description, details, warning_msg)
