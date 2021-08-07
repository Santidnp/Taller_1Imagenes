from basicColor import *

path_user = input("Ingrese el path de la imagen: ")

imagen_user = basicColor(path_user)
print(imagen_user.displayProperties())
imagen_user.makeBW()

h_value = int(input('ingrese un valor de Hue: '))
imagen_user.colorize(hue=h_value)