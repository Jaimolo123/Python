"""Dada una lista de números ordénalos por el número más cercano el promedio de la lista
numeros = [10, 20, 30, 40]"""

numeros = [10, 20, 30, 40]
promedio = sum(numeros) / len(numeros)

def distancia_al_promedio(numero):
    return abs(numero - promedio)
numeros.sort(key=distancia_al_promedio)

print(numeros)

"""cambiooo"""
