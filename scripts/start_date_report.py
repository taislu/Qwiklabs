#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees

def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def preprocess(start_date):
    a_dict = {}
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])  # skip column names
    #print("data:{}".format(data[1:]))

    for row in reader:
        #print("row:{}".format(row))
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if row_date < start_date:
            continue
        name = "{} {}".format(row[0], row[1])
        #print("Sdate:{} name:{}".format(row[3], name))
        if row[3] in a_dict.keys():
            a_dict[row[3]] += [name]
        else:
            a_dict[row[3]] = [name]
    #print(a_dict)

    return a_dict

def list_newer_with_dict(start_date):
    startdate_dict = preprocess(start_date)
    #key: start_date 
    #value: a list of employee names 
    #print(startdate_dict)
    
    for sdate, employee_list in sorted(startdate_dict.items()):
        d_obj = datetime.datetime.strptime(sdate, '%Y-%m-%d')
        print("Started on {}: {}".format(d_obj.strftime("%b %d, %Y"), employee_list))


def main():
    start_date = get_start_date()
    list_newer_with_dict(start_date)
    #list_newer(start_date)

if __name__ == "__main__":
    main()
