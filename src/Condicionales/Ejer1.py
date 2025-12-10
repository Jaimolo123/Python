try:
    edad = int(input("Ingrese edad: "))

    if edad < 0:
        print("La edad no puede ser negativa")
    else:
        if edad < 18:
            print("La persona es menor de edad")
        else:
            print("La persona es mayor de edad")

except ValueError:
    print("La edad no es válida. Debe ser un número entero positivo.")
