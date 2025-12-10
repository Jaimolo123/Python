from itertools import product

inventario = {}
opcion = 0

cantidad = 0
product = " "

retirada = 0

try:
    while opcion != 4:

        print("1-Añadir stock")
        print("2-Vender producto")
        print("3-Mostrar inventario")
        print("4-Salir del programa")
        opcion = int(input("Introduce una opcion "))

        match(opcion):
            case 1:
                cantidad = int(input("Introduce la cantidad "))
                product = input("Introduce el producto ")
                inventario.update({product: cantidad})
            case 2:
                retirada = int(input("Introduce la retirada "))
                product = input("Introduce el producto ")

                inventario.update({product: retirada})
            case 3:
               print(inventario)
            case 4:
                print("Saliendo del programa")
            case _:
                print("Introduce una opcion valida")

except KeyboardInterrupt:
    print("error")