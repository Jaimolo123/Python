def calcularMedia(*args):

    
    if len(args) == 0:
        return "No se recibieron números."

    suma = sum(args)
    promedio = suma / len(args)
    return f"Suma: {suma}, Promedio: {promedio:.2f}"



print(calcularMedia(2, 4, 6, 8))
print(calcularMedia(10, 20))
print(calcularMedia())
