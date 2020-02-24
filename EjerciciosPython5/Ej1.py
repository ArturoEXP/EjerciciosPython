class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcularArea(self):
        area = float(self.base) * float(self.altura)

        return str(area)


    def calcularPerimetro(self):
        perimetro = float(self.base) * 2 + float(self.altura) * 2

        return str(perimetro)



class PruebaRectangulo:
    rectangulo1 = Rectangulo(20, 10)
    rectangulo2 = Rectangulo(50, 60)
    rectangulo3 = Rectangulo(2, 6)

    def primerRectangulo(self):
        print("El primer rectángulo")
        print("Area: " + self.rectangulo1.calcularArea())
        print("Perimetro: " + self.rectangulo1.calcularPerimetro())

    def segundoRectangulo(self):
        print("\n El segundo rectángulo")
        print("Area: " + self.rectangulo2.calcularArea())
        print("Perimetro: " + self.rectangulo2.calcularPerimetro())

    def tercerRectangulo(self):
        print("\n El tercer rectángulo")
        print("Area: " + self.rectangulo3.calcularArea())
        print("Perimetro: " + self.rectangulo3.calcularPerimetro())



rectangulo = PruebaRectangulo()

rectangulo.primerRectangulo()
rectangulo.segundoRectangulo()
rectangulo.tercerRectangulo()