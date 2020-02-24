def relacion(a, b):
    if a>b:
        return 1

    elif a<b:
        return -1

    else:
        return 0

a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")

print(relacion(a, b))