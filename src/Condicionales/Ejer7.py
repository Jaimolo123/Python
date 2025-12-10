try:
    edad = int(input("Introduce la edad: "))

    match edad:
        case _ if edad < 0:
            print("La edad no puede ser negativa")
        case _ if edad < 14:
            print("No puede conducir")
        case _ if edad < 16:
            print("Moto de poca cilindrada")
        case _ if edad < 18:
            print("Moto de gran cilindrada")
        case _:
            print("Puede conducir coches")

except ValueError:
    print("Introduce un valor entero válido")
