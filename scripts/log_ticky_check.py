#!/usr/bin/env python3
import sys
import re
import operator
import csv

def error_search(log_file):
  # error messages count, sorted from most to least
  errs = {}
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for line in file:
      #print("Log: "+line.strip())
      pattern = r"ticky: ERROR ([\w  ']*) "
      msg = re.search(pattern, line.strip())
      if msg is not None:
        errs[msg.group(1)] = errs.get(msg.group(1), 0) + 1

  #print(errs)
  errs_sorted = sorted(errs.items(), key=operator.itemgetter(1), reverse=True)
  #print(errs_sorted)
  return errs_sorted

def user_search(log_file):
  # Username, InfoCount, ErrorCount && Sorted by Username
  usr_info = {}
  usr_errs = {}
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for line in file:
      #print("Log: "+line.strip())
      patternI = r"ticky: INFO [\w [#\d]*] \(([\w.]*)\)"
      #patternR = r"ticky: ERROR: [\w ']* \((\w+)\)"
      patternR = r"ticky: ERROR [\w ']* \(([\w.]*)\)"
      msgI = re.search(patternI, line.strip())
      #print(msgI)
      if msgI is not None:
        usr_info[msgI.group(1)] = usr_info.get(msgI.group(1), 0) + 1
        #usr_info[msgI[1]] = usr_info.get(msgI[1], 0) + 1
        continue
      msgR = re.search(patternR, line.strip())
      if msgR is not None:
        usr_errs[msgR.group(1)] = usr_errs.get(msgR.group(1), 0) + 1
        #usr_errs[msgR[1]] = usr_errs.get(msgR[1], 0) + 1
        continue
      print("Not Matching *** : " + line.strip())

  print(usr_info)
  print(usr_errs)
  usrnamesI = list(usr_info.keys())
  usrnamesR = list(usr_errs.keys())
  usrnames = set( usrnamesI + usrnamesR )
  #usrnames = set( list(usr_info.keys()) + list(usr_errs.keys()) )
  print(usrnames)
  usrnames_sorted = sorted(usrnames)
  print(usrnames_sorted)
  return_list = []
  for name in usrnames_sorted:
    cntInfo = 0
    cntErrs = 0
    if name in usrnamesI:
      cntInfo = usr_info[name]
    if name in usrnamesR:
      cntErrs = usr_errs[name]
    return_list.append([name, str(cntInfo), str(cntErrs)])
  print(return_list)
  
  return return_list

def write_csv(filename, header, data):
  with open(filename, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)


if __name__ == "__main__": # run the script itself
  log_file = "log_syslog.txt"
  errs_list = error_search(log_file)
  write_csv('error_message.csv', ['Error', 'Count'], errs_list)
  usrcount_list = user_search(log_file)
  write_csv('user_statistics.csv', ['Username', 'INFO', 'ERROR'], usrcount_list)
  print("DONE ... Check OUTPUT CSV Files !")
  sys.exit(0)
