import cv2
import numpy as np
import sys
import os
class basicColor():
    
    def __init__(self,path):
        """Se inicializa la clase:
        se pide un path del lugar donde esta la imagen y despues se almacena en opencv
        """

        self.path = path
        self.image = cv2.imread(path)

    def displayProperties(self):
        """
        Recibe:la imagen guaradada del metodo anterior
        Imprime en Pantalla : Los Pixeles y número de canales de la imagen
        """
        Pixeles = self.image.shape[0]*self.image.shape[1]
        canales = self.image.shape[2]
        print(f'canales : {canales}')
        print(f'píxeles:{Pixeles}')

    def makeBW(self):
        """
        Recibe: la imagen guardada
        Imprime en pantalla : La imagen binaria con el metodo de Otsu
        """
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) # Se debe tener primero la imagen en grises
        ret, imgOstu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Image", imgOstu)
        cv2.waitKey(0)
    def colorize(self,hue):
        """
        Recibe: la imagen guardad
        Imprime en pantalla: la imagen en BGR con el canal h escogido por el usuario
        """
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(image_hsv)
        h = hue*np.ones_like(h)
        image_hue = cv2.merge((h,s,v))
        image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
        cv2.imshow("Image", image_hue_bgr)
        cv2.waitKey(0)










