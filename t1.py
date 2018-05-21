#!/usr/bin/env python3

#IMPORT ALL LIBRARIES
import time
import webbrowser as wb
import datetime
from bs4 import BeautifulSoup
import urllib.request
import sys
import whois
import requests
import os


#PREPARING OPTION LIST(MENU)
option_list = '''
	---LIST---

	PRESS 1: Search individual word for input
	PRESS 2: Search image of individual word for input
	PRESS 3: URL of each word
	PRESS 4: Curent date & time
	PRESS 5: Open default web browser 
	PRESS 6: Scan all IP's connected to the network
	PRESS 7: Check owner with its email & contact for a given domain name'''

#DISPLAY OPTIONS & TAKING INPUT
print (option_list)
choice=input("Enter your choice : ")

#DATA CLEANING
def clean_data(ip_data):
	stripped_data=ip_data.strip()	#____Removing extra spaces
	final_data=stripped_data.split()#____Fetching individual words
	return final_data

#PLATFORM DETECTION
def detect_platform():
	platform=sys.platform
	if platform == "linux":
		print("Opening firefox!!")
	elif platform == "darwin":
		print("Opening safari!!")
	elif plarform == "windows":
		print("Opening internet explorer!!!")
	else:
		print ("Opening your default browser!!")


#EXTRACTING REQUIRED INFORMATION FROM DETAILS OF DOMAIN FETCHED
'''
def domain_data_clean(domain_details):
	domain_name_pos=domain_details.find("domain_name")
	sq_pos=domain_details.find("[",domain_name_pos+1)
	start_quote=domain_details.find('"',sq_pos+1)
	end_quote=domain_details.find('"',start_quote+1)
	#d_names=[]
	#d_names.append(domain_details)
	print (domain_details[start_quote:end_quote+1])
'''

#Switching the user choice
if choice == '1':
	#Cleaning & featching words
	usr_ip=input("Enter the sentence : ")
	cleaned_data=clean_data(usr_ip)
	#Searching individual word
	for i in cleaned_data:
		wb.open_new_tab("https://www.google.com/search?q="+i)

elif choice == '2':
	#cleaning & fetching words
	usr_ip=input("Enter the sentence : ")
	cleaned_data=clean_data(usr_ip)
	#Searching individual image for word
	for i in cleaned_data:
		wb.open_new_tab("https://www.google.com/search?q="+i+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjg1ZK5mYjbAhVBzbwKHa-_CjcQ_AUICigB")



##THIS OPTION IS BETA VERSION (BUILD YET TO RELEASE!!!)

elif choice == '3':
	
	usr_ip=input("Enter the sentence : ")
	cleaned_data=clean_data(usr_ip)

	#Searching individual word
	for i in cleaned_data:
		print("LINKS FOR ",i," : ")
		print("")
		#wb.open_new_tab("https://www.google.com/search?q="+i)
		url_new="https://www.google.com/search?q="+i
		page = requests.get(url_new)
		html_source=page.text
		
		#constructing beautifulsoup constructer
		soup=BeautifulSoup(html_source,'html.parser')
		sorted_page=soup.prettify()

		#FINDING LINKS
		del_pos=[]

		while sorted_page.find('<cite') >0:
			cite_pos=sorted_page.find('<cite')
			http_pos=sorted_page.find('http',cite_pos+1)
			end_cite_pos=sorted_page.find('</cite>',http_pos+1)
			link=sorted_page[http_pos:end_cite_pos]
	
			#TO REMOVE <B> TAGS INCLUDED IN link
			new_link=link.split()
			i=0	
			len_list=len(new_link)
			while i < len_list:
				if new_link[i]=='<b>' or new_link[i]=='</b>':
					del_pos.append(i)
				i=i+1
			del_pos.reverse()
			for j in del_pos:
				del new_link[j]
			del del_pos[:]

			#CREATING STRING FROM LIST
			link_final=''
			for i in new_link:
				link_final=link_final+i		
		
			print(link_final)
			print('')
			#link_final=''
			sorted_page=sorted_page[end_cite_pos+6:]


elif choice == '4':
	#Printing current date & time
	print ("Date : ",datetime.datetime.now().date())	
	print ("Time : ",datetime.datetime.now().time())

elif choice == '5':
	detect_platform()
	wb.open("https://")	

elif choice == '6':
	
	ip=os.system('sudo arp-scan --interface=wlp9s0 --localnet')	
	print(ip)

elif choice == '7':
	domain_name=input("Enter domain name : ")
	domain_details=whois.whois(domain_name)
	print ("Domain Name : ",domain_details.domain_name)	
	print ("Emails : ",domain_details.emails)	
	
else:
	print ("Enter correct input !!!")



