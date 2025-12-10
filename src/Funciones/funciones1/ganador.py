from operator import index
from random import randint
def ganador(*participantes):

    aleatorio = randint(0,len(participantes)-1)
    for indice,participante in enumerate(participantes):
        if indice  == aleatorio:
            return participante
print(ganador("pepe","mario","juan","pedro"))