import qrcode
import argparse
import os
from datetime import datetime

# Argument parser for CLI usage
parser = argparse.ArgumentParser(description='Generate a QR code for a URL.')
parser.add_argument('--url', type=str, required=True, help='URL to encode in the QR code')
args = parser.parse_args()

# Output directory
output_dir = 'qr_codes'
os.makedirs(output_dir, exist_ok=True)

# Generate filename using timestamp
timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
filename = f'qr_{timestamp}.png'
filepath = os.path.join(output_dir, filename)

# Create the QR code
img = qrcode.make(args.url)
img.save(filepath)

print(f'[✓] QR code saved to: {filepath}')
