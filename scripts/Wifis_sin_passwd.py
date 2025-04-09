#hay que cronar el script (*/5 * * * * /usr/bin/python3 /ruta/a/Wifis_sin_passwd.py)
import subprocess

# Ejecutar el comando para listar redes Wi-Fi con sus niveles de seguridad
result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY', 'dev', 'wifi'], stdout=subprocess.PIPE)
output = result.stdout.decode()

# Procesar la salida para encontrar redes abiertas (sin WPA/WEP)
for line in output.split('\n'):
    if line.strip() and 'SSID' not in line:
        parts = line.strip().split()
        ssid = parts[0]
        security = ' '.join(parts[1:])
        if 'WPA' not in security and 'WEP' not in security:
            # Intentar borrar la conexión para evitar reconexión futura
            subprocess.run(['nmcli', 'connection', 'delete', ssid])
            print(f"Red abierta eliminada o bloqueada: {ssid}")
