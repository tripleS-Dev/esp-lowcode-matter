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
import csv

def write_data_to_output_csv(path, key, value):
    with open(os.path.join(path, 'output.csv'), 'a') as output_file:
        writer = csv.writer(output_file)

        row_data = [key, value]
        writer.writerow(row_data)

def write_info_file_to_output_csv(path, key, file_name):
    value = None
    with open(os.path.join(path, file_name), 'r') as info_file:
        value = info_file.read()
    write_data_to_output_csv(path, key, value)

def finish_output_csv(path):
    transposed_data = None
    with open(os.path.join(path, 'output.csv'), 'r') as output_file:
        rows_list = list(csv.reader(output_file, delimiter=','))
        # Remove any empty rows, zip otherwise returns empty list
        rows_list = [row for row in rows_list if row]
        transposed_data = list(zip(*rows_list))

    with open(os.path.join(path, 'output.csv'), 'w+', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(transposed_data)
