import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor

#creating a table
c.execute("""CREATE TABLE customers (
	first_name text,
	last_name text,
	email text
	)""")

#DATYPES (NULL,INTEGER,REAL,TEXT,BLOB)

conn.commit()
conn.close()
