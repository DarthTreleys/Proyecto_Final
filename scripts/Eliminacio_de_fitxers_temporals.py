import os
import platform
import sys
import random
import time
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
### Eliminació de fitxers temporals
directorio = input("Indica el directori") #formulario que especifique directorio (php)
    
for archivo in os.listdir(directorio):
    if archivo.endswith(".tmp") or archivo.endswith(".log"):
        os.remove(os.path.join(directorio, archivo))
        print("Eliminado: " + archivo)
