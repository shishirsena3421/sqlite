import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor


c.execute("SELECT  * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 2 ")

items = c.fetchall()

for i in items:
	print(i)


conn.commit()
conn.close()
