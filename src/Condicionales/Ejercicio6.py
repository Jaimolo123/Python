try:
    n = int(input("Introduce el numero "))

    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")
except:
    print(f"Introduce un valor entero")