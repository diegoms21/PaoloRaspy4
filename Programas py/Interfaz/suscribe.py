import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
cliente=mqtt.Client()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
cliente.connect("musach.tk",1883)
def escuchar(cliente,userdata,mensaje):
    sw1=format(mensaje.payload.decode("utf-8"))
    print (sw1)
def escuchar2(cliente,userdata,msj):
    sw2=format(msj.payload.decode("utf-8"))
    print (sw2)
cliente.on_message= escuchar
cliente.on_message= escuchar2
cliente.subscribe("led1")
cliente.subscribe("led2")

cliente.loop_forever()
