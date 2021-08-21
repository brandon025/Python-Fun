#!/usr/bin/env python3
import glob, os
from PIL import Image

# Configs
imagefiles = "/home/student-03-60bbf41681c1/supplier-data/images/*.tiff"
print(glob.glob(imagefiles))

# Convert images
for infile in glob.glob(imagefiles):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im = im.convert('RGB').resize((600,400))
        im.save(file + ".jpeg", "JPEG")
