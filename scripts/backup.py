import os
import subprocess

SOURCE = "/home"
DEST = "/backup"

for root, _, files in os.walk(SOURCE):
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(DEST, os.path.relpath(src, SOURCE))
        dst_dir = os.path.dirname(dst)

        subprocess.run(["sudo", "mkdir", "-p", dst_dir], check=True)
        subprocess.run(["sudo", "cp", "-p", src, dst], check=True)

print("Còpia completada.")
