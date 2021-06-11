import paho.mqtt.client as mqtt
cliente=mqtt.Client()

cliente.connect("musach.tk",1883)
val="6,6,6"
while True:
    val=input("ingrese valores: " )
    cliente.publish("values",val)