# coding: utf-8
import requests
import json
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql
from time import sleep

#小心requrest太過頻繁IP會被對方封鎖
res1 = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170901&stockNo=2330')
sleep(5)
res2 = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20171001&stockNo=2330')

json1 = res1.json()
json2 = res2.json()

header = json1['fields']

data = json1['data']
data.extend(json2['data'])

df = pd.DataFrame.from_records(data, columns=header)

#日期轉換西元年、重複執行這裡會讓日期溢位
for i, row in df.iterrows():
    #print(row[0])
    strDate = row[0]
    DateArr = strDate.split("/")
    DateArr[0] = str(int(DateArr[0])+1911)
    DateArr[1] = str(int(DateArr[1]))
    DateArr[2] = str(int(DateArr[2]))
    #df.set_value(i,'日期','/'.join(DateArr))
    df.loc[i, '日期'] = '/'.join(DateArr)

#存成CSV
df.to_csv('fp_demo.csv', sep=',', encoding='utf-8-sig', index=False)

#存入SqLite
#連線至sqlite檔案，若無該檔案sql，則會建立一個新的
#conn = sql.connect("twse.db")
#將Dataframe資料寫入sql檔中的'demo1'表中，無該資料表則會自動建立
#df.to_sql("demo1", conn, if_exists="replace")


print('Done!')

