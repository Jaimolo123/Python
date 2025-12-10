
try:

    saldo = int (input("Introduce el saldo de la cuenta bancaria: "))

    retirada = int(input("Introduce la cantidad que quieras retirar: "))

    saldo = saldo - retirada

    print(saldo)



except ValueError:
    print("El valor ingresado no es un numero")

except:
    if saldo < retirada:
        print("No se puede retirar mas de lo que hay")