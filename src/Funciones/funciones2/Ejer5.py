def contarArgumentos(*args):
    contador = 0
    for numero in args:
        contador += 1
    return contador

print(contarArgumentos(1,2,3,3,3,4))