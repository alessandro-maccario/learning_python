"""Day 46: Music Time Machine Project"""

from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import re
from dotenv import load_dotenv


# Load env variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

################
### CONSTANT ###
################

URL = "https://www.billboard.com/charts/hot-100/"
SONG_TITLE_CLASS = "c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025"
LIST_ELEMENTS_CLASS = "o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-padding-l-050 lrv-u-padding-l-00@mobile-max u-max-width-397"
SPAN_ANCHOR_TAG_CLASS = "c-label a-no-trucate a-font-secondary u-font-size-15 u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px a-children-link-color-black a-children-link-color-brand-secondary:hover lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max"
LIST_ARTISTS_SONGS_CLASS = "o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-padding-l-050 lrv-u-padding-l-00@mobile-max u-max-width-397"
HEADER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"

SEARCH_ENDPOINT = "https://api.spotify.com/v1/search"
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

# find li elements
list_elements = soup.find_all(
    "span",
    {"class": SPAN_ANCHOR_TAG_CLASS},
)


lists_artists_songs = soup.find_all(
    "li",
    {"class": LIST_ARTISTS_SONGS_CLASS},
)

# list of lists containing [song_name, artist_name] to be used for the search in Spotify
artists_songs_list = [
    re.split(r"\s{2,}", span.get_text().strip()) for span in lists_artists_songs
]


# # convert this into a list comprehension?
# artists_list = [[link["href"] for link in span.find_all("a")] for span in list_elements]

# # clean the list of artist names to have the very first artist name, even though there are multiple ones
# artists_list_cleaned = [artist[0].split("/")[-2] for artist in artists_list if artist]
# # print(artists_list_cleaned)

# # create a list of song titles
# song_titles = [song.get_text().strip() for song in song_titles]
# # print(song_titles)

##################################
### SPOTIFY/SPOTIPY CONNECTION ###
##################################

# Istantiate Spotipy class
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com/callback",
        scope="playlist-modify-private",
    )
)


# print(sp.current_user())
# TODO: need to loop over each and every songs and then save the URI in a list of URIs
song_name = artists_songs_list[1][0]
artist_name = artists_songs_list[2][1]
# Extract the year from the user input and use it for the research in addition to the artist name
year = date[:4]

# define the search query and start the search for the specific artist and the specific year
search_query = f'track:"{song_name}" year:{year}'
research_song = sp.search(q=search_query, limit=1, offset=0, type="track", market=None)
print(research_song["tracks"]["items"][0]["uri"])
