#! /usr/bin/env python3
import os
import requests

# Configs
fbdir = "/data/feedback/"
url = "http://34.121.89.5/feedback/"
fbformat = ["title", "name", "date", "feedback"]

fbfiles = os.listdir(fbdir)

# Process each feedback file and POST to web API on GCLOUD
for fbfile in fbfiles:
    with open(fbdir + fbfile) as file:
        data = {}
        count = 0
        for line in file:
            data[fbformat[count]] = line.strip()
            count+=1
        response = requests.post(url,json=data)
        print("POST status: " + str(response.status_code))
