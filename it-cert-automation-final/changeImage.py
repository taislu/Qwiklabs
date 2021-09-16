#!/usr/bin/env python3

import os
from PIL import Image

images_dir = os.path.expanduser("~") + "/supplier-data/images/"
print(images_dir)

images = os.listdir(images_dir)
print(images)

for afile in images:
  if afile.endswith('.tiff'):
    fn = afile.split('.')
    print(fn)
    infile = images_dir + afile
    outfile = images_dir + fn[0] + '.jpeg'
    #print(infile)
    #print(outfile)
    try:
      with Image.open(infile) as im:
        rgb_im = im.convert('RGB')
        rgb_im.resize((600, 400)).save(outfile, "JPEG")
        print("Convert OK : {}".format(outfile))
    except:
      print("Convert Error : {}".format(infile))
