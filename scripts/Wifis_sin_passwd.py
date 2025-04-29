import subprocess
import os

if os.name == 'posix':
    result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY', 'dev', 'wifi'], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    for line in output.split('\n'):
        if line.strip() and 'SSID' not in line:
            parts = line.strip().split()
            ssid = parts[0]
            security = ' '.join(parts[1:])
            if 'WPA' not in security and 'WEP' not in security:
                subprocess.run(['nmcli', 'connection', 'delete', ssid])
                print(f"Red abierta eliminada o bloqueada: {ssid}")

elif os.name == 'nt':
    result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], stdout=subprocess.PIPE)
    output = result.stdout.decode(errors='ignore')

    for line in output.split('\n'):
        if 'SSID' in line:
            ssid = line.split(":", 1)[1].strip()
        if 'Authentication' in line:
            auth = line.split(":", 1)[1].strip()
            if auth.lower() == 'open':
                print(f"Red abierta detectada: {ssid}")
                subprocess.run(['netsh', 'wlan', 'delete', 'profile', f'name="{ssid}"'])
                print(f"Perfil eliminado (si existía): {ssid}")
