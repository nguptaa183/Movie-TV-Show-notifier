from Modules import dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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


fromaddr = "ur.notifier.bot@gmail.com"
password = "fiernoti1"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Movie or TV show dates"

for date in movie_or_tv_show_list:
    date=date.replace(' ', '+')
    body=dates.dates(date)
    msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(" ----------------")
    print("| SUCCESS xD !!! |")
    print(" ----------------")
except Exception as e:
    print(" -----------------------------------")
    print("| BAD RESPONSE FROM MAIL SERVER !!! |")
    print(" -----------------------------------")
