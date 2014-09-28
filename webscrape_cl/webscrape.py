__author__ = 'markbradford'

import requests
from bs4 import BeautifulSoup

url = "http://austin.craigslist.org/search/sss#list"
#Use requests.get to grab all html at given url
page = requests.get(url)

#Create instance called soup of class BeautifulSoup
soup = BeautifulSoup(page.content)

#   Look at webpage via "inspect element" to see how elements are described
#   in html and use for loops to append the info we want to scrape to each list
items = []
links = []
for item in soup.find_all("a", {"class": "hdrlnk"}):
    items.append(item.text)
    links.append(item.get("href"))

prices = []
for price in soup.find_all("span", {"class": "price"}):
    prices.append(price.text)

print items, links, prices