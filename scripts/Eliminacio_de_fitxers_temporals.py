import os

directorio = input("Indica el directori: ").strip()

# Validar que el directorio existe
if not os.path.isdir(directorio):
    print("El directori indicat no existeix.")
    exit(1)

for archivo in os.listdir(directorio):
    ruta = os.path.join(directorio, archivo)
    if os.path.isfile(ruta) and (archivo.endswith(".tmp") or archivo.endswith(".log")):
        try:
            os.remove(ruta)
            print("Eliminado:", archivo)
        except Exception as e:
            print(f"No se pudo eliminar {archivo}: {e}")
