usuarios = {"Marta", "David", "Elvira", "Marcos"}
administradores = {"Juan", "Marta"}

lista = [usuarios, administradores]

print(lista)

administradores.discard("Juan")

print(lista)

administradores.add("Marcos")

print(lista)

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, " es administrador")
    else:
        print(usuario, " no es administrador")