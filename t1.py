#!/usr/bin/env python3

#IMPORT ALL LIBRARIES
import time
import webbrowser as wb

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

elif choice == '3':
	print ("Under maintainene")

elif choice == '4':
	print ("Under maintainene")

elif choice == '5':
	print ("Under maintainene")

elif choice == '6':
	print ("Under maintainene")

elif choice == '7':
	print ("Under maintainene")

else:
	#usr_ip=input("Enter the sentence : ")
	#print(clean_data(usr_ip))
	print ("Enter correct input !!!")



