notas = [4,6,7,2,3,5]

aprobados = 0

acomulador = 0

for numero in notas:
    if numero >= 5:
        aprobados += 1
    acomulador += numero

print(f"El numero de aprobados es {aprobados}")

print(f"La media es {acomulador/len(notas)}")

print(f"La nota mas alta es {max(notas)}")

print(f"La nota menos alta es {min(notas)}")