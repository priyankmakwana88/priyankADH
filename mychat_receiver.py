#!/usr/bin/env python


#IMPORT LIBRARIES
import socket
import netifaces as ni
import thread
import base64


#INITIALIZE SOCKET
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

my_ip=ni.ifaddresses("wlp9s0")[ni.AF_INET][0]['addr']    #AUTO-DETECT WIRELESS IP
#my_ip =ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']    #AUTO-DETECT LAN IP
#my_ip="192.168.0.117"					 #PLEASE SETUP YOUR OWN IP MANUALLY
my_port=9999

#BINDING IP AND PORT
s.bind((my_ip,my_port))


#SETUP CHAT

print "WELCOME TO MY_CHAT!!\n"
dest_ip=raw_input("Enter destination ip : ")
my_name=raw_input("\nEnter Your name : ")

'''
def setup_self():
	my_name=raw_input("Enter Your name : ")
	s.sendto(my_name,(dest_ip,8888))

def setup_other():
	rec=s.recvfrom(100)	
	other_name=rec[0]
'''
#RECEIVER FUNCTION
def receive_msg():
	#pass
	rec=s.recvfrom(100)	##CHECK
	other_name=rec[0]       ##CHECK
	while 1:
		data_rec=s.recvfrom(1000)
		decoded_msg=base64.b64decode(data_rec[0])
		print '\n'+other_name+' : '+decoded_msg


#SENDER FUNCTION
def send_msg():
	s.sendto(my_name,(dest_ip,8888))##CHECK
	while 1:
		message=raw_input(my_name+" : ")
		secured_msg=base64.b64encode(message)
		s.sendto(secured_msg,(dest_ip,8888))


#PROCESSING BOTH FUNCTIONS TOGETHER USING THREADS

#thread.start_new_thread(setup_self,())
#thread.start_new_thread(setup_other,())

#STARTING THE CONVERSATION
choice=raw_input("Want to start the chat? [y/n]")
if choice=='y' or choice == 'Y':
	thread.start_new_thread(send_msg,())
	thread.start_new_thread(receive_msg,())

#TO KEEP THREADS RUNNIMG
while 1:
	pass

