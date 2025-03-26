import sys
import os
from shared_imports import *
from create_json import create_json_data_model
from create_binary import create_binary_file
from attribute_bounds_maker import process_directories

def run_linter(idl_path):
    """Lints the .matter file using idl_lint.py"""
    original_argv = sys.argv
    sys.argv = ['idl_lint.py', idl_path]
    try:
        idl_lint.main()
    except SystemExit as e:
        if e.code != 0:
            print(f"Linter exited with code: {e.code}")
            sys.exit(e.code)
    except Exception as e:
        print(f"An error occurred during linting: {e}")
        sys.exit(1)
    finally:
        sys.argv = original_argv

def check_files_exist():
    """Check if both attribute_bounds.csv and attribute_bounds.pkl exist."""
    csv_exists = os.path.exists('attribute_bounds.csv')
    pickle_exists = os.path.exists('attribute_bounds.pkl')
    return csv_exists and pickle_exists

def ensure_attribute_files():
    """Ensure attribute_bounds.csv and attribute_bounds.pkl exist, running the maker if necessary."""
    if not check_files_exist():
        print("attribute_bounds.csv or attribute_bounds.pkl not found, generating them...")
        
        directories = [
            os.path.expandvars(os.path.join('$ESP_MATTER_PATH', 'connectedhomeip', 'connectedhomeip', 'src', 'app', 'zap-templates', 'zcl', 'data-model', 'chip')),
            # Add more directories if necessary
        ]
        
        output_csv = 'attribute_bounds.csv'
        output_pickle = 'attribute_bounds.pkl'
        
        process_directories(directories, output_csv, output_pickle)
    
    if not check_files_exist():
        raise FileNotFoundError("Failed to create attribute_bounds.csv or attribute_bounds.pkl")

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <path_to_.matter_file> <output_files_path>")
        sys.exit(1)

    idl_file_path = sys.argv[1]
    output_files_path = sys.argv[2]

    if not os.path.exists(idl_file_path):
        print(f"File not found: {idl_file_path}")
        sys.exit(1)

    if not os.path.exists(output_files_path):
        os.makedirs(output_files_path)

    ensure_attribute_files()

    # Run the linter before proceeding
    run_linter(idl_file_path)

    # Create JSON data model
    json_file_path = os.path.join(output_files_path, "data_model.json")
    create_json_data_model(idl_file_path, json_file_path)

    # Create binary file from JSON data model
    bin_file_path = os.path.join(output_files_path, "data_model.bin")
    create_binary_file(json_file_path, bin_file_path)

if __name__ == "__main__":
    main()
