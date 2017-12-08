# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.nccu.edu.tw/')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
all_links = soup.find_all('h1')

for link in all_links:
	print(link)
	