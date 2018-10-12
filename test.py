#---------DEPENDENCIES---------#
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def dates(movie_or_tv_show):

    #---------EXCEPTION HANDLING---------#
    try:
        #---------CURRENT YEAR---------#
        now = datetime.now()
        current_year = now.year

        #---------FUNCTION TO GET HTML FROM URL---------#
        def getHTML(url):
            response = requests.get(url)
            return BeautifulSoup(response.content, 'lxml')

        #---------GETTING TITLE ID OF TV SHOW FROM IMDB SEARCH---------#
        imdb_home_page = getHTML(
            "https://www.imdb.com/find?&q=" + movie_or_tv_show + "&s=all")
        find_show_id = imdb_home_page.findAll('td', class_='result_text')[0]
        fetch_anchor_tag = find_show_id.find(
            'a')  # --- movie_or_tv_show_name---#
        fetch_link = fetch_anchor_tag['href']
        show_id = fetch_link[7:17]

        #---------CHECKING WEATHER IT IS MOVIE OR TVSHOW---------#
        imdb_page = getHTML("https://www.imdb.com/title/" + show_id)
        movie_show_date_year = imdb_page.find(
            'div', class_='subtext').findAll('a')[-1]
        if 'TV Series' in movie_show_date_year.text.strip():
            print("TV series name: " + fetch_anchor_tag.text.strip())
            #---------GETTING TV SHOW RELEASE DATE FROM IMDB---------#
            imdb_page = getHTML("https://www.imdb.com/title/" + show_id)
            show_date_year = imdb_page.find(
                class_='seasons-and-year-nav').find_all('a')
            show_years = []
            for year in show_date_year:
                year = year.text.strip()
                if len(year) == 4:
                    show_years.append(year)
            show_year = show_years[0]
            show_last_year = show_years[1]

            #---------DISPLAYING STATUS OF SHOW---------#
            if int(show_year) < current_year:
                print("Status: The show has finished streaming all its episodes.\n")
            elif (int(show_year) > current_year) and (int(show_year)-1 != int(show_last_year)):
                print("Status: The next season begins in " + show_year + ".\n")
            elif (int(show_year) > current_year) and (int(show_year)-1 == int(show_last_year)):
                imdb_episode_url = "https://www.imdb.com/title/" + \
                    show_id + "episodes?year=" + show_last_year
                imdb_episode_page = getHTML(imdb_episode_url)
                show_date = imdb_episode_page.findAll(class_='airdate')
                airdate = []
                for ad in show_date:
                    ad = ad.text.strip()
                    if len(ad) != 4:
                        airdate.append(ad)
                show_date = airdate[-1]
                if '.' in show_date:
                    show_date = show_date.replace('.', '')
                show_date = datetime.strptime(show_date, '%d %b %Y').date()
                if show_date <= now.date():
                    print("Status: The next season begins in " + show_year + ".\n")
                elif show_date > now.date():
                    print("Status: The next episode airs on " +
                          str(show_date) + ".\n")

            elif int(show_year) == current_year:
                imdb_episode_url = "https://www.imdb.com/title/" + \
                    show_id + "episodes?year=" + show_year
                imdb_episode_page = getHTML(imdb_episode_url)
                show_date = imdb_episode_page.findAll(class_='airdate')
                airdate = []
                for ad in show_date:
                    ad = ad.text.strip()
                    if len(ad) != 4:
                        airdate.append(ad)
                show_date=airdate[-1]
                if '.' in show_date:
                    show_date=show_date.replace('.', '')
                show_date = datetime.strptime(show_date, '%d %b %Y').date()
                if show_date <= now.date():
                    print("Status: The show has finished streaming all its episodes of this year" +
                          "(" + str(current_year) + ").\n")
                elif show_date > now.date():
                    print("Status: The next episode airs on " +
                          str(show_date) + ".\n")

        else:
            print("Movie name: " + fetch_anchor_tag.text.strip())
            #---------GETTING MOVIE RELEASE DATE FROM IMDB---------#
            imdb_page = getHTML("https://www.imdb.com/title/" +
                                show_id + "releaseinfo/")
            movie_country = imdb_page.find(
                'table', class_='subpage_data').findAll('a')
            movie_release_date = imdb_page.find(
                'table', class_='subpage_data').findAll(class_='release_date')
            country_list = [countrylist.text.strip()
                            for countrylist in movie_country]
            release_date_list = [releasedate.text.strip()
                                 for releasedate in movie_release_date]
            final_date = []
            if "India" in country_list:
                x = country_list.index("India")
                y = release_date_list[x]
                final_date.append("India")
                final_date.append(y)

            if len(final_date) == 0:
                if "IN" in country_list:
                    x = country_list.index("IN")
                    y = release_date_list[x]
                    final_date.append("IN")
                    final_date.append(y)

            if len(final_date) == 0:
                if "USA" in country_list:
                    x = country_list.index('USA')
                    y = release_date_list[x]
                    final_date.append('USA')
                    final_date.append(y)

            if len(final_date) == 0:
                final_date.append(country_list[0])
                final_date.append(release_date_list[0])

            movie_date = datetime.strptime(final_date[1], '%d %B %Y').date()
            if movie_date < now.date():
                print("Status: The movie was realeased on " +
                      final_date[1] + ".\n")
            elif movie_date >= now.date():
                print("Status: The movie will realease on " +
                      final_date[1] + ".\n")

    #---------EXCEPTION---------#
    except Exception as e:
        print("\n        ERROR RETRIEVING DATA FROM IMDB\n")
        print(" ------------------------------------------------")
        print("|              POSSIBLE REASONS:                 |")
        print("| --> NO INTERNET CONNECTION                     |")
        print("| --> ENTERED TV SHOW DOESNOT EXIST              |")
        print("| --> BAD RESPONSE FROM IMDB WHILE SCRAPING DATA |")
        print("| --> ABSENCE OF DATA AT THE MOMENT              |")
        print(" ------------------------------------------------")


#---------USER INPUT---------#
movie_or_tv_show = input("Enter Movie or TV Show: ").replace(' ', '+')
dates(movie_or_tv_show)
