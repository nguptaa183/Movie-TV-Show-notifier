import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

a = 'fnsdf@jfl.com'
b = ['a', 'b', 'c']


def create_table():
    c.execute('''CREATE TABLE DATAS
         (email_id           VARCHAR(255)    NOT NULL,
         movie_or_tvshow     VARCHAR(255)     NOT NULL);''')


create_table()


def insert():
    for x in b:
        c.execute(
            '''INSERT INTO DATAS(email_id,movie_or_tvshow) VALUES(?,?)''', (a, x))


insert()

email = []
ll = []


def retrieve():
    c.execute('''SELECT email_id FROM DATAS''')
    for row in c.fetchone():
        email.append(row)
    c.execute('''SELECT email_id,movie_or_tvshow FROM DATAS''')
    for row in c.fetchall():
        ll.append(row[1])


retrieve()


def drop_table():
    c.execute('''DROP TABLE DATAS''')


drop_table()

conn.commit()
conn.close()

print(email[0])
print(ll)
