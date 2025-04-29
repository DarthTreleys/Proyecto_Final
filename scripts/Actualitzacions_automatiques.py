import subprocess
import os

so = platform.system()
if so="Linux":
print("Actualizando lista de paquetes...")
subprocess.run(["sudo", "apt", "update"], check=True)

print("Instalando actualizaciones disponibles...")
subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

print("Limpieza de paquetes innecesarios...")
subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)

print("Actualización completada con éxito.")

elif so="Windows":
print("Buscando actualizaciones...")
resultado = subprocess.run(["powershell", "-Command", "Get-WindowsUpdate"], capture_output=True, text=True)
print("Actualizaciones disponibles:\n", resultado.stdout)

print("Instalando actualizaciones...")
resultado = subprocess.run(["powershell", "-Command", "Install-WindowsUpdate -AcceptAll -AutoReboot"], capture_output=True, text=True)
print("Instalando actualizaciones:\n", resultado.stdout)

print("Proceso completado.")

else: 
print("Lo sentimos, su sistema no es compatible con este script.")
