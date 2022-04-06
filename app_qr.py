# QR code generator by blomjoe

import qrcode
from PIL import Image

value = input("\nPlease enter content for QR code:\n\n")

img = qrcode.make(value)
img.save("QR.jpg")

print("\nQR code generated in program path.\n")