# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://edition.cnn.com/')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())	