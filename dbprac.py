import requests
from bs4 import BeautifulSoup

tv_show = input("Enter tv show: ")
page = requests.get("https://www.google.co.in/search?q=" + tv_show)
soup=BeautifulSoup(page.content,'html.parser')
imdb_url=None
for x in soup.findAll('cite'):
    if 'https://www.imdb.com/title/' in x.text:
        imdb_url=x.text
print(imdb_url)


