from basicColor import *

""":
En este script se corre la clase basiccolor 
creada anteriormente con el path de uma imagen del 
Usuario
"""
path_user = input("Ingrese el path de la imagen: ")
h_value = int(input('ingrese un valor de Hue: '))

imagen_user = basicColor(path_user)
print(imagen_user.displayProperties())
imagen_user.makeBW()


imagen_user.colorize(hue=h_value)