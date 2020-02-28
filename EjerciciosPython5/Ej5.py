class Libro:
    def __init__(self, titulo, autor, numPags, clasificacion = None):
        self.titulo = titulo
        self.autor = autor
        self.numPags = numPags
        self.clasificacion = range(1, 10)

    def devolverTitulo(self):
        return self.titulo

    def devolverAutor(self):
        return self.autor

    def devolverNumPags(self):
        return self.numPags

    def cambiarTitulo(self):
        self.titulo = input("Inserte el nuevo título del libro")
        print("El título actual del libro es: ").format(self.titulo)

    def cambiarAutor(self):
        self.autor = input("Inserte el nuevo nombre del autor")
        print("El nombre del autor del libro: {} es: {}").format(self.titulo, self.autor)

    def puntuar(self):
        while True:
            self.clasificacion = input("Inserte una puntuación del 1 al 10: ")
            if self.clasificacion > 0 or self.clasificacion < 10:
                print("La clasificación del título {} es ahora de: {} puntos").format(self.titulo, self.clasificacion)
                break
            else:
                print("Inserte un número del 1 al 10 \n")



class ConjuntoLibros:
    def __init__(self, libros = []):
        self.libros = libros

    def anadirLibros(self, libro):
        if len(self.libros) <= 3:
            self.libros.append(libro)
            print("El libro " + str(libro.devolverTitulo()) + " se ha añadido correctamente")
        else:
            print("No es posible insertar más libros en la colección, está llena")

    def eliminarLibros(self, busqueda):
                
        print(str(self.libros))
    

class PruebaLibros:
    libro1 = Libro("Lo que el viento se llevó", "Margaret Mitchell", 1037, 7.00)
    libro2 = Libro("Harry Potter y la piedra filosofal", "J. K. Rowling", 256, 8.00)
    libro3 = Libro("TEO EN EL PARQUE NATURAL", "Violeta Denou", 20, 10.00)
    conjunto = ConjuntoLibros()

    conjunto.anadirLibros(libro1)
    conjunto.anadirLibros(libro2)
    conjunto.anadirLibros(libro3)

    conjunto.eliminarLibros("Lo que el viento se llevó")

prueba = PruebaLibros()

    

    