from Users import user
from Llave_principal import llave
import paho.mqtt.client as mqtt_client
import RPi.GPIO as GPIO
import time
import serial
import threading
import random

s = serial.Serial("/dev/ttyACM0",9600)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
der=GPIO.PWM(19,100)
izq=GPIO.PWM(26,100)

der.start(0)
izq.start(0)
global bandera1
global bandera2
global bandera3
global bandera4
bandera1 = 0
bandera2 = 0
bandera3 = 0
bandera4 = 0
broker = 'musach.tk'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'

def lectura():
    while True:
        entrada1=GPIO.input(4)
        entrada2=GPIO.input(14)
        if entrada1 == 0:
            print(f"s1 `{entrada1}` to s2 `{entrada2}`")
            der.ChangeDutyCycle(100)
            izq.ChangeDutyCycle(100)
            GPIO.output(19,GPIO.HIGH)
            GPIO.output(26,GPIO.HIGH)
            bandera1=1
            bandera3=1
        if entrada2 == 0:
            print(f"s1 `{entrada1}` to s2 `{entrada2}`")
            der.ChangeDutyCycle(100)
            izq.ChangeDutyCycle(100)
            GPIO.output(19,GPIO.HIGH)
            GPIO.output(26,GPIO.HIGH)
            bandera2=1
            bandera4=1
        

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to NEWRO server!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def logica_llave(text,text2):
    if text=="key":        
        if text2=="on":
            GPIO.output(17,GPIO.HIGH)
        else:
            GPIO.output(17,GPIO.LOW)
    if text=="dirIzq":        
        if text2=="on":
            GPIO.output(27,GPIO.HIGH)
        else:
            GPIO.output(27,GPIO.LOW)
    if text=="dirDer":
        if text2=="on":
            GPIO.output(18,GPIO.HIGH)
        else:
            GPIO.output(18,GPIO.LOW)
    if text=="ledInf":        
        if text2=="on":
            GPIO.output(22,GPIO.HIGH)
        else:
            GPIO.output(22,GPIO.LOW)
    if text=="ledSup":        
        if text2=="on":
            GPIO.output(23,GPIO.HIGH)
        else:
            GPIO.output(23,GPIO.LOW)
    if text=="luzAlta":        
        if text2=="on":
            GPIO.output(24,GPIO.HIGH)
        else:
            GPIO.output(24,GPIO.LOW)
    if text=="claxon":        
        if text2=="on":
            GPIO.output(25,GPIO.HIGH)
        else:
            GPIO.output(25,GPIO.LOW)
    if text=="motor":
        if text2=="v1d":
            #GPIO.output(26,GPIO.LOW)
            #der.ChangeDutyCycle(25)
            print("derecha lenta")
            #bandera2 = 0
            #bandera3 = 0
            #motor(bandera1,bandera2,bandera3,bandera4)
            letra="E"
            s.write(str.encode(letra))
        elif text2=="v2d":
            GPIO.output(26,GPIO.LOW)
            der.ChangeDutyCycle(50)
            print("derecha lenta")
            bandera2 = 0
            bandera3 = 0
        elif text2=="sss":
            der.ChangeDutyCycle(0)
            izq.ChangeDutyCycle(0)
            GPIO.output(26,GPIO.LOW)
            GPIO.output(19,GPIO.LOW)
            time.sleep(0.15)
            print("detenido")
        elif text2=="v1i":
            #GPIO.output(19,GPIO.LOW)
            #izq.ChangeDutyCycle(25)
            print("izquierda lenta")
            #bandera1 = 0
            #bandera4 = 0
            letra="A"
            s.write(str.encode(letra))
        elif text2=="v2i":
            GPIO.output(19,GPIO.LOW)
            izq.ChangeDutyCycle(50)
            print("izq rapido")
            bandera1 = 0
            bandera4 = 0
    if text=="acel":        
        if text2=="acBaj":
            GPIO.output(16,GPIO.LOW)
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)
        elif text2=="acMed":
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)
        elif text2=="acAlt":
            GPIO.output(16,GPIO.LOW)
            GPIO.output(20,GPIO.HIGH)
            GPIO.output(21,GPIO.LOW)

class Application:
    def __init__(self):
        #funcion para validar conexion
        #iniciamos conexion socket
        self.text="NEWRO ROBOTIC"
        print(self.text)     
    def suscriber(self,client: mqtt_client):
        self.text="Estamos en suscripcion"
        print(self.text)
        def on_message(client, userdata, msg):
            #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            var=format(msg.payload.decode("utf-8"))
            logica_llave(msg.topic,var)
            print("validacion de topico {}".format(msg.topic))
            
        print("Suscribe processing")
        client.subscribe("key")
        client.subscribe("dirIzq")
        client.subscribe("dirDer")
        client.subscribe("ledInf")
        client.subscribe("ledSup")
        client.subscribe("claxon")
        client.subscribe("motor")
        client.subscribe("acel")
        client.subscribe("sw_vel1")
        client.subscribe("sw_vel2")
        client.subscribe("intermm")
        client.on_message = on_message
        
        
    def publisher(self,client):
        self.text="Estamos en publicador"
        print(self.text)
        topic3="values"
        while True:
            time.sleep(1)
            a = s.readline()
            #msg = a.decode()
            #c = msg.split(',')
            #c[1]=c[1].rstrip('\r\n')
            #msg = f"messages: {msg_count}"
            #msg = f"Distancia: {b}"
            #msg="10"
            result = client.publish(topic3, a)
            #client.publish("values2",c[1])
            #print("esto es ",c)
            #
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{a}` to topic `{topic3}`")
            else:
                print(f"Failed to send message to topic {topic3}")
        
client = connect_mqtt()
#loggin=user()
#loggin.validacion()
general=Application()
entrada1=GPIO.input(4)
print(f"Lectura sensor {entrada1}")
#general.suscriber(client)
#general.publisher(client)

T1 = threading.Thread(target=general.suscriber,args=(client,))
T2 = threading.Thread(target=general.publisher,args=(client,))
#T3 = threading.Thread(target=lectura,args=())
T2.start()
T1.start()
#T3.start()
va=llave()
client.loop_forever()