"""Scraping a live website: HackerNews. We would like to get the title of the news article, the link and the score (the points) that
each article has."""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# request the HNs website as a text and then parse it with BeautifulSoup
hn_website = requests.get("https://news.ycombinator.com/newest").text

# instantiate the beautifulsoup class
soup = BeautifulSoup(hn_website, "html.parser")

#############
### TITLE ###
#############
# find a list of all span elements which contains anchor tags
spans = soup.find_all("tr", {"class": "athing submission"})
scores = soup.find_all("span", {"class": "score"})

# create a list of article titles
titles = [span.get_text() for span in spans]
# remove the rank (numbered position) of the element in the string
titles = [re.sub("(\d+.)", "", title) for title in titles]

#############
### LINKS ###
#############
links = [link.find_all("a")[1]["href"] for link in spans]
# sometimes the link starts with "item?id=..." because the article is a news ycombinator message, not an article referring to an external site.
# Then, need to add the "https://news.ycombinator.com/" string to it
links = [
    ("https://news.ycombinator.com/" + link) if link.startswith("item?id=") else link
    for link in links
]

############
### RANK ###
############
scores = [
    int(score.get_text().replace(" point", "").replace(" points", "").replace("s", ""))
    for score in scores
]

#####################
### CONVERT TO DF ###
#####################

if __name__ == "__main__":
    # dictionary of lists
    dict = {"titles": titles, "links": links, "scores": scores}
    df = pd.DataFrame(dict).sort_values(by=["scores"], ascending=False)
    print(df)
