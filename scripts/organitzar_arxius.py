import os
import platform
import sys
import random
import time
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
##Programa que organitzi els arxius en un directori, movent-los a subdirectoris en base la seva extensió
directori = input("Directori: ")

for arxiu in os.listdir(directori):
    ruta = os.path.join(directori, arxiu)
    if os.path.isfile(ruta):
        extension = arxiu.split('.')[-1] 
        if extension == "png":
            os.system("move " +ruta+ r" C:\Users\DEEPGAMING\Pictures")
        if extension == "mp4":
            os.system("move " +ruta+ " C:\\Users\\DEEPGAMING\\Videos")
        if extension == "mp3":
            os.system("move " +ruta+ " C:/Users/DEEPGAMING/Music")