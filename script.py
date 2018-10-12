from Modules import dates
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#-----------------USER INPUT-----------------#
address= True
while address:
    toaddr = input("Enter your Email address: ").replace(' ','')
    if "@" and "." not in toaddr:
        print(" ----------------------------------------")
        print("| PLEASE ENTER CORRECT EMAIL ADDRESS !!! |")
        print(" ----------------------------------------")
    else:
        address = False

mtvl=True
while mtvl:
    movie_or_tv_show_list = list(map(str,input("Enter Movie or TV show separated by comma(,): ").split(',')))
    if len(movie_or_tv_show_list) == 0:
        print(" -------------------------------------")
        print("| PLEASE ENTER A MOVIE OR TV SHOW !!! |")
        print(" -------------------------------------")
    else:
        mtvl = False

#-------------STORE USER ENTERED DATA IN DATABASE-------------#

#-----------------DATABASE CONNECTION-----------------#
conn = sqlite3.connect('Database/database.db')
c = conn.cursor()

#--------------CREATE TABLE--------------#
def create_table():
    c.execute('''CREATE TABLE DATAS
        (email_id           VARCHAR(255)    NOT NULL,
        movie_or_tvshow     VARCHAR(255)     NOT NULL);''')

create_table()

#--------------INSERT DATA INTO TABLE--------------#
def insert():
    for movie_or_tv_show in movie_or_tv_show_list:
        c.execute(
            '''INSERT INTO DATAS(email_id,movie_or_tvshow) VALUES(?,?)''', (toaddr, movie_or_tv_show))

insert()

#--------------RETRIEVE DATA FROM TABLE--------------#
toaddr_from_db_list = []
movie_or_tv_show_list_from_db = []

def retrieve():
    c.execute('''SELECT email_id FROM DATAS''')
    for row in c.fetchone():
        toaddr_from_db_list.append(row)
    c.execute('''SELECT email_id,movie_or_tvshow FROM DATAS''')
    for row in c.fetchall():
        movie_or_tv_show_list_from_db.append(row[1])

retrieve()

#--------------DELETE THE CREATED TABLE AFTER RETRIEVING DATA--------------#
def drop_table():
    c.execute('''DROP TABLE DATAS''')

drop_table()

#--------------COMMIT AND CLOSE THE DATABASE CONNECTION--------------#
conn.commit()
conn.close()

toaddr_from_db=toaddr_from_db_list[0]

fromaddr = "ur.notifier.bot@gmail.com"
password = "fiernoti1"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr_from_db
msg['Subject'] = "Movie or TV show dates"

for date in movie_or_tv_show_list_from_db:
    date=date.replace(' ', '+')
    body=dates.dates(date)
    msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr_from_db, text)
    server.quit()
    print(" ----------------")
    print("| SUCCESS xD !!! |")
    print(" ----------------")
except Exception as e:
    print(" -----------------------------------")
    print("| BAD RESPONSE FROM MAIL SERVER !!! |")
    print(" -----------------------------------")
