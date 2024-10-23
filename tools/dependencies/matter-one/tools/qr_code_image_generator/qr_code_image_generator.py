import os
from os import path
import argparse
from pathlib import Path

import io
import xml.etree.ElementTree as ET
import qrcode.image.svg
import cairosvg

def generate_qr_code_svg(qr_code: str, manual_code: str, file_path: Path) -> None:
    """Generate a QR code in SVG format.

    Args:
        qr_code (str): QR Code data to encode in the image.
        manual_code (str): Manual Code data to encode in the image.
        file_path (Path): File path to save the QR code in SVG format.

    Returns:
        None
    """
    # Generate a QR code with the specified data using the SvgPathImage image factory

    img = qrcode.make(qr_code, image_factory=qrcode.image.svg.SvgPathImage)

    # Create a BytesIO buffer to store the SVG image data
    buffer = io.BytesIO()
    img.save(buffer)  # Save the SVG image data to the buffer
    svg_contents = buffer.getvalue().decode('utf-8')

    # Parse the SVG image data as an ElementTree object
    root = ET.fromstring(svg_contents)

    # Find the 'path' element with the 'id' attribute equal to 'qr-path'
    qr_path = root.find(".//{http://www.w3.org/2000/svg}path[@id='qr-path']")
    d_attribute = qr_path.get('d')

    # Parse the SVG template file
    template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'matter_qr_code_type_1.svg')
    tree = ET.parse(template_file_path)
    root = tree.getroot()

    # Find the path and text elements and edit their attributes
    path = root.find(".//*[@id='qr-path']")
    path.set('d', d_attribute)

    text = root.find(".//*[@id='onboarding_code']")
    text.text = manual_code

    # Save the modified SVG file
    tree.write(str(file_path))

def convert_svg_to_png(svg_path, png_path):
    cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=300, scale=10, output_width=300)

def generate_qr_code(manual_code, qr_code: str, svg_path: Path, png_path: Path) -> None:
    generate_qr_code_svg(manual_code, qr_code, svg_path)
    convert_svg_to_png(svg_path, png_path)

def create_default_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_args():
    parser = argparse.ArgumentParser(description='QR Code image generator tool for ZeroCode')
    parser.add_argument("--qr_code", default=None, required=True, type=str, help='QR Code payload')
    parser.add_argument("--manual_code", default=None, required=True, type=str, help='Manual Code payload')
    parser.add_argument("--output_path", default=None, type=str, help='Path for output files')
    args = parser.parse_args()

    return args.qr_code, args.manual_code, args.output_path

def main():
    qr_code, manual_code, output_path = get_args()

    if output_path:
        path = os.path.join(output_path)
    else:
        path = os.path.join('output')

    create_default_dirs(path)
    generate_qr_code(qr_code, manual_code, os.path.join(path, 'qr_code.svg'), os.path.join(path, 'qr_code.png'))

    print('Created qr_code images at: ' + path + '/')

if __name__ == '__main__':
    main()
