import os
import platform
import sys
import time
#Crear puntos de Restauración

SOURCE = input("Indica la carpeta que vols incloure en el punt de restauració: ").strip()
DEST = input("Indica la carpeta on guardaràs el punt de restauració: ").strip()

# Assegura que la carpeta de destí existeix
os.makedirs(DEST, exist_ok=True)

# Crea un nom de fitxer únic amb la data
backup_name = f"backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"
backup_path = os.path.join(DEST, backup_name)

# Executa la comanda tar per fer la còpia de seguretat
print("Creant el punt de restauració... Això pot trigar uns minuts.")
result = subprocess.run(["tar", "-czvf", backup_path, SOURCE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Comprova si la còpia s’ha fet correctament
if result.returncode == 0:
    print(f"Punt de restauració creat: {backup_path}")
else:
    print("Hi ha hagut un error al crear el punt de restauració.")
    print(result.stderr.decode())
