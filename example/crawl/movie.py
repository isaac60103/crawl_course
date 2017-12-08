# -*- coding: utf-8 -*-
import requests
import pandas as pd
import sqlite3 as sql

response = requests.get('http://www.taipeibo.com/year/2017')
response.encoding = 'utf-8'

# convert html table into dataframe
# note that return type is a list
df_list = pd.read_html(response.text)
df = df_list[0]
print(df)

# connect to db. if db is not exist, it will create a new one
conn = sql.connect("movie_review.db")

# insert dataframe into table. If table exist, it would replace it
df.to_sql("moview_review_table", conn, if_exists="replace")

# query from DB 
df_query = pd.read_sql_query("select * from moview_review_table;", conn).head()
print(df_query.head())


