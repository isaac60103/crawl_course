# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cwb.gov.tw/V7/forecast/week/week.htm')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
all_links = soup.find_all('a')

#for link in all_links:
#	print(link)
	