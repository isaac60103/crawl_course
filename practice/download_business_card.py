# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'https://www.mrcaca.com/'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
all_imgs = soup.find_all('img')


for index, img in enumerate(all_imgs):
#    print(img['src'])
    if 'template' in img['src']: 
        urlretrieve(url+img['src'], img['src'].split('/')[-1])
        break