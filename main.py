import dates

#---------USER INPUT---------#
# movie_or_tv_show = input("Enter Movie or TV Show: ").replace(' ', '_')
ll = ['lion', 'opopwers', 'game of throne', 'suits', 'Captain Marvel']
for z in ll:
    z = z.replace(' ', '_')
    dates.dates(z)
