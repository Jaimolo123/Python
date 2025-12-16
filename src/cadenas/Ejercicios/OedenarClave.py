"""Ordenar la lista de estudiantes por la nota"""
estudiantes = [
    ["Ana", 22, 8.5],
    ["Luis", 20, 7.0],
    ["Marta", 21, 9.2],
    ["Carlos", 23, 6.8]
]

def clave_nota(estudiante):
    return estudiante[2]

estudiantes.sort(key=clave_nota)

print(estudiantes)

