
def analizar_texto(texto):
    contador = 0
    primera_palabra = texto.split()[0]
    texto_0espacios = texto.replace(' ', '')
    lista = []


    for palabra in texto.split():
        contador += 1
    for palabra in texto:
        lista.append(palabra)

    mi_tupla = (len(texto_0espacios), contador,primera_palabra)
    return mi_tupla


print(analizar_texto("Hola mundo"))

