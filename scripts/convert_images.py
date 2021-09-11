#!/usr/bin/env python3

import os
from PIL import Image

input_dir = os.path.expanduser("~") + "/images/"
output_dir = "/opt/icons/"
print("input_dir: {}".format(input_dir))
print("output_dir: {}".format(output_dir))

images = os.listdir(input_dir)
#print(images)

for filename in images:
  infile = input_dir + filename
  outfile = output_dir + filename
  try:
    with Image.open(infile) as im:
      # print(infile, " : ", im.format, f"{im.size}x{im.mode}")
      # Only RGB can convert to JPEG
      rgb_im = im.convert('RGB')
      rgb_im.rotate(270).resize((128, 128)).save(outfile, "JPEG")
      print("Convert OK : {}".format(filename))
  except:
    print("Convert Error : {}".format(filename))
