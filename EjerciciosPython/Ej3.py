vocales = ['a', 'e', 'i', 'o', 'u']

caracter = input("Introduce un caracter para saber si es una vocal o no ")

if caracter in vocales:
    print("El caracter " + caracter + " es una vocal")
else:
    print("El caracter " + caracter + " no es una vocal")

