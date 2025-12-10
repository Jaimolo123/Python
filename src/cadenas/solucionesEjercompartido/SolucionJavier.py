
palabra = input("Introduce una palabra y te dire si es un anagrama: ")

inversa = palabra[::-1]

if palabra == inversa:
    print("El palabra es un anagrama")
else:
    print("El palabra no es un anagrama")