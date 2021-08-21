#!/usr/bin/env python3
import requests
import glob
# This example shows how a file can be uploaded using
# The Python Requests module

# Configs
url = "http://localhost/upload/"
imagepath = glob.glob("/home/student-03-60bbf41681c1/supplier-data/images/*.jpeg")

for image in imagepath:
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
