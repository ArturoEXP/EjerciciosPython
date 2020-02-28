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
    def __init__(self, dni, cuentas = []):
        self.dni = dni
        self.cuentas = cuentas

    def addCuentas(self, cuenta):
        if len(self.cuentas) < 3:
            print("La cuenta se ha creado correctamente")
            self.cuentas.append(cuenta.__dict__)
        else:
            print("Tiene usted un exceso de cuentas debería eliminar alguna antes de crear una nueva")

    def morosidad(self):
        for c in self.cuentas:
            if c["saldo"] < 0:
                print("La cuenta con número de cuenta: " + str(c["numCuenta"]) + " está en números rojos, su saldo es igual a: " + str(c["saldo"]))

    def transferencia(self, numCuentaEmisor, numCuentaReceptor, saldoAenviar):
        for c in self.cuentas:
            if c["numCuenta"] == numCuentaEmisor:
                c["saldo"] -= saldoAenviar
            elif c["numCuenta"] == numCuentaReceptor:
                numCuenta2 = numCuentaReceptor
                c["saldo"] += saldoAenviar
            else:
                print("El número de cuenta: " + str(c["numCuenta"]) + " no existe como cuenta de esta persona")

            

class PruebaCuentas:
    persona = Persona("53189747Q")

    cuenta1 = Cuenta("cuenta1", 0)
    cuenta2 = Cuenta("cuenta2", 700)

    persona.addCuentas(cuenta1)
    persona.addCuentas(cuenta2)

    cuenta1.recibirAbonos(1100)
    cuenta2.pagarRecibos(750)

    persona.morosidad()
    persona.transferencia(cuenta1.numCuenta, cuenta2.numCuenta, 100)
    persona.morosidad()
    cuenta1.consultarSaldo()
    cuenta2.consultarSaldo()





pruebaCuentas = PruebaCuentas()
