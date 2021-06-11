import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(24, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
#rojo = GPIO.PWM(17, 100)
der = GPIO.PWM(24, 100)
izq = GPIO.PWM(17, 100)
der.start(0)
izq.start(0)
    
while True:
    
    valor=input("Leer vel: ")
    if valor=="1":
        GPIO.output(17, GPIO.LOW)
        der.ChangeDutyCycle(50)
        #rojo.start(100)
    elif valor=="2":
        GPIO.output(17, GPIO.LOW)
        der.ChangeDutyCycle(100)
        #rojo.ChangeDutyCycle(75)
    elif valor=="3":
        der.ChangeDutyCycle(0)
        izq.ChangeDutyCycle(0)
        #der.ChangeDutyCycle(50)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)
        #rojo.ChangeDutyCycle(50)
    elif valor=="4":
        GPIO.output(24, GPIO.LOW)
        izq.ChangeDutyCycle(50)
        
    elif valor=="5":
        
        GPIO.output(24, GPIO.LOW)
        izq.ChangeDutyCycle(100)
    