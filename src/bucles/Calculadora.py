
def calculadora():
    opcion = 0

    while opcion != 5:
        print("1 sumar")
        print("2 retar")
        print("3 multiplicar")
        print("4 dividir")
        print("5 sair")

        try:
            opcion = int(input("ingrese su opcion: "))


            n1 = int(input("Ingresa un numero: "))
            n2 = int(input("Ingresa un numero: "))

            match (opcion):
                case 1:
                    print(n1 + n2)
                case 2:
                    print(n1 * -n2)
                case 3:
                    print(n1 * n2)
                case 4:
                    print(n1 / n2)
                case _:
                    print("error")

        except ZeroDivisionError:
            print("No se puede dividir por 0 ")
        except ValueError:
            print("error")


calculadora()