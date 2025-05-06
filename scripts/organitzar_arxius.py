import os
import platform
import sys
##Programa que organitzi els arxius en un directori, movent-los a subdirectoris en base la seva extensió
directori = "/home"

if os.name="nt":
for arxiu in os.listdir(directori):
    ruta = os.path.join(directori, arxiu)
    if os.path.isfile(ruta):
        extension = arxiu.split('.')[-1] 
        if extension == "png":
            os.system("move " +ruta+ " ~\\Pictures")
        if extension == "mp4":
            os.system("move " +ruta+ "~\\Videos")
        if extension == "mp3":
            os.system("move " +ruta+ "~\\Music")
