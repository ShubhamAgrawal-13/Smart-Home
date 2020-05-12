from socket import *
#from time import ctime
import RPi.GPIO as GPIO
import subprocess
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)

HOST=''
PORT=12321
BUFSIZE=1024
ADDR=(HOST,PORT)
ccmd=['p','l','m','a']
cccmd=['o','f','e']
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
flag=1
flag1=1
flag2=1
flag3=1
data=''
s=''
while True:
	flag1,flag2,flag3=1,1,1
	print("Waiting for connection")
	tcpCliSock,addr = tcpSerSock.accept()
	print("...connected from : ",addr)
	try:
		while True:
			data= tcpCliSock.recv(BUFSIZE)
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
									s="sudo fswebcam image.jpg -S 30"
									subprocess.call(s,shell='True')
									time.sleep(1)
			
								if data == cccmd[1]:
									print('pir OFF')

								if data == cccmd[2]:
									flag1=0

								if not data:
									print('hello')
									break
						if flag1==0:
								break
					except:
						print("hello from except")
							
				
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

								if data == cccmd[0]:
									print('led ON')
									GPIO.output(2,True)
			
								if data == cccmd[1]:
									print('led OFF')
									GPIO.output(2,False)

								if data == cccmd[2]:
									flag2=0

								if not data:
									print('hello')
									break
						if flag2==0:
								break
					except:
						print("hello from except")

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
									GPIO.output(23,True)			
								if data == cccmd[1]:
									print('fan OFF')
									GPIO.output(23,False)

								if data == cccmd[2]:
									flag3=0

								if not data:
									print('hello')
									break
						if flag3==0:
								break
					except:
						print("hello from except")
				
			if data == ccmd[3]:
				flag=0
			if not data:
				#print("hello")
				break
		if flag==0:
			break
	except:
		print("hello from except")
print("hi")
GPIO.cleanup()
tcpSerSock.close()
	
