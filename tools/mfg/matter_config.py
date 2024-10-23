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
from types import SimpleNamespace
import json

from qr_code_image_generator import *
from output_file_creation import *
from sources.mfg_tool import *

def add_matter_to_csv(path):
    with open(os.path.join(path, 'mfg_config.csv'), 'a') as info_file:
        info_file.write('chip-factory,namespace,,')
        info_file.write('\n')
        info_file.write('discriminator,file,u32,' + str(os.path.join(path, 'discriminator.info')))
        info_file.write('\n')
        info_file.write('iteration-count,file,u32,' + str(os.path.join(path, 'iteration_count.info')))
        info_file.write('\n')
        info_file.write('salt,file,string,' + str(os.path.join(path, 'salt.info')))
        info_file.write('\n')
        info_file.write('verifier,file,string,' + str(os.path.join(path, 'verifier.info')))
        info_file.write('\n')
        info_file.write('cert-dclrn,file,binary,' + str(os.path.join(path, 'cd_cert.der')))
        info_file.write('\n')
        info_file.write('vendor-id,file,u32,' + str(os.path.join(path, 'vendor_id.info')))
        info_file.write('\n')
        info_file.write('product-id,file,u32,' + str(os.path.join(path, 'product_id.info')))
        info_file.write('\n')
        info_file.write('vendor-name,file,string,' + str(os.path.join(path, 'vendor_name.info')))
        info_file.write('\n')
        info_file.write('product-name,file,string,' + str(os.path.join(path, 'product_name.info')))
        info_file.write('\n')
        info_file.write('serial-num,file,string,' + str(os.path.join(path, 'serial_num.info')))
        info_file.write('\n')
        info_file.write('rd-id-uid,file,hex2bin,' + str(os.path.join(path, 'rotating_device_id.info')))
        info_file.write('\n')
        info_file.write('hardware-ver,file,u32,' + str(os.path.join(path, 'hw_ver.info')))
        info_file.write('\n')
        info_file.write('hw-ver-str,file,string,' + str(os.path.join(path, 'hw_ver_str.info')))
        info_file.write('\n')

def add_matter_to_output_csv(path):
    write_info_file_to_output_csv(path, 'discriminator', 'discriminator.info')
    write_info_file_to_output_csv(path, 'iteration_count', 'iteration_count.info')
    write_info_file_to_output_csv(path, 'salt', 'salt.info')
    write_info_file_to_output_csv(path, 'verifier', 'verifier.info')
    write_info_file_to_output_csv(path, 'vendor_id', 'vendor_id.info')
    write_info_file_to_output_csv(path, 'product_id', 'product_id.info')
    write_info_file_to_output_csv(path, 'vendor_name', 'vendor_name.info')
    write_info_file_to_output_csv(path, 'product_name', 'product_name.info')
    write_info_file_to_output_csv(path, 'serial_num', 'serial_num.info')
    write_info_file_to_output_csv(path, 'rotating_device_id', 'rotating_device_id.info')
    write_info_file_to_output_csv(path, 'hw_ver', 'hw_ver.info')
    write_info_file_to_output_csv(path, 'hw_ver_str', 'hw_ver_str.info')
    write_info_file_to_output_csv(path, 'passcode', 'passcode.info')
    write_info_file_to_output_csv(path, 'qr_code_url', 'qr_code_url.info')

def generate_cd(path, products_path, product, vendor_id, product_id, origin_vendor_id, origin_product_id, device_type_id, not_save_cd_cert):
    product_path = os.path.join(os.getcwd(), products_path, product)
    cd_cert_name = os.path.join(product_path, 'cd_cert_' + vid_pid_str(vendor_id, product_id) + '.der')
    cd_exists = os.path.exists(cd_cert_name)
    out_cd_cert_path = os.path.join(path, 'cd_cert.der')
    if not cd_exists:
        if os.path.exists(out_cd_cert_path):
            os.remove(out_cd_cert_path)
        TOOLS['chip-cert'] = shutil.which('chip-cert')
        signing_cert = str(os.path.join('certs', 'cd_signing_cert.pem'))
        signing_key = str(os.path.join('certs', 'cd_signing_key.pem'))
        certificate_id = 'CSA22107MAT40107-24'
        cmd = [
            TOOLS['chip-cert'], 'gen-cd',
            '--key', signing_key,
            '--cert', signing_cert,
            '--out', out_cd_cert_path,
            '--format-version', str(1),
            '--security-level', str(0),
            '--security-info', str(0),
            '--version-number', str(9876),
            '--certification-type', str(1),
            '--certificate-id', certificate_id,
            '--vendor-id', hex(vendor_id),
            '--product-id', hex(product_id),
            '--dac-origin-vendor-id', hex(origin_vendor_id),
            '--dac-origin-product-id', hex(origin_product_id),
            '--device-type-id', hex(device_type_id),
        ]
        execute_cmd(cmd)
        print("The items in path is: {}".format(os.listdir(path)))
        logging.info('Generated CD certificate: {}'.format(cd_cert_name))
        print('New CD generated')
        if not not_save_cd_cert:
            shutil.copyfile(out_cd_cert_path, cd_cert_name)
    else:
        shutil.copyfile(cd_cert_name, out_cd_cert_path)

    return cd_cert_name

def setup_out_dirs(path, count):
    if not os.path.exists(os.path.join(path, 'staging')):
        os.makedirs(os.path.join(path, 'staging'))

    OUT_DIR['top']  = path
    OUT_DIR['stage'] = str(os.path.join(path, 'staging'))

    OUT_FILE['config_csv']   = os.sep.join([OUT_DIR['stage'], 'config.csv'])
    OUT_FILE['mcsv']         = os.sep.join([OUT_DIR['stage'], 'master.csv'])
    OUT_FILE['pin_csv']      = os.sep.join([OUT_DIR['stage'], 'pin.csv'])
    OUT_FILE['pin_disc_csv'] = os.sep.join([OUT_DIR['stage'], 'pin_disc.csv'])
    OUT_FILE['cn_dac_csv']   = os.sep.join([OUT_DIR['stage'], 'cn_dacs.csv'])

    for i in range(count):
        uuid_str = ''
        UUIDs.append(uuid_str)
        os.makedirs(os.sep.join([OUT_DIR['top'], uuid_str, 'internal']), exist_ok=True)

def add_optional_KVs():
    chip_factory_append('rd-id-uid', 'data', 'hex2bin', None)
    chip_factory_append('serial-num', 'data', 'string', None)
    chip_factory_append('verifier', 'data', 'string', None)


def add_matter_data_to_files(path, vendor_id, product_id, vendor_name, product_name, hw_ver, hw_ver_str, serial_num):
    with open(OUT_FILE['mcsv'], 'r') as csv_file:
        csv_dict = csv.DictReader(csv_file)
        for row in csv_dict:
            with open(os.path.join(path, 'discriminator.info'), 'w+') as info_file:
                info_file.write(row['discriminator'])
            with open(os.path.join(path, 'iteration_count.info'), 'w+') as info_file:
                info_file.write(row['iteration-count'])
            with open(os.path.join(path, 'salt.info'), 'w+') as info_file:
                info_file.write(row['salt'])
            with open(os.path.join(path, 'verifier.info'), 'w+') as info_file:
                info_file.write(row['verifier'])
            with open(os.path.join(path, 'rotating_device_id.info'), 'w+') as info_file:
                info_file.write(row['rd-id-uid'])

    with open(os.path.join(path, 'vendor_id.info'), 'w+') as info_file:
        info_file.write(str(vendor_id))
    with open(os.path.join(path, 'product_id.info'), 'w+') as info_file:
        info_file.write(str(product_id))
    with open(os.path.join(path, 'vendor_name.info'), 'w+') as info_file:
        info_file.write(vendor_name)
    with open(os.path.join(path, 'product_name.info'), 'w+') as info_file:
        info_file.write(product_name)
    with open(os.path.join(path, 'hw_ver.info'), 'w+') as info_file:
        info_file.write(str(hw_ver))
    with open(os.path.join(path, 'hw_ver_str.info'), 'w+') as info_file:
        info_file.write(hw_ver_str)
    with open(os.path.join(path, 'serial_num.info'), 'w+') as info_file:
        info_file.write(serial_num)

    qr_code = None
    manual_code = None
    passcode = None
    with open(os.path.join(path, '-onb_codes.csv'), 'r') as info_file:
        csv_data = csv.DictReader(info_file)
        row = csv_data.__next__()
        qr_code = row['qrcode']
        manual_code = row['manualcode']
        passcode = row['passcode']

    generate_qr_code(qr_code, manual_code, os.path.join(path, 'qr_code.svg'), os.path.join(path, 'qr_code.png'))

    with open(os.path.join(path, 'qr_code.info'), 'w+') as info_file:
        info_file.write(qr_code)
    with open(os.path.join(path, 'manual_code.info'), 'w+') as info_file:
        info_file.write(manual_code)
    with open(os.path.join(path, 'passcode.info'), 'w+') as info_file:
        info_file.write(passcode)

    print("QR code is: " + qr_code)
    print("Manual code is: " + manual_code)
    print("QR code images: qr_code.svg, qr_code.png")
    url = 'https://project-chip.github.io/connectedhomeip/qrcode.html?data={}'.format(qr_code)
    print("QR code URL: " + url)
    with open(os.path.join(path, 'qr_code_url.info'), 'w+') as info_file:
        info_file.write(url)

    os.remove(os.path.join(path, '-onb_codes.csv'))
    os.remove(os.path.join(path, '-qrcode.png'))
    shutil.rmtree(os.path.join(path, 'internal'))
    shutil.rmtree(os.path.join(path, 'staging'))

def get_product_info_details(products_path, product):
    product_path = os.path.join(os.getcwd(), products_path, product)
    print('Getting product_info json for: ' + product)

    product_file = open(os.path.join(product_path, 'product_info.json'))
    product_json = json.load(product_file)
    product_file.close()

    vendor_id = product_json['vendor_id']
    product_id = product_json['product_id']
    device_type_id = product_json['device_type_id']
    vendor_name = product_json['vendor_name']
    product_name = product_json['product_name']
    hw_ver = product_json['hw_ver']
    hw_ver_str = product_json['hw_ver_str']

    origin_vendor_id = 4891
    origin_product_id = 2
    if 'origin_vendor_id' in product_json:
        origin_vendor_id = product_json['origin_vendor_id']
    if 'origin_product_id' in product_json:
        origin_product_id = product_json['origin_product_id']

    return vendor_id, product_id, origin_vendor_id, origin_product_id, device_type_id, vendor_name, product_name, hw_ver, hw_ver_str

def create_matter_files(path, products_path, certs_path, mac_address, node_platform, port, product, node_id, mqtt_endpoint, serial_number, test, no_matter, no_rainmaker, not_save_cd_cert):
    vendor_id, product_id, origin_vendor_id, origin_product_id, device_type_id, vendor_name, product_name, hw_ver, hw_ver_str  = get_product_info_details(products_path, product)

    setup_out_dirs(path, 1)
    add_optional_KVs()

    args = SimpleNamespace(count=1, passcode=None, discriminator=None, enable_dynamic_passcode=False)
    generate_passcodes_and_discriminators(args)

    args = SimpleNamespace(csv=None)
    write_csv_files(args)
    cd_cert = generate_cd(path, products_path, product, vendor_id, product_id, origin_vendor_id, origin_product_id, device_type_id, not_save_cd_cert)
    if serial_number is not None:
        serial_num = serial_number[:32]
    else:
        serial_num = node_id.replace("-", "")[:32]

    args = SimpleNamespace(paa=False, pai=False, dac_cert=None, dac_key=None, cn_prefix=None, lifetime=0, valid_from=None, vendor_id=vendor_id, product_id=product_id, cert_dclrn=cd_cert, commissioning_flow=0, discovery_mode=1, enable_rotating_device_id=True, rd_id_uid=None, serial_num=serial_num, csv=None, mcsv=None, enable_dynamic_passcode=False)
    write_per_device_unique_data(args)

    add_matter_data_to_files(path, vendor_id, product_id, vendor_name, product_name, hw_ver, hw_ver_str, serial_num)
    print("Created Matter files")
