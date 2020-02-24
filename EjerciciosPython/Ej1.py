mayor = 0
maximo = 2 #Cantidad de numeros, puede variar
 
for i in range(maximo):
    num = input("Introduce un número entero: ")
    if int(num) > int(mayor):
        mayor = num
 
print(mayor)