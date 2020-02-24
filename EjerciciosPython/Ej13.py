num1 = input("Introduce un número mínimo para el rango: ")

num2 = input("Introduce un número máximo para el rango: ")

lista = list(range(int(num1), int(num2)))

for elemento in lista:
    if elemento%2 == 1:
        lista.remove(elemento)

print (len(lista))