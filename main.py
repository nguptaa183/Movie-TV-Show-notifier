from Modules import dates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# email_address = 'addicniku@gmail.com'
movie_or_tv_show_list = ['lion', 'game of throne', 'suits', 'Captain Marvel']

fromaddr = "ur.notifier.bot@gmail.com"
toaddr = "addicniku@gmail.com"
password = "fiernoti1"
# for data in movie_or_tv_show_list:
#     data = data.replace(' ', '_')
#     msg=dates.dates(data)
# msg ="TV series name: Suits"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Movie or TV shows dates"

body = "Status: The show has finished streaming all its episodes of this year(2018)."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


