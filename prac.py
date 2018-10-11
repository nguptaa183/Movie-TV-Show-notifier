import sqlite3

l = ['a', 'b', 'c']

#create a data structure
conn = sqlite3.connect('example.db')
c = conn.cursor()

#Create table
c.execute('''Create TABLE if not exists server("sites")''')

#Insert links into table


def data_entry():
    # for item in list_:
    c.execute("INSERT INTO server(sites) VALUES(?)", (l[0],l[1],l[2]))
    conn.commit()


data_entry()  # ==> call the function

#query database
c.execute("SELECT * FROM server")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()
