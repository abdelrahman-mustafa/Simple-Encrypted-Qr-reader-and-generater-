import imutils
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import cv2
import time
import qrcode 
import numpy
import PIL 
class Qrcode(object):
    def __init__(self, plainText):
        self.text = plainText
    def genQr(self):
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
        qr.add_data(self.text)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")

    def readQr(self):
        print("starting video stream...")
        vs = VideoStream(src=0).start()
        time.sleep(2.0)
        while True:
            frame = vs.read()
            pytframe = imutils.resize(frame, width=400)
            barcodes = pyzbar.decode(frame)
            if barcodes:
                break 
            else:
                pass
            cv2.imshow("qrCode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        if barcodes:
            return barcodes[0]

        print("[INFO] cleaning up...")
        cv2.destroyAllWindows()
        vs.stop()

    def readImQr(self, image):
        print(image)
        pil_image = PIL.Image.open(image).convert('RGB') 
        image = numpy.array(pil_image) 
        image = imutils.resize(image, width=400)
        barcodes = pyzbar.decode(image)
        if barcodes:
            return barcodes[0]
