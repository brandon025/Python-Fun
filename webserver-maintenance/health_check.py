#!/usr/bin/env python3
import psutil
import shutil

# Check CPU usage
def check_cpu_usage:
    cpu_count = psutil.cpu_percent(interval=1)
    return usage < 80

# Check if theres enough free space on a disk
def check_disk_usage(disk):
    du = shutil.disk_uage(disk)
    free = du.free / du.total * 100
    return free < 20

# Check available memory in bytes
def check_available_mem():
    mem_available = psutil.virtual_memory().available/(1024*1024)
    return available_memory < 500

# Check if local host is correctly configured for 127.0.0.1
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'

if check_cpu_usage():
    errormsg = "CPU usage is over 80%"
elif check_disk_uage('/'):
    errormsg = "Available disk space is less than 20%"
elif check_available_mem():
    errormsg = "Available memory is less than 500MB"
elif check_localhost():
    error_message = "localhost cannot resolve to 127.0.0.1"
else:
    pass
