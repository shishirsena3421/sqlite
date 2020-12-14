import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor



c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")    #Arranging in descending order



#c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")    #Arranging in Ascending order

#c.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")    #Arranging in alphabetical descending order for first name



items = c.fetchall()

for i in items:
	print(i)











conn.commit()
conn.close()
