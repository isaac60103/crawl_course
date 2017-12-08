import requests
from bs4 import BeautifulSoup
import re

response = requests.get("http://yp.518.com.tw/service-life.html?ctf=10")

soup = BeautifulSoup(response.text, 'html.parser')
all_lis = soup.find_all("li",class_="comp_loca", text = re.compile("高雄"))

for li in all_lis:
    print(li)
