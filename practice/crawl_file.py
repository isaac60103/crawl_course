# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url='https://www.go100.com.tw/exam_download_3.php'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
all_as = soup.find_all('a')

for index, a_tag in enumerate(all_as):
    if 'pdf' in a_tag['href']: 	
#	    print(a_tag['href'])
        urlretrieve(a_tag['href'], 'file_tmp.pdf')
        break
