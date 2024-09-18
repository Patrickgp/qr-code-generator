import os
import qrcode

# Path to save the QR codes on your desktop
output_dir = '/Users/patrick.poopathi/Desktop/qr-codes'

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# IDs to generate QR codes
# Replace with test or sample ids
ids = ['47215', '47136', '47098', '47073', '46358', '46355', '46352', '46349']

# Generate and save the QR codes
for i in ids:
    qr = qrcode.make(i)
    qr.save(os.path.join(output_dir, f'{i}.png'))

print(f"QR codes saved to {output_dir}")
