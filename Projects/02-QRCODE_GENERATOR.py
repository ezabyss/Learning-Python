# module
# pyqrcode  : to generate QR CODE 
# pypng     : to render as .png file 
# pyzbar    : to decode the qrcode
import pyqrcode

# creating 
print("Welcome to the QRCODE GENERATOR: ")
scrt_msg = input("Please, enter your message: ")
result = pyqrcode.create(scrt_msg)
result.png("Projects/Assets/QRCODE.png",scale=5)

print("QRCODE GENERATED SUCCESSFULLY")


