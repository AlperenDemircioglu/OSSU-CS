# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

listurl = []
listshow = []
k = 0
i = 0

while k < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    listurl.clear()
    listshow.clear()

    for tag in tags:
        if i == 18:
          url = listurl[17]
          i = 0
          break
        listurl.append((tag.get('href', None)))
        listshow.append((tag.contents[0]))
        i = i + 1

    k = k + 1


print(listshow[len(listshow)-1])
