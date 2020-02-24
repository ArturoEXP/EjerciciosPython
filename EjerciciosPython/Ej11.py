estaciones = ['Verano', 'Otoño', 'Invierno' , 'Primavera']

print('1 para Verano \n')
print('2 para Otoño \n')
print('3 para Invierno \n')
print('4 para Primavera \n')
print('salir para terminar el programa \n')

while True:
    opcionMenu = input('Ingresa un número del 1 al 4 o escriba salir: ')

    if opcionMenu == '1':
        print(estaciones[0] + '\n')
    
    elif opcionMenu == '2':
        print(estaciones[1] + '\n')
    
    elif opcionMenu == '3':
        print(estaciones[2] + '\n')

    elif opcionMenu == '4':
        print(estaciones[3] + '\n')

    elif opcionMenu == 'salir':
        print("Adiós! \n")
        break

    else:
        print("Tecla incorrecta! Inténtelo de nuevo! \n")



