import psutil
import datetime

# Obtener la hora actual
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Obtener estadísticas del sistema
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disk = psutil.disk_usage('/')

# Crear el log
log = (
    f"[{now}]\n"
    f"CPU: {cpu:.1f}%\n"
    f"RAM: {ram.percent:.1f}% ({ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB)\n"
    f"DISK: {disk.percent:.1f}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)\n"
    "--------------------------\n"
)

log_path = "/var/log/sys_monitor.log"

with open(log_path, "a") as f:
    f.write(log)

