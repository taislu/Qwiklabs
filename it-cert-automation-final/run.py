#! /usr/bin/env python3

import os
import locale
import requests

input_dir = os.path.expanduser("~") + "/supplier-data/descriptions/"
#print(input_dir)

txt_files = os.listdir(input_dir)
#print(txt_files)

columns = ["name", "weight", "description", "image_name"]

url = "http://localhost/fruits/"

for fn in txt_files:
  infile = input_dir + fn
  file = fn.split('.')
  print(infile)

  with open(infile, 'r') as f:
    data = f.readlines()

  a_dict = {}
  a_dict[columns[0]] = data[0].strip()
  weight = data[1].strip()
  a_dict[columns[1]] = locale.atoi(weight.strip("lbs"))
  a_dict[columns[2]] = data[2].strip()
  a_dict[columns[3]] = file[0] + '.jpeg'
  print(a_dict)

  response = requests.post(url, json=a_dict)
  print(response.status_code)
     
