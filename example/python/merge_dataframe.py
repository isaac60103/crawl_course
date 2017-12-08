import pandas as pd

df1 = pd.read_csv('merge1.csv')
df2 = pd.read_csv('merge2.csv')

print('first dataframe is:')
print(df1.head())

print('second dataframe is:')
print(df2.head())

print('\ninner merge\n')
inner_merge = pd.merge(df1, df2, on='student name')
print(inner_merge.head())


print('\nouter merge\n')
outer_merge = pd.merge(df1, df2, on='student name', how='outer')
print(outer_merge.head())
