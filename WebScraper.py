'''
Python Webscraper using https://www.geeksforgeeks.org/python-web-scraping-tutorial/
Author: Jayson Waters
Date: 12/2/2022
'''
import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

''' 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

#----------------------------------------
# print request object (prints the url)
print(r.url)
   
# print status code
print(r.status_code)
'''
#----------------------------------------
#Python BeautifulSoup Parsing HTML

# check status code for response received
# success code - 200
'''
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
'''
#----------------------------------------
#Extracting the title of the page

# Parsing the HTML
'''
soup = BeautifulSoup(r.content, 'html.parser')
 
# Getting the title tag
print(soup.title)
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 
# use the child attribute to get
# the name of the child tag
'''
#----------------------------------------
#Finding Elements by class

# Parsing the HTML
'''
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)
'''
#----------------------------------------
#Finding Elements by class
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)
'''
#----------------------------------------
#Finding Elements by ID
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Finding by id
s = soup.find('div', id= 'main')
 
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
 
# All the li under the above ul
content = leftbar.find_all('li')
 
print(content)
'''
#----------------------------------------
#Extracting Text from the tags
#Removing the tags from the content of the page
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='entry-content')
 
lines = s.find_all('p')
 
for line in lines:
    print(line.text)
 '''
#----------------------------------------
#Removing the tags from the content of the leftbar
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Finding by id
s = soup.find('div', id= 'main')
 
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
 
# All the li under the above ul
lines = leftbar.find_all('li')
 
for line in lines:
    print(line.text)

'''
#----------------------------------------
#Extracting Links
#Python BeautifulSoup Extracting Links
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))
'''
#----------------------------------------
#Extracting Image Information
#Python BeautifulSoup Extract Image 
'''
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)
'''
#----------------------------------------
#Scraping multiple Pages -part 1
'''
URL = 'https://www.geeksforgeeks.org/page/1/'
 
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')
 
titles = soup.find_all('div',attrs = {'class','head'})
 
print(titles[4].text)
'''
#Scraping multiple Pages -part 2
#Get the titles of all the articles by just sandwiching those lines with a loop
'''
URL = 'https://www.geeksforgeeks.org/page/'
 
for page in range(1, 10):
 
    req = requests.get(URL + str(page) + '/')
    soup = BeautifulSoup(req.text, 'html.parser')
 
    titles = soup.find_all('div', attrs={'class', 'head'})
 
    for i in range(4, 19):
        if page > 1:
            print(f"{(i-3)+page*15}" + titles[i].text)
        else:
            print(f"{i-3}" + titles[i].text)
'''

#Looping through a list of different URLs
'''
URL = ['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']
 
for url in range(0,2):
    req = requests.get(URL[url])
    soup = BeautifulSoup(req.text, 'html.parser')
 
    titles = soup.find_all('div',attrs={'class','head'})
    for i in range(4, 19):
        if url+1 > 1:
            print(f"{(i - 3) + url * 15}" + titles[i].text)
        else:
            print(f"{i - 3}" + titles[i].text)
'''
#----------------------------------------
#Saving Data to CSV
#Python BeautifulSoup saving to CSV

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
 
soup = BeautifulSoup(req.text, 'html.parser')
 
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)
#----------------------------------------
