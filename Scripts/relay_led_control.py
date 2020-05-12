from socket import *
#from time import ctime
import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)


HOST=''
PORT=122
BUFSIZE=1024
ADDR=(HOST,PORT)
ccmd=['o','f','e']
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
flag=1
data=''
while True:
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
				print("ON")
				GPIO.output(23,False)
				
				#time.sleep(5)
			if data == ccmd[1]:
				print("OFF")
				GPIO.output(23,True)

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
	
