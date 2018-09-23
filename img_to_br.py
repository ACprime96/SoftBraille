#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:08:38 2017

@author: csrproject
"""

import io
import _thread
# import map_1
import cv2
import numpy as np
import json
import get_path
from generate_braille_text_image import Hed_test
global index
index=0
class img_braille():
    f1=""
    f2=""
    # con_f = open('/Users/adityachandra/Environments/myocr/Gui/config.json')
    # config = json.load(con_f)
    # con_f.close()

    def __init__(self,f1):
        self.f1=f1

    def convert_img(self):
        # image = cv2.imread(self.f1)
        # height, width = image.shape[:2]
        #
        # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
        # res = cv2.resize(img_gray_blur,None,fx=(80/width), fy=(84/height), interpolation = cv2.INTER_CUBIC)
        #
        # canny = cv2.Canny(res, 200, 255)
        # ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY_INV)
        #
        # hm,wm = mask.shape

        # Open a file
        s=get_path.get_braille_images()

        global index
        index=index+1
        fo = s+"/imbr"+str(index)+".txt"
        a = Hed_test()
        # a.start(self.f1,fo)
        try:
            _thread.start_new_thread( a.start,(self.f1,fo) )

        except Exception as exc:
            print(exc)

        # for i in range(2,hm,3):
        #     for j in range(1,wm,2):
        #         cell = (mask[i-2][j-1],mask[i-1][j-1],mask[i][j-1],mask[i-2][j],mask[i-1][j],mask[i][j])
        #         fo.write(chr(map_1.map[cell]).encode("utf-8"))
        #     fo.write("\n".encode("utf-8"))
        # fo.close()
