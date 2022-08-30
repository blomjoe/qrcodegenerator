# QR code generator by blomjoe

import qrcode
from PIL import Image
import PySimpleGUI as sg
import os.path

import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter text or link for QR-Code'), sg.InputText()],
            [sg.Button('Generate')] ]

# Create the Window
window = sg.Window('Python QR-Code Generator by blomma-dev', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Generate': # if user closes window or clicks cancel
        break
    print("QR code generated in program path.")


img = qrcode.make(values[0])
img.save("QR_export.jpg")

print("\nQR code generated in program path.\n")

window.close()