from socket import *
#from time import ctime
import RPi.GPIO as GPIO
from gpiozero import LightSensor,Motor
import subprocess
import smtplib
import time
import logging
#import test1
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)#PIR
#GPIO.setup()
GPIO.setup(23,GPIO.OUT)#LED
GPIO.setup(27,GPIO.OUT)#FAN
		
def hh():
	i=1
	s1=''
	#logging.basicConfig(filename='log.txt',level=logging.DEBUG)
	#logging.info("a new info came")
	try:
		#time.sleep(10)
		while True:
			if GPIO.input(22):
				print("Motion Detected-",i)
				i+=1
				time.sleep(3)
			time.sleep(0.2)
			if ttt == 1:
				break
	except Exception as msg:
		#logging.exception(msg)
		print("dfg")
		#GPIO.cleanup()
	
	print("BYE")
HOST=''
PORT=12321
BUFSIZE=1024
ADDR=(HOST,PORT)
ccmd=['p','l','m','a','c','q','r']
cccmd=['o','f','e']
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
flag=1
flag1=1
flag2=1
flag3=1
flag4=1
flag5=1
flag6=1
data=''
ttt=0
ttt1=0
ttt2=0
a=Motor(20,21)
ldr = LightSensor(26)
while True:
	flag1,flag2,flag3,flag4,flag5,flag6=1,1,1,1,1,1
	ttt=0
	print("Waiting for connection")
	tcpCliSock,addr = tcpSerSock.accept()
	print("...connected from : ",addr)
	try:
		while True:
			data= tcpCliSock.recv(BUFSIZE)
			#print("hello")
			#print(data)
			#print(type(data))
			data=data.decode("utf-8")
			
			if data == ccmd[0]:
				print('PIR')
				while True:
					print('Hello')
					tcpCliSock,addr = tcpSerSock.accept()
					print("...connected from : ",addr)
					try:
						while True:
								data= tcpCliSock.recv(BUFSIZE)
								#print(data)
								#print(type(data))
								data=data.decode("utf-8")

								if data == cccmd[0]:
									print('pir ON')
									ttt=0
									
									t1=threading.Thread(target=hh,name='thread_PIR')
									#print("Shubham's favourite sir is Durga sir")
									t1.start()
										
									
								if data == cccmd[1]:
									print('pir OFF')
									ttt=1
			
								if data == cccmd[2]:
									flag1=0

								if not data:
									print('hello')
									break
						if flag1==0:
								break
					except:
						print("hello from except pir")
							
				
			if data == ccmd[1]:
				print("LED")
				while True:
					print('Hello')
					tcpCliSock,addr = tcpSerSock.accept()
					print("...connected from : ",addr)
					try:
						while True:
								data= tcpCliSock.recv(BUFSIZE)
								#print(data)
								#print(type(data))
								data=data.decode("utf-8")

								if data == cccmd[1]:
									print('led OFF')
									GPIO.output(23,True)
			
								if data == cccmd[0]:
									print('led ON')
									GPIO.output(23,False)

								if data == cccmd[2]:
									flag2=0

								if not data:
									print('hello')
									break
						if flag2==0:
								break
					except:
						print("hello from except led")

			
			if data == ccmd[2]:
				print("FAN")
				while True:
					print('Hello')
					tcpCliSock,addr = tcpSerSock.accept()
					print("...connected from : ",addr)
					try:
						while True:
								data= tcpCliSock.recv(BUFSIZE)
								#print(data)
								#print(type(data))
								data=data.decode("utf-8")

								if data == cccmd[0]:
									print('fan ON')
									GPIO.output(27,False)			
								if data == cccmd[1]:
									print('fan OFF')
									GPIO.output(27,True)

								if data == cccmd[2]:
									flag3=0

								if not data:
									print('hello')
									break
						if flag3==0:
								break
					except:
						print("hello from except fan")
			if data == ccmd[3]:
				flag=0
				print("Exit")
			if not data:
				print('hello')
				break
			
		if flag==0:
			break
	except:
		print("hello from except")
print("hi shubham")
GPIO.cleanup()
tcpSerSock.close()

	
