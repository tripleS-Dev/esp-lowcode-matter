import sys
import os

def binary_to_c_array(file_path):
    # Read the binary file
    with open(file_path, 'rb') as f:
        binary_data = f.read()

    # Convert the binary data to a C array format
    hex_array = ', '.join(f'0x{byte:02x}' for byte in binary_data)
    array_name = os.path.splitext(os.path.basename(file_path))[0]

    # Create the C code string
    c_code = f'uint8_t data_model_bin[] = {{ {hex_array} }};'

    return c_code

def write_c_header(c_code, output_dir):
    # Determine the header file path
    header_file_path = os.path.join(output_dir, 'data_model_bin.h')

    # Write the C code to the header file
    with open(header_file_path, 'w') as f:
        f.write(c_code)

    print(f'Header file created: {header_file_path}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python c-header-maker.py <binary_file>')
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f'File not found: {file_path}')
        sys.exit(1)

    # Generate the C array code from the binary file
    c_code = binary_to_c_array(file_path)

    # Assume the current directory is 'python-tools'
    output_dir = os.path.join(os.curdir, '..', 'main')
    
    # Normalize path to absolute path
    output_dir = os.path.abspath(output_dir)

    # Write the C code to the header file in the main directory
    write_c_header(c_code, output_dir)

if __name__ == '__main__':
    main()
