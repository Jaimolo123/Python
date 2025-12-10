opcion = 0

while opcion != 3:

    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Salir")

    opcion = int(input("Ingresa un numero: "))
    match opcion:
        case 1:
            print( "Ver Perfil")
        case 2:
            print("Editar Perfil")
        case 3:
            print("Salir!!")
        case _:
            print("Escoge una opcion correcta")

