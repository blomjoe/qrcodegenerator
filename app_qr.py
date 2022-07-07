# QR code generator by blomjoe

import qrcode
from PIL import Image

value = input("\nenter content for QR code:\n\n")

img = qrcode.make(value)
img.save("QR_export.jpg")

print("\nQR code generated in program path.\n")
