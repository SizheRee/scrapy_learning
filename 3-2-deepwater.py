#! /usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
import datetime
import random
import logging

pages = set()
random.seed(datetime.datetime.now())
logging.basicConfig(level=logging.DEBUG)

# get all in-link from page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        href = link.attrs['href']
        if href is not None:
            if href not in internalLinks:
                logging.debug("found new interlink:%s"%href)
                internalLinks.append(href)

# get all out-link from page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("random externalLink is:" + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
