import collections

class Libro:
    def __init__(self, titulo, autor, numPags, clasificacion = None):
        self.titulo = titulo
        self.autor = autor
        self.numPags = numPags
        self.clasificacion = range(1, 10)

    def devolverTitulo(self):
        print("El título del libro es: " + self.titulo)

    def devolverAutor(self):
        print("El autor es: " + self.autor)

    def devolverNumPags(self):
        print("El libro tiene: " + self.numPags + " páginas")

    def cambiarTitulo(self):
        self.titulo = input("Inserte el nuevo título del libro")
        print("El título actual del libro es: " + self.titulo)

    def cambiarAutor(self):
        self.autor = input("Inserte el nuevo nombre del autor")
        print("El nombre del autor del libro: " + self.titulo + " es: " + self.autor)

    def puntuar(self):
        while True:
            self.clasificacion = input("Inserte una puntuación del 1 al 10: ")
            if self.clasificacion > 0 or self.clasificacion < 10:
                print("La clasificación del título " + self.titulo + " es ahora de: " + self.clasificacion + " puntos")
                break
            else:
                print("Inserte un número del 1 al 10 \n")


class ConjuntoLibros:
    def __init__(self):
        self.libros = collections.deque(maxlen=3)

    def anadirLibros(self, libro):
        self.libros.append(libro)

    


class PruebaLibros:
    libro1 = Libro("Lo que el viento se llevó", "Margaret Mitchell", 1037)
    libro2 = Libro("Harry Potter y la piedra filosofal", "J. K. Rowling", 256)
    conjunto = ConjuntoLibros()

    conjunto.anadirLibros(libro1)
    conjunto.anadirLibros(libro2)

    

    