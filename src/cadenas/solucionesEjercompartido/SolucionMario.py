
cadena = input("Introduce una frase")

if len(cadena) >5:
    cadena = cadena[::-1]
    print(cadena)
else:
    print("La cadena no es lo suficientemente larga como para invertirla")
