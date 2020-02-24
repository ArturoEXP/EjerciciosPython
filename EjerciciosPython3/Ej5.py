def separar(lista):
    listaPares = []
    listaImpares = []

    for elemento in lista:
        if elemento%2 == 0:
            listaPares.append(elemento)
        else:
            listaImpares.append(elemento)

    return listaPares, listaImpares

lista = [25, 35, 44, 66, 15, 98, 74]

print(separar(lista))
