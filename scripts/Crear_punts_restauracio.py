import os
import shutil
from datetime import datetime

SOURCE = input("Indica la carpeta que vols incloure en el punt de restauració: ").strip()
DEST = input("Indica la carpeta on guardaràs el punt de restauració: ").strip()

# Validación de rutas
if not os.path.isdir(SOURCE):
    print("La carpeta d'origen no existeix.")
    exit(1)

# Crear la carpeta destino si no existe
os.makedirs(DEST, exist_ok=True)

# Crear nombre de archivo de copia de seguridad
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_base_name = os.path.join(DEST, f"backup_{timestamp}")

# Crear archivo .tar.gz (funciona en Linux y Windows)
print("Creant el punt de restauració... Això pot trigar uns minuts.")

try:
    archive_path = shutil.make_archive(backup_base_name, 'gztar', root_dir=SOURCE)
    print(f"Punt de restauració creat: {archive_path}")
except Exception as e:
    print("Hi ha hagut un error al crear el punt de restauració.")
    print(e)
