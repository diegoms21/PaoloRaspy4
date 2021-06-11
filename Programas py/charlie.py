entrada1 = GPIO.input(4)
    if entrada1 == 0 and bandera3 == 0:
        der.ChangeDutyCycle(100)
        izq.ChangeDutyCycle(100)
        der.ChangeDutyCycle(100)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        bandera1 = 1
        bandera3 = 1
    else:
        print("nada")
    entrada2 = GPIO.input(14)
    if entrada2 == 0 and bandera4 == 0:
        der.ChangeDutyCycle(100)
        izq.ChangeDutyCycle(100)
        der.ChangeDutyCycle(100)
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        bandera2 = 1
        bandera4 = 1
    else
        print("nada")