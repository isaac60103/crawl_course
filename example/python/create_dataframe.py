import pandas as pd

my_list = [('isaac', 60, 50),('julie', 90, 70),('alex', 30, 40)]
header = ['name','math score','english score']
df_from_list = pd.DataFrame.from_records(my_list, columns=header)

print('create dataframe from list')
print(df_from_list)

my_dict = \
[{'name':'isaac', 'math score':60,'english score':50},
{'name':'julie', 'math score':90,'english score':70},
{'name':'alex', 'math score':30,'english score':40}
]
df_from_dict = pd.DataFrame(my_dict, columns=['name', 'math score', 'english score'])
print('create dataframe from dict')
print(df_from_dict)


