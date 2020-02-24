def recortar(numero, minimo, maximo):
    if numero < minimo:
        numero = minimo
    elif numero > maximo:
        numero = maximo

    return numero


numero = input("Ingresa un número para recortar")
minimo = ("Ingresa el límite mínimo")
maximo = ("Ingresa el límite máximo")

print(recortar(numero, minimo, maximo))