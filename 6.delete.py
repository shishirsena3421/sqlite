import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor


c.execute("DELETE  from customers WHERE last_name = 'Sharma'")   



conn.commit()
conn.close()
