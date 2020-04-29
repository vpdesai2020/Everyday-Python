from pyzbar.pyzbar import decode
from PIL import Image


def qrCode():
    try:
        img  = decode(Image.open("QR.png"))
        print(img[0].data.decode())
    except IOError:
        print("file NOT found")
        pass
  
qrCode()
