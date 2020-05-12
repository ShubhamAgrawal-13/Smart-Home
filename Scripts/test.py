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
GPIO.setup(17,GPIO.IN)#PIR
#GPIO.setup()
GPIO.setup(23,GPIO.OUT)#LED
GPIO.setup(27,GPIO.OUT)#FAN

def gg():
	while True:	
		if ldr.value>0.5:
	    		print(ldr.value)
	    		time.sleep(1)
			GPIO.output(23,False)
		else:	
			print(ldr.value)
			time.sleep(1)	
			GPIO.output(23,True)
			
		if ttt2==1:
			break		

def ff():
	while True:	
		if ldr.value>0.5:
	    		print(ldr.value)
	    		time.sleep(1)
			a.forward(0.5)
			time.sleep(0.8)
			a.stop()
			while(ldr.value>0.5):
				time.sleep(1)	
				if ttt1==1:
					break
		else:
			if ttt1==1:
				break	
			print(ldr.value)
			time.sleep(1)	
			a.backward(0.4)
			time.sleep(0.8)
			a.stop()
			while(ldr.value<0.5):
				time.sleep(1)
				if ttt1==1:
					break
		if ttt1==1:
			break				
		

def hh():
	i=11
	s1=''
	logging.basicConfig(filename='log.txt',level=logging.DEBUG)
	logging.info("a new info came")
	try:
		#time.sleep(10)
		while True:
			if GPIO.input(17):
				print("Motion Detected")
				s1="sudo fswebcam /home/pi/image"+str(i)+".jpg -S 30"
				subprocess.call(s1,shell='True')
				time.sleep(5)
			
				system_id = 'pi.minorproject@gmail.com'
		                system_password = 'Raspberry281'
		                homeowner = 'homeowner.project@gmail.com'

		                subject = 'Home security'

		                msg = MIMEMultipart()
		                msg['From'] = system_id
		                msg['To'] = homeowner
		                msg['Subject'] = subject

		                body = 'Hi there, There is a intruder in your house..here is a pic..check it out!'
		                msg.attach(MIMEText(body,'plain'))
				print('hello vaibhav')
		                filename='image'+str(i)+'.jpg'
				print('shubham')
		                attachment  =open(filename,'rb')
				print('hello vedant')
		                part = MIMEBase('application','octet-stream')
		                part.set_payload((attachment).read())
		                encoders.encode_base64(part)
		                part.add_header('Content-Disposition',"attachment; filename= "+filename)

		                msg.attach(part)
		                text = msg.as_string()
		                server = smtplib.SMTP('smtp.gmail.com',587)
		                server.starttls()
		                server.login(system_id,system_password)

				print('hello shubham')
		                server.sendmail(system_id,homeowner,text)
		                server.quit()
				print('good shubham')
				i=i+1
			time.sleep(0.2)
			if ttt == 1:
				break
	except Exception as msg:
		logging.exception(msg)
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
									t1=threading.Thread(target=hh,name='t1_PIR')
									print("Shubham's favourite sir is Durga sir")
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
									GPIO.output(23,True)
			
								if data == cccmd[1]:
									print('led OFF')
									GPIO.output(23,False)

								if data == cccmd[2]:
									flag2=0

								if not data:
									print('hello')
									break
						if flag2==0:
								break
					except:
						print("hello from except")

			if data == ccmd[5]:
				print("Smart led")
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
									print('Smart led ON')
									ttt2=0
									t2=threading.Thread(target=gg,name='S_led')
									print("Shubham's favourite sir is Durga sir")
									t2.start()
											
								if data == cccmd[1]:
									print('Smart led  OFF')
									ttt2=1
									

								if data == cccmd[2]:
									flag5=0

								if not data:
									print('hello')
									break
						if flag5==0:
								break
					except:
						print("hello from except")


			if data == ccmd[6]:
				print("Smart Curtain")
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
									print('Smart curtain ON')
									ttt1=0
									t3=threading.Thread(target=ff,name='S_Curtain')
									print("Shubham's favourite sir is Durga sir")
									t3.start()
											
								if data == cccmd[1]:
									print('Smart curtain  OFF')
									ttt1=1
									

								if data == cccmd[2]:
									flag6=0

								if not data:
									print('hello')
									break
						if flag6==0:
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
						print("hello from except")
			if data == ccmd[4]:
				print("Curtain")
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
								
								#ldr = LightSensor(26)
									
								if data == cccmd[0]:
	    								#time.sleep(1)
									a.forward(0.5)
									time.sleep(0.8)
									a.stop()
									print('Curtain ON')
										
								if data == cccmd[1]:
									#time.sleep(1)
									a.backward(0.3)
									time.sleep(0.8)
									a.stop()		
									print('Curtain OFF')
									

								if data == cccmd[2]:
									flag4=0
									#flag=0
	
								if not data:
									print('hello')
									break
						if flag4==0:
								break
					except Exception as msg:
						logging.exception(msg)				
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
	
