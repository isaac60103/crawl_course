# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

payload = {
"FromStationName":"1008",
"ToStationName":"1025",
"TrainClass":"2",
"searchdate":"2017-12-06",
"FromTimeSelect":"0000",
"ToTimeSelect":"2359",
"Timetype":"1"
}

response = requests.post('http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx', data=payload)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
train_info = soup.find_all('script')
print(train_info)
