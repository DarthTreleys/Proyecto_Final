import os
import platform
import sys
import random
import time
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
### Crear copies de seguretat
SOURCE = input("Directori base de la copia de seguretat:")
DEST = input("Directori on es guardara la copia de seguretat:")

for root, _, files in os.walk(SOURCE):
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(DEST, os.path.relpath(src, SOURCE))

print("Còpia completada.")