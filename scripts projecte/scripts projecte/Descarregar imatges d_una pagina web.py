import os
import platform
import sys
import random
import time
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
###Descarregar imatges d'una pagina web
url = input("Indica la pagina web: ")
carpeta = input("Indica on vols descarregar les imatges")

soup = BeautifulSoup(requests.get(url).text, "html.parser")
for i, img in enumerate(soup.find_all("img")):
    img_url = img.get("src", "").strip()
    if img_url and not img_url.startswith("http"):
        img_url = url + img_url
    
    img_resposta = requests.get(img_url, stream=True)
    with open(os.path.join(carpeta, f"imatge_{i}.jpg"), "wb") as f:
        for chunk in img_resposta.iter_content(1024):
            f.write(chunk)
    print(f"Descarregada: {img_url}")