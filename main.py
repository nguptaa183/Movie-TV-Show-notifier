from Modules import dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

address= True
while address:
    toaddr = input("Enter your Email address: ")
    if "@" and "." not in toaddr:
        print("Enter correct address")
        address = False


movie_or_tv_show_list = ['game of thrones']


fromaddr = "ur.notifier.bot@gmail.com"

password = "fiernoti1"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Movie or TV show dates"

for date in movie_or_tv_show_list:
    date=date.replace(' ', '_')
    body=dates.dates(date)
    msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

