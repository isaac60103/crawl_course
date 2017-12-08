import pandas as pd

df = pd.read_csv('RegularSeasonCompactResults.csv')

print('print df head')
print(df.head())

print('print df tail')
print(df.tail())

print('print df shape')
print(df.shape)

print('change columns to list')
print(df.columns.tolist())

print('print statistics on df')
print(df.describe())

print('print max value of all columns')
print(df.max())

print('print Wscore max and Lscore mean')
print(df['Wscore'].max())
print(df['Lscore'].max())


# use iloc(integer-location based indexing for selection by position) to access row

print('print first three row of dataframe')
print(df.iloc[:3])

print('print the row that Wscore is max')
print(df.iloc[[df['Wscore'].argmax()]])

print('print the Lscore that Wscore is max')
df.loc[df['Wscore'].argmax(), 'Lscore']

print('print Wscore that is greater than 150')
df[df['Wscore'] > 150]

print('print Wscore that is greater than 150 and Lscore is less than 100')
df[(df['Wscore'] > 150) & (df['Lscore'] < 100)]

print('get wscore column')
wscore_column = df[['Wscore']]
print(wscore_column.head())

for index, row in df.iterrows():
    print(row)
    if index == 0:
        break
		
print('drop first row of dataframe')
df_drop1 = df.drop(df.index[0])
print(df_drop1.head())

print('drop first three row of dataframe')
df_drop2 = df.drop(df.index[:3])
print(df_drop2.head())

print('after dropping, please remember to reset index')
df_reset_index1 = df_drop1.reset_index(drop=True)
df_reset_index2 = df_drop2.reset_index(drop=True)

print(df_reset_index1.head())
print(df_reset_index2.head())

print('drop first column of dataframe')
df_drop_column = df.drop('Season', axis=1)
print(df_drop_column.head())


print('save panda dataframe as csv file')
df.to_csv('save_pandas_without_index.csv', sep=',', index=False)
df.to_csv('save_pandas_with_index.csv', sep=',')

print('save panda dataframe to html format')
df = df[:10]
df.to_html('save_pandas.html')

print('read html format to panda frame')
df_html = pd.read_html('save_pandas.html', encoding='utf-8')
print(df_html[0])