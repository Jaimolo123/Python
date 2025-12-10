frase = input("Ingresa una frase: ")

fraseMinuscula = frase.lower()

fraseMayuscula = frase.upper()

fraseInvertida = frase[::-1]

contador = 0
for i in frase:
    if i ==  'a' or i == "A":
        contador += 1


print(fraseMinuscula)
print(fraseMayuscula)
print(fraseInvertida)
print(f"La letra a aparece {contador} veces")