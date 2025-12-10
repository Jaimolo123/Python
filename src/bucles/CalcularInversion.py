def calcularInversion():
    try:
        inversion = int (input("Inversion: "))
        interes = int (input("Intres: "))
        nAnios = int(input("Total de años"))

    except ValueError:
        print("Introduce un valor entero")

calcularInversion()