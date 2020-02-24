def intermedio(a, b):
    intermedio = int(a) + int(b)
    intermedio = int(intermedio) / 2

    return intermedio

print("Introduzca dos números para hallar el intermedio")
a = input("introduzca el primer número: ")
b = input("Introduzca el segundo número: ")

print(intermedio(a, b))