import requests
from bs4 import BeautifulSoup
response = requests.get("https://isaac60103.github.io/crawl_course/example/beautifulsoup_example.html")
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

print('find the first h1 tag')
print(soup.find("h1"))
print('\n')

print('show the first h1 tag content')
print(soup.find("h1").text)
print('\n')


print('find the first td tag')
print(soup.find("td")) 
print('\n')

print('show the first td tag content')
print(soup.find("td").text) 
print('\n')

print('find all td tag')
print(soup.find_all("td")) 
print('\n')

print('find all tag with class = group1')
print(soup.find_all("", {"class":"group1"})) 
print('\n')

print('show the first div tag with id=id1')
print(soup.find("div", id = "id1").text)
print("\n")


print('find all tag with text= hello_python')
print(soup.find_all(text = "hello_python")) 
print("\n")


print('find third td tag')
print(soup.find_all("td")[2])  
print("\n")

print('find a tag within third td tag')
print(soup.find_all("td")[2].find("a"))
print("\n")

print('find the first a tag and return href')
print(soup.find("a")['href'])   