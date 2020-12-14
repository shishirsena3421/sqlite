import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor

#inserting record into database
#c.execute("INSERT INTO customers VALUES('Shishir', 'Timilsena', 'shishir.timilsena@gmail.com')")




#inserting multiple records at a time


many_customers =[
			('shristi','timilsena','shristi@gmail.com'),
			('hemkala','timilsena','hemkala@gmail.com'), 
			('ccr','timilsena','ccr@gmail.com'),
		]
c.executemany("INSERT INTO customers VALUES('?','?','?')", many_customers)

print("Record inserted...succesfully")
conn.commit()
conn.close()
