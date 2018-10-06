import requests
from bs4 import BeautifulSoup
import datetime

#---------CURRENT YEAR---------#
now = datetime.datetime.now()
current_year=now.year

#---------FUNCTION TO GET HTML FROM URL---------#
def getHTML(url):
	response = requests.get(url)
	return BeautifulSoup(response.content, 'html.parser')

#---------GETTING IMDB LINK OF TV SHOW FROM GOOGLE---------#
tv_show = input("Enter tv show: ")
google_page = getHTML("https://www.google.co.in/search?q=" + tv_show)
imdb_url=None
for websites in google_page.findAll('cite'):
    if 'https://www.imdb.com/title/' in websites.text:
        imdb_url=websites.text

#---------GETTING TV SHOW RELEASE DATE IMDB---------#
imdb_page = getHTML(imdb_url)
show_date_year = imdb_page.find(attrs={'class': 'seasons-and-year-nav'}).find_all('a')
show_year=None
for year in show_date_year:
    if len(year.text)==4:
        show_year=year.text
        break

#---------DISPLAYING STATUS OF SHOW---------#
# if int(show_year) > current_year:
#     print("The next season begins in " + show_year + ".")
if int(show_year) < current_year:
    print("The show has finished streaming all its episodes.")
else:
    imdb_episode_url=imdb_url + "episodes?year=" + show_year
    imdb_episode_page = getHTML(imdb_episode_url)
    show_date2 = imdb_episode_page.find(attrs={'id': 'nextEpisode'}).find('span')
    show_date2 = imdb_episode_page.find(attrs={'class': 'airdate'})
    air_date=None
    if show_date2:
        print(show_date2)

        

        # print("The next episode airs on ")


