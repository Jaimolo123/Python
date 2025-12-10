

cadena = input("Introduce una frase")

letra = input("Introduce la letra que quieras buscar")


def existeletra(cadena,letra):
    return letra.lower() in cadena.lower()




def pasarMayuscula(cadena,letra):
    cadena = cadena.lower()

    if existeletra(cadena,letra):
        cadena = cadena.replace(letra.lower() ,letra.upper())
        return cadena

print(pasarMayuscula(cadena,letra))