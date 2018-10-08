from Modules import dates

#---------USER INPUT---------#
# movie_or_tv_show = input("Enter Movie or TV Show: ").replace(' ', '_')

movie_or_tv_show_list = ['lion', 'opopwers', 'game of throne', 'suits', 'Captain Marvel']
for data in movie_or_tv_show_list:
    data = data.replace(' ', '_')
    dates.dates(data)
