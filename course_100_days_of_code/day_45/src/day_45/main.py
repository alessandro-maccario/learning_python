"""Scraping a live website: HackerNews"""

from bs4 import BeautifulSoup
from bs4 import Tag
import requests
import pandas as pd


hn_website = requests.get("https://news.ycombinator.com/newest").text

# instantiate the beautifulsoup class
soup = BeautifulSoup(hn_website, "html.parser")

#############
### TITLE ###
#############
# find a list of all span elements which contains anchor tags
spans = soup.find_all("tr", {"class": "athing submission"})
scores = soup.find_all("span", {"class": "score"})
# print(spans)

# create a list of article titles
titles = [span.get_text() for span in spans]
# print(titles)

#############
### LINKS ###
#############
links = [link.find_all("a")[1]["href"] for link in spans]
# print(links)

############
### RANK ###
############
scores = [score.get_text() for score in scores]


#####################
### CONVERT TO DF ###
#####################

# dictionary of lists
dict = {"titles": titles, "links": links, "scores": scores}
df = pd.DataFrame(dict)
print(df)
