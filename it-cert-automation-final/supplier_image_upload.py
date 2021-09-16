#!/usr/bin/env python3

import requests
import os

images_dir = os.path.expanduser("~") + "/supplier-data/images/"
#print(images_dir)

images = os.listdir(images_dir)
#print(images)

url = "http://localhost/upload/"

for afile in images:
  if afile.endswith('.jpeg'):
    infile = images_dir + afile
    print(infile)
    with open(infile, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      print(r.status_code)
