#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
from datetime import datetime

sender = "automation@example.com"
recipient = "student-00-6793cdfff67c@example.com"

body = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage(high_threshold):
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    print("{}: INFO: CPU Usage: {}% : High_Threshold= {}%".format(datetime.now(), usage, high_threshold))
    if usage >= high_threshold:
        subject = "Error - CPU usage is over {}%".format(high_threshold)
        message = emails.generate_email_no_attachment(sender, recipient, subject, body)
        emails.send_email(message)
        print("{}: {}: Alerting Email sent to [{}]".format(datetime.now(), subject, recipient))

def check_disk_usage(disk, low_threshold):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print("{}: INFO: Disk Space Free: {:.2f}% : Low_Threshold= {}%".format(datetime.now(), free, low_threshold))
    if free <= low_threshold:
        subject = "Error - Available disk space is less than {}%".format(low_threshold)
        message = emails.generate_email_no_attachment(sender, recipient, subject, body)
        emails.send_email(message)
        print("{}: {}: Alerting Email sent to [{}]".format(datetime.now(), subject, recipient))

def check_memory_usage(low_threshold):
    """Verifies that there's enough meemory in MB"""
    memory = psutil.virtual_memory()
    free = memory.available >> 20
    print("{}: INFO: Memory Free: {}MB : Low_Threshold= {}MB".format(datetime.now(), free, low_threshold))
    if free <= low_threshold:
        subject = "Error - Available memory is less than {}MB".format(low_threshold)
        message = emails.generate_email_no_attachment(sender, recipient, subject, body)
        emails.send_email(message)
        print("{}: {}: Alerting Email sent to [{}]".format(datetime.now(), subject, recipient))

def check_localhost(hostip):
    localhost = socket.gethostbyname('localhost')
    print("{}: INFO: localhost: {} : Expected= {}".format(datetime.now(), localhost, hostip))
    if localhost != hostip:
        subject = "Error - localhost cannot be resolved to {}".format(hostip)
        message = emails.generate_email_no_attachment(sender, recipient, subject, body)
        emails.send_email(message)
        print("{}: {}: Alerting Email sent to [{}]".format(datetime.now(), subject, recipient))
    #return localhost == "127.0.0.1"



if __name__ == "__main__":
  cpu_high_threshold = 80   # percentage
  #cpu_high_threshold = 3
  check_cpu_usage(cpu_high_threshold)

  disk = '/'
  diskspace_low_threshold = 20  # percentage
  #diskspace_low_threshold = 72   # testOnly
  check_disk_usage(disk, diskspace_low_threshold)
  
  memory_low_threshold = 500  #MegaBytes
  #memory_low_threshold = 6600  #testOnly
  check_memory_usage(memory_low_threshold)
  
  hostip = "127.0.0.1"
  #hostip = "0.0.0.0"      #testOnly
  check_localhost(hostip)

# Set up a cron tab
# which python3
# crontab -e
# * * * * * /usr/bin/python3 /home/student-00-6793cdfff67c/health_check.py >> /home/student-00-6793cdfff67c/health_check.log 2>&1
# crontab -l

