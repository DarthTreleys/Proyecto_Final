import os
import platform
import sys
import csv
### Creacio d'usuaris amb un csv
with open('usuaris.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['username']
        full_name = row['full_name']
        password = row['password']
        print(f"Cal crear l'usuari: {username}, Nom complet: {full_name}, Contrasenya: {password}")
