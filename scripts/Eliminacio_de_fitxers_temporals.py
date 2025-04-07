import os
import platform
import sys
### Eliminació de fitxers temporals
directorio = input("Indica el directori") #formulario que especifique directorio (php)
    
for archivo in os.listdir(directorio):
    if archivo.endswith(".tmp") or archivo.endswith(".log"):
        os.remove(os.path.join(directorio, archivo))
        print("Eliminado: " + archivo)
