import imutils
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import cv2
import time

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
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break


for barcode in barcodes:
    print(barcode) 

print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()