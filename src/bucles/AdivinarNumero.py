from random import randint


def adivinar():

    n = randint(1,100)

    opcion = 0

    intentos = 0

    while opcion != n and intentos < 6:

        opcion = int(input("Ingresa un numero: "))

        if opcion == n:
            print(f"Has acertado en {intentos} intentos")
        elif opcion > n:
            print(f"El numero es menor")
            intentos += 1
        else:
            print(f"El numero es mayor")
            intentos += 1
    print("Te has quedado sin intentos")


adivinar()