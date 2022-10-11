#LED BLINKING
import RPi.GPIO as GPIO
	from time import sleep
		
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
	
	while True:                     
	    GPIO.output(10, GPIO.HIGH)              
	    print("The LED is ON")
	    sleep(2)                     
	    
	    GPIO.output(10, GPIO.LOW)               
	    print("The LED is OFF")
	    sleep(2)                    
