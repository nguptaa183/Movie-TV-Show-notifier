import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb')

db.close()



# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE datas(id INTEGER PRIMARY KEY, email TEXT unique, name TEXT)
''')
db.commit()
