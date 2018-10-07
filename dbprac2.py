import requests
from bs4 import BeautifulSoup,Comment
import datetime

#---------USER INPUT---------#
tv_show = input("Enter tv show: ").replace(' ','_')

#---------CURRENT YEAR---------#
now = datetime.datetime.now()
current_year = now.year

#---------FUNCTION TO GET HTML FROM URL---------#
def getHTML(url):
	response = requests.get(url)
	return BeautifulSoup(response.content, 'lxml')

#---------GETTING TITLE ID OF TV SHOW FROM IMDB SEARCH---------#
imdb_home_page = getHTML("https://www.imdb.com/find?" + tv_show)
find_show_id = imdb_home_page.findAll('td',class_='result_text')
fetch_anchor_tag = find_show_id[0].find('a')
fetch_link = fetch_anchor_tag['href']
show_id = fetch_link[7:17]


#---------GETTING TV SHOW RELEASE DATE IMDB---------#
imdb_page = getHTML("https://www.imdb.com/title/" + show_id)
show_date_year = imdb_page.find(class_='seasons-and-year-nav').find_all('a')
show_year = None
for year in show_date_year:
    if len(year.text) == 4:
        show_year = year.text
        break

#---------DISPLAYING STATUS OF SHOW---------#
if int(show_year) < current_year:
        print("The show has finished streaming all its episodes.")
elif int(show_year) < current_year:
    imdb_episode_url = "https://www.imdb.com/find?" + tv_show + "episodes?year=" + show_year
    imdb_episode_page = getHTML(imdb_episode_url)
    show_date1 = imdb_episode_page.find(attrs={'id': 'nextEpisode'}).find('span')
    show_date2 = imdb_episode_page.find(attrs={'class': 'airdate'})
    air_date = None
    print(show_date1)
    if show_date2:
        print(show_date2)
