import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
#GPIO.setup(24, GPIO.LOW)
while True:
    entrada = GPIO.input(4)
    if entrada:
        GPIO.output(12,GPIO.LOW)
        
    else:
        GPIO.output(12,GPIO.HIGH)
        