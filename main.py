from Modules import dates

email_address = 'addicniku@gmail.com'
movie_or_tv_show_list = ['lion', 'opopwers', 'game of throne', 'suits', 'Captain Marvel']
for data in movie_or_tv_show_list:
    data = data.replace(' ', '_')
    dates.dates(data)
