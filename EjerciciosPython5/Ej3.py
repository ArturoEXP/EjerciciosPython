class Tiempo:
    'Esta es una clase que recoge la hora los minutos y los segundos uingresados por el usuario'
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def modificarHora(self, hora, minuto, segundo):
        self.hora = input("Inserta la hora: ")

    def mostrarHora(self):
        print("Son las " + str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo))

    

h = input("Inserta hora: ")
m = input("Inserta hora: ") or 0
s = input("Inserta hora: ") or 0

t = Tiempo(h, m, s)

t.mostrarHora()