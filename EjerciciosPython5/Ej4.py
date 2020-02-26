class Cuenta:
    def __init__(self, numCuenta, saldo):
        self.numCuenta = numCuenta
        self.saldo = saldo

    def consultarSaldo(self):
        print("El saldo es de " + str(self.saldo) + "€")

    def recibirAbonos(self, abono):
        self.saldo += abono
        print("Tras el abono de " + str(abono) + " el saldo es de " + str(self.saldo) + "€")

    def pagarRecibos(self, recibo):
        self.saldo -= recibo
        print("Tras el recibo de " + str(recibo) + " el saldo es de " + str(self.saldo) + "€")

class Persona:
    def __init__(self, dni):
        self.dni = dni
        self.cuentas = []

    cuenta = Cuenta(12536, 0)

    def addCuentas(self, cuenta):
        if len(self.cuentas) < 3:
            print("La cuenta se ha creado correctamente")
            self.cuentas.append(cuenta.__dict__)
        else:
            print("Tiene usted un exceso de cuentas debería eliminar alguna antes de crear una nueva")


    def morosidad(self):
        cuentas = self.cuentas.keys()
        for i in cuentas:
            print(i)


persona = Persona(1234546)

cuenta1 = Cuenta(12516, 0)
cuenta2 = Cuenta(12565, 121)
cuenta3 = Cuenta(12564, 111)
cuenta4 = Cuenta(125654, 0)

persona.addCuentas(cuenta1)
persona.addCuentas(cuenta2)
persona.addCuentas(cuenta3)
persona.addCuentas(cuenta4)

print(persona.__dict__)

cuenta1.pagarRecibos(25)

print(persona.__dict__)

persona.morosidad()