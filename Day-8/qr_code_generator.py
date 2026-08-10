#

import qrcode

# Get text or URL from the user
data = input("Enter text or URL: ")

# Create QR code
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("qrcode.png")

print("QR Code generated successfully!")
print("Saved as: qrcode.png")