import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.google.co.in/search?q=suits')
soup=BeautifulSoup(page,'html.parser')
for x in soup.findAll('cite'):
    print(x)

