import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor


c.execute("SELECT rowid, * FROM customers")    #for primary key in id; rowid is used here

items = c.fetchall()

for i in items:
	print(i)











conn.commit()
conn.close()
