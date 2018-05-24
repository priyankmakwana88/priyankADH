#!/usr/bin/env python

#IMPORT LIBRARIES
import socket
import thread
import netifaces as ni


#INITIALIZE SOCKET AND BIND IP WITH PORT
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#my_ip=ni.ifaddresses("wlp9s0")[ni.AF_INET][0]['addr']		#AUTO-DETECT MY WIRELESS IP
#my_ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']		#AUTO-DETECT MY LAN IP
my_ip="127.0.0.1" 						#PLEASE SETUP YOUR OWN IP MANUALLY
my_port=8888
s.bind((my_ip,my_port)) 

#SETUP CHAT

print "WELCOME TO MY_CHAT!!\n"
dest_ip=raw_input("Enter destination ip : ")
my_name=raw_input("\nEnter Your name : ")

'''
def setup_self():
	my_name=raw_input("Enter Your name : ")
	s.sendto(my_name,(dest_ip,9999))

def setup_other():
	rec=s.recvfrom(100)	
	other_name=rec[0]
'''

#FUNCTION TO SEND THE DATA
def send_msg():
	s.sendto(my_name,(dest_ip,9999))##CHECK
	while 1:
		msg=raw_input(my_name+' : ')
		s.sendto(msg,(dest_ip,9999))


#FUNCTION TO RECEIVE THE MESSAGE
def receive_msg():
	rec=s.recvfrom(100)	##CHECK
	other_name=rec[0]       ##CHECK
	while 1:
		rec_data=s.recvfrom(1000)
		print '\n'+other_name+' : '+rec_data[0]

#PROCESSING BOTH FUNCTIONS TOGETHER USING THREADS

#thread.start_new_thread(setup_self,())
#thread.start_new_thread(setup_other,())
#STARTING THE CONVERSATION
choice=raw_input("Want to start the chat? [y/n]")
if choice=='y' or choice == 'Y':
	thread.start_new_thread(send_msg,())
	thread.start_new_thread(receive_msg,())

#TO KEEP THREADS RUNNING
while 1:
	pass

