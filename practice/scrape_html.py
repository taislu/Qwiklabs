#!/usr/bin/env python3
from bs4 import BeautifulSoup

with open('scrape_home.html', 'r') as html_file:
  content = html_file.read()
  #print(content)

  soup = BeautifulSoup(content, 'lxml')
  #print(soup.prettify())

  course_cards = soup.find_all('div', class_='card') # class is a reserved word

  for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]

    print(f'{course_name} costs {course_price}')


  #tags = soup.find('h5')  # search the 1st matching element
  #tags = soup.find_all('h5') # returns a list
  #print(tags)
  #for elem in tags:
    #print(elem.text)
