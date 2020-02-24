generos= ["Terror", "Acción", "Aventura"]
edad = input("Introduzca su edad: ")


while True:
        
        print("Opciones:")
        print("Introduzca 1 para " + generos[0])
        print("Introduzca 2 para " + generos[1])
        print("Introduzca 3 para " + generos[2])
        print("Escriba salir para no seleccionar ninguna \n")

        opcion = input("Introduzca la opción que quiere: ")

        if opcion == "1" and int(edad) in range(18, 55):
            print("Ha escogido usted el género " + generos[0] + " \n")
            break

        elif opcion == "1" and int(edad) not in range(18, 55):
            print("No tiene la edad correspondiente a este género, escoja otra o salga \n")

        elif opcion == "2" and int(edad) >= 10:
            print("Ha escogido usted el género "+ generos[1] + " \n")
            break

        elif opcion == "2" and int(edad) < 10:
            print("No tiene la edad correspondiente a este género, escoja otra o salga \n")
        
        elif opcion == "3" and int(edad) >= 4:
            print("Ha escogido usted el género " + generos[2] + " \n")
            break

        elif opcion == "3" and int(edad) < 4:
            print("No tiene la edad correspondiente a este género, escoja otra o salga \n")

        elif opcion == "salir":
            print("Adiós! \n")
            break

        else:
            print("Ha escogido una opción no válida, por favor introduzca una opción de la lista \n")
