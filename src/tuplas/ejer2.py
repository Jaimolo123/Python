import math


def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

punto1 = (1, 2)
punto2 = (4, 6)

print(distancia(punto1, punto2))  
