class user:
    def __init__(self):
        self._usuario="Musk"
        self._password="NEWRO"
    def validacion(self):
        self.dato1 = input("Agregue usuario: ")
        self.dato2 = input("Agregue password: ")
        if self.dato1==self._usuario and self.dato2==self._password:
            self.bandera = True
            print("Welcome {} to NEWRO ROBOTIC, processing".format(self.dato1))
        else:
            self.bandera = False
            print("Try againg {}, por favor".format(self.dato1))
        return self.bandera