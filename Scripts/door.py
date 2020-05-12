import RPi.GPIO as GPIO
from socket import *
import time
from gpiozero import Motor

GPIO.setmode(GPIO.BCM)
print("Door")
a=Motor(20,21)

HOST=''
PORT=12321
BUFSIZE=1024
ADDR=(HOST,PORT)
ccmd=['p','l','m','a','c','q','r']
cccmd=['o','f','e']
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
flag4=1
data=''

while True:
	print('Hello')
	flag4=1
	print("Waiting for connection")
	tcpCliSock,addr = tcpSerSock.accept()
	print("...connected from : ",addr)
	try:
		while True:
			data= tcpCliSock.recv(BUFSIZE)
			#print(data)
			#print(type(data))
			data=data.decode("utf-8")
			if data == cccmd[0]:
	    			#time.sleep(1)
				a.forward(0.5)
				time.sleep(0.8)
				a.stop()
				print('Door Locked')
										
			if data == cccmd[1]:
				#time.sleep(1)
				a.backward(0.3)
				time.sleep(0.8)
				a.stop()		
				print('Door UnLocked')
									

			if data == cccmd[2]:
				flag4=0
	
			if not data:
				print('hello')
				break
		if flag4==0:
			break
	except Exception as msg:		
		print("hello from except")
print("hi")
GPIO.cleanup()
tcpSerSock.close()
