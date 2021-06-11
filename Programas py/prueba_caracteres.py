import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
while True:
    let=input("introduce letra: ")
    if let=="1":
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)
    elif let=="2":
        GPIO.output(3,GPIO.LOW)
        #GPIO.PWM(4,50)
    elif let=="0":
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
    elif let=="3":
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)