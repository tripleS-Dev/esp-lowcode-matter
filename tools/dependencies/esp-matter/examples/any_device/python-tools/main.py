import sys
import os
from create_json import create_json_data_model
from create_binary import create_binary_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_.matter_file>")
        sys.exit(1)

    idl_file_path = sys.argv[1]

    if not os.path.exists(idl_file_path):
        print(f"File not found: {idl_file_path}")
        sys.exit(1)

    # Derive the base filename from the .matter file
    base_filename = os.path.splitext(idl_file_path)[0]

    # Create JSON data model
    json_file_path = f"{base_filename}.json"
    create_json_data_model(idl_file_path, json_file_path)

    # Create binary file from JSON data model
    bin_file_path = f"{base_filename}.bin"
    create_binary_file(json_file_path, bin_file_path)

if __name__ == "__main__":
    main()
