# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'https://www.thsrc.com.tw/tw/TimeTable/SearchResult'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
all_imgs = soup.find_all('img')

for index, img in enumerate(all_imgs):
    if index!=0:
        print(img['src'])
        print('https://www.thsrc.com.tw'+img['src'])
        urlretrieve('https://www.thsrc.com.tw'+img['src'], img['src'].split('/')[-1])