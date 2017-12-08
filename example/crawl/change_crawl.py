# -*- coding: utf-8 -*-
import requests
import hashlib
import os
from bs4 import BeautifulSoup

url = 'http://www.ntu.edu.tw/'
response = requests.get(url)
response.encoding = 'utf-8'
sig = hashlib.md5(response.text.encode('utf-8')).hexdigest()
old_sig=''

if os.path.exists('eq_sig.txt'):
    with open('eq_sig.txt', 'r') as fp:
        old_sig = fp.read()
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)
else:
    with open('eq_sig.txt', 'w') as fp:
        fp.write(sig)

if sig == old_sig:
    print('data not update, don\'t need parse data')
    exit()	
else:
    print('data update! Start analysis data')
    
    '''
	use beautifulsoup or regular expression to analysis data ... ....
    '''	