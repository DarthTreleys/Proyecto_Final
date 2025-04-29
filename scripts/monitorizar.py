import psutil
import datetime

so=platform.system()

if so="Linux"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disk = psutil.disk_usage('/')

log = (
    f"[{now}]\n"
    f"CPU: {cpu}%\n"
    f"RAM: {ram.percent}% ({ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB)\n"
    f"DISK: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)\n"
    "--------------------------\n"
)

if so="Linux":
with open("/var/log/sys_monitor.log", "a") as f:
    f.write(log)
    
elif so="Windows":
# Ruta al archivo log dentro de la carpeta "Documents" del usuario
log_path = os.path.expanduser("~\\Documents\\sys_monitor.log")
# Asegurarse de que el directorio exista
os.makedirs(os.path.dirname(log_path), exist_ok=True)
with open(log_path, "a") as f:
    f.write(log)
