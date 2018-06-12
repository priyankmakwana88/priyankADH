#!/usr/bin/env python3

#IMPORTING LIBRARIES
import urllib.request as ur
from bs4 import BeautifulSoup

website="https://www.news18.com/cricketnext/newstopics/live-cricket-score.html"

web_data=ur.urlopen(website)
source_code=web_data.read()

data=BeautifulSoup(source_code,'html5lib')

final_data=data.get_text()

#print(final_data)

x=final_data.find('@media')
final_data=final_data[x:]
print(final_data)

