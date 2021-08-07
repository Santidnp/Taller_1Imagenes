import cv2
import numpy as np
import sys
import os
class basicColor():
    
    def __init__(self,path):

        self.path = path
        self.image = cv2.imread(path)

    def displayProperties(self):
        Pixeles = self.image.shape[0]*self.image.shape[1]
        canales = self.image.shape[2]
        print(f'canales : {canales}')
        print(f'píxeles:{Pixeles}')

    def makeBW(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret, imgOstu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Image", imgOstu)
        cv2.waitKey(0)
    def colorize(self,hue):
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(image_hsv)
        h = hue*np.ones_like(h)
        image_hue = cv2.merge((h,s,v))
        image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
        cv2.imshow("Image", image_hue_bgr)
        cv2.waitKey(0)










