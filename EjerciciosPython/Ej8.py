lista = []
num = 0
max = 3

for i in range(max):
    num = input("Ingresa un número: ")
    lista.append(num)

lista.sort()

for numero in lista:
  print(numero)
