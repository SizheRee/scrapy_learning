
#! /usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import logging
import random
import datetime

logging.basicConfig(level=logging.INFO)

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)

count = 0
logging.info("*************findlink**********")
for link in bsObj.findAll("a"):
    count += 1
    if 'href' in link.attrs:
        print("%s:"%(count),link.attrs['href'])
        if count > 10 :
            break
        
logging.info("*************optimize*********")
count = 0
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                            href=re.compile("^(/wiki/)((?!:).)*$")): 
    count += 1
    if 'href' in link.attrs:
        print("%s: "%count, link.attrs['href'])
    if count >= 10:
        break

logging.info("************getLinks**********")

random.seed(datetime.datetime.now)
def getLinks (articleUrl):
    domain = "http://en.wikipedia.org"
    html = urlopen(domain + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                            href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while (len(links) > 0):
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle, "get_links[%s]"%len(links))
    links = getLinks(newArticle)

