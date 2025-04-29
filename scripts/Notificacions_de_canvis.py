import time
import requests

web = input("Indica la web a vigilar: ").strip()

try:
    last_content = requests.get(web).text
except Exception as e:
    print(f"Error al accedir a la web: {e}")
    exit(1)

while True:
    time.sleep(60)
    try:
        current_content = requests.get(web).text
        if current_content != last_content:
            print(f"Canvi detectat a la web: {web}")
            last_content = current_content
    except Exception as e:
        print(f"Error al tornar a accedir a la web: {e}")
