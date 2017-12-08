# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
response = requests.get('http://www.ntu.edu.tw/', headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
all_links = soup.find_all('a')

for link in all_links:
    print(link)
	