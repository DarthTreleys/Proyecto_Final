import os
import requests
from bs4 import BeautifulSoup

###Descarregar imatges d'una pagina web
url = input("Indica la pagina web: ")
carpeta = input("Indica on vols descarregar les imatges: ")

resposta = requests.get(url)
html = resposta.text

soup = BeautifulSoup(html, "html.parser")
imatges = soup.find_all("img")

contador = 1

for imatge in imatges:
    img_url = imgatge.get("src")
    img_url_full = url + "/" + img_url

    nom_fitxer = f"imatge_{contador},jpg"
    url_full = os.path.join(destino, nom_fitxer)

    wget = f'wget -q "{img_url_full}" -0 "{url_full}"'

    resultat = os.system(wget)
    if resultat == 0:
        print(f"Imatge Descarregada: {nom_fitxer}")
        contador += 1
    else:
        print(f"no se pudo descargar: {img_url_full}")
