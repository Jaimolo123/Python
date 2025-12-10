try:
    nota = float (input("Introduce un numero: "))

    match nota:
        case n if nota>=0 and nota<5:
            print("suspenso")
        case n if nota>=5 and nota<7:
            print("aprobado")
        case n if nota>=7 and nota<9:
            print("notable")
        case n if nota>=9 and nota<10:
            print("sobresaliente")
        case _:
            print("Introduce un valor entre 0 y 10")
except ValueError:
    print("Introduce un valor numerico")