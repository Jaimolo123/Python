
n_anios = int (input("Ingresa el numero de años"))
interes = int(input("Ingresa el interes"))

cantidad = int(input("Ingresa el cantidad"))


porcentaje = interes/100


for n in range(n_anios):

    subida = porcentaje * cantidad
    cantidad += subida

    print(f"Interes del año {n+1} es {cantidad}")