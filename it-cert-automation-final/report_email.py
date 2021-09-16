#!/usr/bin/env python3

import reports
import emails
import os
from datetime import date

def get_report_data():
  input_dir = os.path.expanduser("~") + "/supplier-data/descriptions/"
  #print(input_dir)

  txt_files = os.listdir(input_dir)
  #print(txt_files)

  plist = []
  for fn in txt_files:
    infile = input_dir + fn
    #print(infile)
    
    with open(infile, 'r') as f:
      data = f.readlines()

    pstr = "name: {}<br/>weight: {}<br/>".format(data[0].strip(), data[1].strip())
    plist.append(pstr)
  #plist.sort()
  #print(plist)
  return(plist)

if __name__ == "__main__":
  plist = get_report_data()
  print(plist)
  report_file = "/tmp/processed.pdf"
  title = "Processed Update on " + date.today().strftime("%b %d, %Y")
  add_info = "<br/>".join(plist)
  print(add_info)
  reports.generate_report(report_file, title, add_info)
  print("Report File: {} : Title: {}".format(report_file, title))

  sender = "automation@example.com"
  recipient = "student-00-6793cdfff67c@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, recipient, subject, body, report_file)
  emails.send_email(message)
  print("Email sent with attachment !!!")
