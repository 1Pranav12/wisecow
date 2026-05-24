import psutil
import time

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > CPU_THRESHOLD:
        print("⚠ ALERT: High CPU Usage!")

    if memory > MEM_THRESHOLD:
        print("⚠ ALERT: High Memory Usage!")

    if disk > DISK_THRESHOLD:
        print("⚠ ALERT: High Disk Usage!")

if __name__ == "__main__":
    while True:
        print("\n--- System Health Check ---")
        check_system_health()
        time.sleep(5)