import RPi.GPIO as GPIO
import subprocess
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
#GPIO.setup(23,GPIO.OUT)
i=11
s=''
try:
		while True:
					if GPIO.input(23):
						print("Motion Detected")
						#GPIO.output(23,True)
						s="sudo fswebcam image"+str(i)+".jpg -S 30"
						subprocess.call(s,shell='True')
						time.sleep(5)
						i=i+1
						#GPIO.output(23,False)
					time.sleep(2)
except:
	GPIO.cleanup()
GPIO.cleanup()
