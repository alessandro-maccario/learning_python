"""Day 46: Music Time Machine Project"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import pandas as pd

################
### CONSTANT ###
################

URL = "https://www.billboard.com/charts/hot-100/"
SONG_TITLE_CLASS = "c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025"
HEADER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
############
### MAIN ###
############

# Request the date to which the user would like to go back to to collect the music information
date = input(
    "Which year do you want to travel to? Type the data in the following format: YYYY-MM-DD: "
)

# add the date to the url
url_date_to_search = URL + date + "/"

try:
    # request the billboard website as a text and then parse it with BeautifulSoup
    billboard_website = requests.get(
        url_date_to_search,
        headers={"User-Agent": HEADER},
    ).text
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

# instantiate the beautifulsoup class
soup = BeautifulSoup(billboard_website, "html.parser")

#############
### TITLE ###
#############
# find a list of all span elements which contains anchor tags
song_titles = soup.find_all("h3", {"class": SONG_TITLE_CLASS})

# create a list of song titles
song_titles = [song.get_text().strip() for song in song_titles]
print(song_titles)
