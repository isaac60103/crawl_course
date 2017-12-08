import requests
from time import sleep
#Set URL.
url = 'http://app.twse.com.tw/ch/trading/fund/T86/T86.php'

#Set post data.
payload = {'download': '', 'qdate': '106/10/06', 'select2': '01', 'sorting': 'by_issue'}

max_Retry = 3  #set times to retry when connection got errors.
retry = 1

while retry <= max_Retry:
    try:
        #Request the data with the payload.
        res = requests.post(url, data=payload)

        print(res.text)

        #You also can do something using BeautifulSoup if the resource is in html form.

        #Break the loop when finished the job.
        break

    except Exception as e:
        #If connection is failed.
        retry += 1
        print("I got an error: ", e)
        continue