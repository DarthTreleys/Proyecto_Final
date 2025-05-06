import psutil
import datetime

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

with open("/var/log/sys_monitor.log", "a") as f:
    f.write(log)
    
