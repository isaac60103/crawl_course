# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://isaac60103.github.io/crawl_course/example/beautifulsoup_example.html')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
all_tds = soup.find_all('td', re.compile('group[0-9]'))

for td in all_tds:
    print(td)

	