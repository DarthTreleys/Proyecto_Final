import os
import platform
import sys
import random
import time
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
###Notificacions quan es detecten canvis en una pagina web
web = input("Indica la web que vols vigilar: ")
last_content = requests.get(web).text

while True:
    time.sleep(60)
    current_content = requests.get(web).text
    
    if last_content != current_content:
        print(f"Canvi detectat a la web: {web}")
        last_content = current_content