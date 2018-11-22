from qrcodeR import *
from encData import *


if __name__ == '__main__':
    key = 'boda1010'
    cipher = AESCipher(key) 

    plaintext = b'Hi there '
    encrypted = cipher.encrypt(plaintext)
    print(encrypted)
    qr = Qrcode(encrypted)
    image = qr.genQr()
    text = qr.readImQr(image)
    print(text)