#!/usr/bin/env python3
import psutil
import shutil
import socket
import os
from emails import generate_error_report, send_email

# Check CPU usage
def check_cpu_usage():
    cpu_count = psutil.cpu_percent(interval=1)
    return cpu_count > 80

# Check if theres enough free space on a disk
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

# Check available memory in bytes
def check_available_mem():
    mem_available = psutil.virtual_memory().available/(1024*1024)
    return mem_available < 500

# Check if local host is correctly configured for 127.0.0.1
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'

# Set error message
if check_cpu_usage():
    errormsg = "CPU usage is over 80%"
elif check_disk_usage('/'):
    errormsg = "Available disk space is less than 20%"
elif check_available_mem():
    errormsg = "Available memory is less than 500MB"
elif check_localhost():
    errormsg = "localhost cannot resolve to 127.0.0.1"
else:
    errormsg = None

# Send email if error message
if errormsg:
    print("Maintenance error: " + errormsg)
    try:
        sender = "automation@example.com"
        receiver = "student-03-60bbf41681c1@example.com"
        #receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(errormsg)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    except NameError:
        pass
