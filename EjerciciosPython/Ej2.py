x = input("Introduce un número entero: ")

if int(x) == 0:
    print ('El número ' + x + ' es un número neutro')
elif int(x) < 0:
    print ('El número ' + x + ' es un número negativo')
else:
    print ('El número ' + x + ' es un número positivo')