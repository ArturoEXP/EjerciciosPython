class Tiempo:
    def __init__(self, hora, minuto = 15, segundo = 15):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def modificarHora(self, hora, minuto, segundo):
        self.hora = input("Inserta la hora: ")
        self.minuto = input("Inserta los minutos: ")
        self.segundo = input("Inserta los segundos: ")



h = input("Inserta hora: ")

t = Tiempo(h)

print(list(t.__dict__))