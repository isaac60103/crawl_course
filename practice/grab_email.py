# -*- coding: utf-8 -*-
import requests
import re
response = requests.get('https://isaac60103.github.io/crawl_course/practice/email_list.html')
response.encoding = 'utf-8'

pattern = "[A-Za-z0-9._]+@[A-Za-z.]+"
match = re.findall(pattern, response.text)

print(match)
	