import subprocess

print("Buscando actualizaciones...")
resultado = subprocess.run(["powershell", "-Command", "Get-WindowsUpdate"], capture_output=True, text=True)
print("Actualizaciones disponibles:\n", resultado.stdout)

print("Instalando actualizaciones...")
resultado = subprocess.run(["powershell", "-Command", "Install-WindowsUpdate -AcceptAll -AutoReboot"], capture_output=True, text=True)
print("Instalando actualizaciones:\n", resultado.stdout)

print("Proceso completado.")
