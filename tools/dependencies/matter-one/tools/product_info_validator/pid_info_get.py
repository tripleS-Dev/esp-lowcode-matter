from os import path
from time import sleep
import pandas as pd
from io import BytesIO
from typing import Union
import argparse
import re
from share_point_client import SharePointClient

def is_valid_hex(pid):
    """ Validate if the input is a valid uppercase hexadecimal. """
    if re.match(r'^0x[0-9A-F]+$', pid):
        return pid
    else:
        raise argparse.ArgumentTypeError(f"'{pid}' is not a valid uppercase hexadecimal value.")

# Function to read an Excel file from either a local path or a URL
def read_excel_file(source: Union[str, bytes], sheet_name: str):
    if isinstance(source, bytes):
        # If the source is bytes, assume it's downloaded content
        return pd.read_excel(BytesIO(source), sheet_name=sheet_name, header=1)
    else:
        # If the source is a string, treat it as a file path
        return pd.read_excel(source, sheet_name=sheet_name, header=1)

# Function to find a row by PID with cell references for expected headers
def find_row_by_pid_with_cell_references(df, pid):
    row_data = df[df['PID'] == pid]
    if not row_data.empty:
        row_dict = row_data.iloc[0].to_dict()
        new_row_dict = {}
        for idx, (key, value) in enumerate(row_dict.items()):
            if 'Unnamed' in key:
                new_key = f"{chr(65 + idx)}2"  # Excel column letter + row number 2 for header
                new_row_dict[new_key] = value
            else:
                new_row_dict[key] = value
        return new_row_dict
    return None

# Function to search for a PID in both sheets and return a combined result with cell references
def search_pid_with_cell_references(pid, sheet1_df, sheet2_df):
    combined_result = {}
    row1 = find_row_by_pid_with_cell_references(sheet1_df, pid)
    if row1:
        combined_result['ESP-ZeroCode'] = row1
    row2 = find_row_by_pid_with_cell_references(sheet2_df, pid)
    if row2:
        combined_result['Pre-Provisioning'] = row2
    return combined_result


def get_pid_details(pid, to_save, client_secret):
    tenant_id = "5faf27fd-3557-4294-9545-8ea74a409f39"
    client_id = "bf776721-87a5-4ce9-91b1-8c83ea5227ee"
    resource = "https://graph.microsoft.com/"

    client = SharePointClient(tenant_id, client_id, client_secret, resource)
    target_file = 'General/ESP Matter PID allocation.xlsx'

    file_name, file_content = client.run_all(target_file)

    if to_save and file_content:
        with open(file_name, "wb") as file:
            file.write(file_content)
        data_source = file_name
    else:
        data_source = file_content

    esp_zero_code_df = read_excel_file(data_source, 'ESP-ZeroCode')
    pre_provisioning_df = read_excel_file(data_source, 'Pre-Provisioning')

    combined_result = search_pid_with_cell_references(pid, esp_zero_code_df, pre_provisioning_df)
    return pd.Series(combined_result).to_json()
