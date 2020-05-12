from socket import *
#from time import ctime
import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
i=11
s=''

HOST=''
PORT=1224
BUFSIZE=1024
ADDR=(HOST,PORT)
ccmd=['o','f','e']
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
flag=1
data=''
data1=''
while True:
	print("Waiting for connection")
	tcpCliSock,addr = tcpSerSock.accept()
	print("...connected from : ",addr)
	
	
	try:
		while True:
			data= tcpCliSock.recv(BUFSIZE)
			data=data.decode("utf-8")
	
			if data == ccmd[0]:
				print("ON")
				
				if GPIO.input(23):
						print("Motion Detected")
						s="sudo fswebcam image"+str(i)+".jpg -S 30"
						subprocess.call(s,shell='True')
						time.sleep(5)
						i=i+1
				time.sleep(2)
				
				
			if data == ccmd[1]:
				print("OFF")
						

			if data == ccmd[2]:
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
	
