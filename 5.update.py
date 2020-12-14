import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor() #creating a cursor


c.execute("UPDATE customers SET last_name = 'Sharma' WHERE rowid = 2")   




conn.commit()
conn.close()
