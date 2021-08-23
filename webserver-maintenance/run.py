#! /usr/bin/env python3

import os
import requests
import glob
import re

# Configs
descpath = os.path.expanduser('~') + "/supplier-data/descriptions/*.txt"
url = "http://34.123.193.96/fruits/"
descformat = ["name", "weight", "description"]

# Process each fruit and then upload to API on webserver
fruitsdata = []
for infile in glob.glob(descpath):
    fruit = {}
    filename, ext = os.path.splitext(infile)
    filename = os.path.basename(filename) + ".jpeg"
    fruit["image_name"] = filename

    with open(infile) as file:
        count = 0
        for line in file:
            if count == 1:
                line = re.sub("[^0-9]", "", line)
            if count>=3:
                break
            fruit[descformat[count]] = line.strip()
            count+=1
        response = requests.post(url,json=fruit)
        print("POST status: " + str(response.status_code))
