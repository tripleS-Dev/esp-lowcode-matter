import os
import argparse
import json
from json.decoder import JSONDecodeError
from pydantic import ValidationError
from data_handler.error_handling import error_handling
from data_handler.base_model import set_locale
from sys import exit

from doc_generator import generate_documentation

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def create_status_file(path, status='Success', description='Success', details=''):
    with open(os.path.join(path, 'status.json'), 'w+') as info_file:
        status_info = {
            "status": status,
            "description": description,
            "details": details
        }
        json.dump(status_info, info_file, indent=4)

def generate_files(json_schema_file_path, json_documentation_file_path):
    # NOTE: This is called here because, this needs to be done after the locale is set
    from zerocode_product.zerocode_product_config import ZerocodeProductConfig

    schema = ZerocodeProductConfig.model_json_schema()
    with open(json_schema_file_path, "w") as json_schema:
        json_schema.write(json.dumps(schema, indent=4))
    print(bcolors.OKGREEN + "Successfully generated the JSON Schema at: " + json_schema_file_path + bcolors.ENDC)

    generate_documentation(schema, json_documentation_file_path)
    print(bcolors.OKGREEN + "Successfully generated the JSON Documentation at: " + json_documentation_file_path + bcolors.ENDC)

def verify_product_config(product_config_path, output_path, is_low_code):
    # NOTE: This is called here because, this needs to be done after the locale is set
    from zerocode_product.zerocode_product_config import ZerocodeProductConfig
    from low_code_product.lowcode_product_config import LowcodeProductConfig
    try:
        with open(product_config_path) as json_file:
            if is_low_code:
                product = LowcodeProductConfig(**json.loads(json_file.read()))
            else:
                product = ZerocodeProductConfig(**json.loads(json_file.read()))
        print(bcolors.OKGREEN + "Successfully Validated the product config file: {}".format(product_config_path) + bcolors.ENDC)
    except JSONDecodeError as e:
        status = 'Failure'
        description = 'Product Config JSON File Format Invalid'
        details = str(e)
        if output_path != None:
            create_status_file(output_path, status, description, details)
        print(bcolors.FAIL + description)
        print(e)
        print(bcolors.ENDC)
        return -1
    except ValidationError as e:
        print(bcolors.FAIL + "These Errors were found in the product_config: {}".format(product_config_path) + bcolors.ENDC)
        with open(product_config_path) as json_file:
            error = error_handling(e, json.loads(json_file.read()))
            status = 'Failure'
            description = 'Errors were found in the product config. Check the details for more info.'
            details = json.dumps(error, indent=4)
            if output_path != None:
                create_status_file(output_path, status, description, details)
            print(bcolors.FAIL + details + bcolors.ENDC)
            print(description)
        return -1
    
    return 0

def create_default_dir(path, locale):
    if not os.path.exists(path):
        os.makedirs(path)
    locale_path = os.path.join(path, locale)
    if not os.path.exists(locale_path):
        os.makedirs(locale_path)
    return locale_path

def get_args():
    parser = argparse.ArgumentParser(description="Product Config Validation and JSON Schema validator for matter-one")
    parser.add_argument("--product_config_path", default="", type=str, help="Provide path for the product_config.json to validate")
    parser.add_argument('--output_path', default="output", type=str, help="Provide the path to store the output files. If not set, \'output\' is used.")
    parser.add_argument("--low_code", default=False, action='store_true', help="validate product_config for low_code application")

    args = vars(parser.parse_args())
    return args['product_config_path'], args['output_path'], args['low_code']

def main():
    product_config_path, output_path, is_low_code = get_args()
    # The locales need to be lower case for it to work in the backend
    supported_locales = ['en-us', 'zh-cn']

    for locale in supported_locales:
        print('Generating files for locale: ' + locale)
        path = create_default_dir(output_path, locale)
        json_schema_file_path = os.path.join(path, 'json_schema.json')
        json_documentation_file_path = os.path.join(path, 'json_documentation.md')

        set_locale(locale)
        generate_files(json_schema_file_path, json_documentation_file_path)

    if os.path.exists(product_config_path):
        print('Validating product config: ' + product_config_path)
        ret = verify_product_config(product_config_path, output_path, is_low_code)
        if ret != 0:
            exit(1)

    create_status_file(output_path)

if __name__ == '__main__':
    main()
