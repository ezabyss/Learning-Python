from pyzbar.pyzbar import decode 
from PIL import Image   
# reading Qr    
img = Image.open("Projects/Assets/QRCODE.png")

# img.show()
d = decode(img)

print(d[0].data.decode)
