#!/usr/bin/env python3

#IMPORTING LIBRARIES
import urllib.request as ur
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import numpy as np

#WEBBSITE TO SCRAP
website="http://www.cricbuzz.com/cricket-match/live-scores"

#GETTING SOURCE CODE
web_data=ur.urlopen(website)
source_code=web_data.read()

#USING BEAUTIFUL-SOUP TO ALIGN THE TEXT
data=BeautifulSoup(source_code,'html5lib')
#sent_split=sent_tokenize(final_data)

#print(np.shape(sent_split))
good_data=data.prettify()


#FUNCTION TO EXTRACT SCORE DATA FROM SOUCE CODE
def get_score(good_data):
	first_header=good_data.find('<h2')
	next_header=good_data.find('<h2',first_header+1)
	if first_header==-1 or next_header==-1:	
		return	
	req_score_data=good_data[first_header:next_header]
	score_bs4=BeautifulSoup(req_score_data,'html5lib')
	score_instance=score_bs4.get_text(strip=True)
	split_instance=sent_tokenize(score_instance)
	copy_instance=split_instance[0]
	
	#INSTANCE CLEANING
	live=split_instance[0].find('Live')
	split_instance[0]=split_instance[0][:live]
	check_discarded=copy_instance[live:]
	
	#print('@@\n'+check_discarded+'\n@@\n')
	'''
	if len(check_discarded)>38:
		while len(check_discarded)>38:
			news=check_discarded.find('News')
			live=check_discarded.find('Live',news)
			patch=check_discarded[news+4:live]
			split_instance.append(patch)
			check_discarded=check_discarded[live+1:]
				
	'''
	print(split_instance)
	print('\n')
	
	good_data=good_data[next_header:]
	get_score(good_data)

get_score(good_data)
