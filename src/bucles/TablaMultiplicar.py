try:
    n = int(input("Ingresa un numero: "))


    for numero in range(1,11):
        numero2 = n * numero
        print(f"{n}*{numero} = {numero2}")
except ValueError:
    print("Ingresa un numero")