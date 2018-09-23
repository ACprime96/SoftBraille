import cv2
import numpy as np
from PIL import Image
import pytesseract
import json
import get_path

class imgt():
    f1=""   #to read images to process
    f2=""
       #to convert img to text using ocr
    def __init__(self,f1):
        self.f1=f1


    def imgtes(self):
        try:
            imgIn = cv2.imread(self.f1, cv2.IMREAD_GRAYSCALE)
            kernel = np.zeros( (9,9), np.float32)
            kernel[4,4] = 2.0
            boxFilter = np.ones( (9,9), np.float32) / 81.0
            kernel = kernel - boxFilter
            custom = cv2.filter2D(imgIn, -1, kernel)
            res1 = cv2.resize(custom,(0,0),fx=0.75,fy=0.75)
            f=open(get_path.get_english(),'w+',encoding="utf-8")
            f.write(pytesseract.image_to_string(custom))
            f.close()
        except Exception as e:
            print("Image quality is poor!!")
            f=open(get_path.get_english(),'w+',encoding="utf-8")
            f.close()
