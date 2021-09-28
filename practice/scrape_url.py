#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=Riverside%2C+California"

html_text = requests.get(url).text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#print(jobs)
for job in jobs:
  published_date = job.find('span', class_ = 'sim-posted').span.text
  if 'few' in published_date:
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
    location = job.find('ul', class_ = 'top-jd-dtl clearfix').span.text
    skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
    more_info = job.header.h2.a['href']
    
    print(f'Company Name : {company_name}')
    print(f'Location : {location}')
    print(f'Required Skills : {skills}')
    print(f'Published Date : {published_date}')
    print(f'More Info : {more_info}')
    print('')
    
