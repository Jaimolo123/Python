try:
    n1 = int (input("Introduce un numero: "))
    n2 = int (input("Introduce un numero: "))

    if n1 > n2:
        print(f"{n1} es mayor que {n2}.")
    elif n1 < n2:
        print(f"{n2} es mayor que {n1}.")
    else:
        print(f"{n1} es igual a {n2}.")
except ValueError:
    print("El valor debe de ser un numero")