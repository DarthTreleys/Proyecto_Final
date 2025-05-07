import os
import shutil

SOURCE = "/home"
DEST = "/backup" 

for root, _, files in os.walk(SOURCE):
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(DEST, os.path.relpath(src, SOURCE))

        os.makedirs(os.path.dirname(dst), exist_ok=True) 
        shutil.copy2(src, dst)  

print("Còpia completada.")
