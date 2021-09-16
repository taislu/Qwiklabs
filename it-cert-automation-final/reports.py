#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  
  report.build([report_title, report_info])

if __name__ == "__main__":
  report_file = "/tmp/processed.pdf"
  title = "Processed Update on " + date.today().strftime("%b %d, %Y")
  print("Report File: {} : Title: {}".format(report_file, title))
  p = [
    "name: Apple<br/>weight: 500 lbs<br/>",
    "name: Avocado<br/>weight: 200 lbs<br/>",
  ]
  add_info = "<br/>".join(p)
  generate_report(report_file, title, add_info)
