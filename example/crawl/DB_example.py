import sqlite3

conn = sqlite3.connect('test.db')

first_number = 20 
second_number = 10

sqlstr = "insert into test_table (field1, field2) values({},{});".format(first_number,second_number)
conn.execute(sqlstr)
conn.commit()

sqlstr = "select * FROM test_table;"
cursor = conn.execute(sqlstr)
for row in cursor:
	print('{} {} {}'.format(row[0], row[1], row[2]))

