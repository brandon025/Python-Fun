#! /usr/bin/env python3
import glob
from PIL import Image

# Configs
imagefiles = "images/ic*"
outfile = "out/"

# Convert image to standard
for files in glob.glob(imagefiles):
    im = Image.open(files)
    im = im.resize((128,128)).rotate(270).convert('RGB')
    im.save(files.replace("images/",outfile),'JPEG')
