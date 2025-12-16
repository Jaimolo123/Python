
palabra = input("Introduce una palabra y te dire si es un palindromo: ")

palabra = palabra.replace(" ", "")
palabra = palabra.lower()



inversa = palabra[::-1]

if palabra == inversa:
    print("El palabra es un palindromo")
else:
    print("El palabra no es un palindromo-")