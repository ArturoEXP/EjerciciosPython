num = int(input("Introduce un número para saber si es múltiplo de 3 o 5 : "))

if(num % 3 == 0 and num % 5 == 0):
    print("El número " + str(num) + " es múltiplo de 3 y 5")
else:
    print("El número "+ str(num) + " no es múltiplo de 3 y 5")