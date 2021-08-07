import cv2
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
    def colorize(self,h):
        







imagen_1 = basicColor(r'C:\Users\sngh9\OneDrive\Escritorio\Maestria_Semestre_2\Procesamiento_de_imagenes\Taller_1\cat.png')
imagen_1.displayProperties()
imagen_1.makeBW()