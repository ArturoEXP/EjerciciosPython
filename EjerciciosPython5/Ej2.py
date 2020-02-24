class Coche:
    def __init__(self, color, marca, modelo, caballos, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula

class PruebaCoche:
    miCocheBonito = Coche("rojo", "Audi", "A5", 170, 3, "2503JNG")
    miFurgoTrabajo = Coche("azul", "Renault", "kangoo", 170, 3, "2503JNG")
    miCocheMmm = Coche("negro", "Peugot", "308", 170, 3, "2503JNG")
    miFurgoGuay = Coche("blanco", "Mercedes", "VitoVIP", 170, 3, "2503JNG")

    def cambiarColor(self, colorNuevo):
        self.miCocheBonito.color = colorNuevo
        print("El color del coche se ha cambiado a " + self.miCocheBonito.color)

    def mostrarCoches(self):
        print(self.miCocheBonito.__dict__)
        print(self.miCocheMmm.__dict__)
        print(self.miFurgoGuay.__dict__)
        print(self.miFurgoTrabajo.__dict__)

coche = PruebaCoche().cambiarColor("Azul")

coche = PruebaCoche().mostrarCoches()