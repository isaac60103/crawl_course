# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.ntu.edu.tw/')
response.encoding = 'utf-8'

print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
all_links = soup.find_all('a')

for link in all_links:
    print(link)
	