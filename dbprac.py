import requests
from bs4 import BeautifulSoup

#---------FUNCTION TO GET HTML FROM URL---------#
def getHTML(url):
	response = requests.get(url)
	return BeautifulSoup(response.content, 'html.parser')

#---------GETTING IMDB LINK OF TV SHOW FROM GOOGLE---------#
tv_show = input("Enter tv show: ")
page = getHTML("https://www.google.co.in/search?q=" + tv_show)
imdb_url=None
for websites in page.findAll('cite'):
    if 'https://www.imdb.com/title/' in websites.text:
        imdb_url=websites.text
print(imdb_url)

#---------GETTING IMDB LINK OF TV SHOW FROM GOOGLE---------#
# data['poster'] = html.find(attrs={'class': 'poster'}).find('img')['src']

