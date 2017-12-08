# -*- coding: utf-8 -*-
import requests
import pandas as pd
import sqlite3 as sql

df = pd.read_csv("./house.csv")
# connect to db. if db is not exist, it will create a new one
conn = sql.connect("house.db")

# insert dataframe into table. If table exist, it would replace it
df.to_sql("house_table", conn, if_exists="replace")

# query from DB 
df_query = pd.read_sql_query("select * from house_table;", conn).head()
print(df_query.head())
