import subprocess
import os

    result = subprocess.run(["sudo", "nmcli", "-f", "SSID,SECURITY", "dev", "wifi"], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    for line in output.split('\n'):
        if line.strip() and 'SSID' not in line:
            parts = line.strip().split()
            ssid = parts[0]
            security = ' '.join(parts[1:])
            if 'WPA' not in security and 'WEP' not in security:
                subprocess.run(["nmcli", "connection", "delete", ssid])
                print(f"Red abierta eliminada o bloqueada: {ssid}")

