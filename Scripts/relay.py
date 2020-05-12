import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
try:
	while True:
			GPIO.output(2,True)	
			time.sleep(2)
			GPIO.output(2,False)
			GPIO.output(3,True)	
			time.sleep(2)
			GPIO.output(3,False)
			GPIO.output(4,True)	
			time.sleep(2)
			GPIO.output(4,False)
			GPIO.output(17,True)	
			time.sleep(2)
			GPIO.output(17,False)
			time.sleep(2)
except:
	GPIO.cleanup()


