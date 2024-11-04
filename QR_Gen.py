import qrcode
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Generate a QR code from input data.")
parser.add_argument('data', type=str, help='The data to encode in the QR code.')
parser.add_argument('output_path', type=str, help='The path where the QR code image will be saved.')
parser.add_argument('--box_size', type=int, default=10, help='Size of each box in pixels (default is 10).')
parser.add_argument('--border', type=int, default=4, help='Width of the border (default is 4).')

# Parse arguments
args = parser.parse_args()

# Ensure the output directory exists
output_dir = os.path.dirname(args.output_path)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")

# Create QR code with custom dimensions
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=args.box_size,
    border=args.border,
)

qr.add_data(args.data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save(args.output_path)

print(f"QR code generated and saved to {args.output_path}")
