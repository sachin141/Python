#!usr/bin/python
from bs4 import BeautifulSoup
import urllib

httpResponse = urllib.request.urlopen("http://www.python.org")
bs=BeautifulSoup(httpResponse, 'lxml')

#find perticular element from html
# data = bs.find('ul', {'class': 'subnav menu'})
# print(data)

#find the forms in html
forms = bs.find_all('form')
print(forms)