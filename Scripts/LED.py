import RPi.GPIO as GPIO
import time
#import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)

try:
    while True:
      	    GPIO.output(24,True)
            time.sleep(5)
	    GPIO.output(24,False)
	    print("light detected")
            time.sleep(5)
except:
	GPIO.cleanup()

