import json
import os
import argparse
from pydantic import BaseModel, ValidationError
from typing import List, Optional
from sys import exit

class ChipModel(BaseModel):
    id: str
    gpio_pins: List[int]
    adc_connections: List[int]
    strapping_pins: List[int]
    only_input_pins: Optional[List[int]] = None

class EspDevice(BaseModel):
    id: str
    list: List[ChipModel]

class IoData(BaseModel):
    esp_device: List[EspDevice]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Validation for io_data")
    parser.add_argument("--io_data_path", default="io_data.json", type=str, help="Provide path for the io_data.json to validate")
    args = vars(parser.parse_args())
    file_path = args['io_data_path']
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        io_data = IoData(**data)
        print("IO_DATA JSON is valid.")
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"IO_DATA JSON is invalid: {e}")
