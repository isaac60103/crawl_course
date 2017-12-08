# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

payload = {
"StartStation":"977abb69-413a-4ccf-a109-0272c24fd490",
"EndStation":"a7a04c89-900b-4798-95a3-c01c455622f4",
"SearchDate":"2017/12/11",
"SearchTime":"12:00",
"SearchWay":"DepartureInMandarin",
"RestTime":"",
"EarlyOrLater":""
}

 
response = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = payload)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

print(len(soup.find_all("td",class_="column1")))