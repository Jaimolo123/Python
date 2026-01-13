
lista = [1,21,3,4]

def  calcular_estadisticas(numeros):
    tupla =(min(numeros), max(numeros), sum(numeros)/len(numeros))
    return tupla

print(calcular_estadisticas(lista))