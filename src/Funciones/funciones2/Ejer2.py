
def precioEntrada():
    estudiante = input("Eres estudiante responde con si o no: ")
    menor = input("Eres menor: ")
    entradaNormal = 10
    precio = 0

    if estudiante == "si" or menor == "si":
        precio = entradaNormal/2
    else:
        precio = entradaNormal

    return precio

print(precioEntrada())