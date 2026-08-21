# Commit 0.1 Creacion del juego 3

# Commit 3.1 crar el tablero y colocar minas

import random


def crear_tablero(tablero, minas):

    tablero = []

    for i in range(5):
        fila = ["?", "?", "?", "?", "?"]
        tablero.append(fila)

    minas = []

    while len(minas) < 4:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)

        if (fila, columna) not in minas:
            minas.append((fila, columna))


    # Commit 3.2 asiganr valores a cada celada segun cuantas minas en el alrededor

    for fila in range(5):
        for columna in range(5):

            if (fila, columna) in minas:
                tablero[fila][columna] = "X"

            else:
                contador = 0

                for mina in minas:

                    if abs(mina[0] - fila) <= 1 and abs(mina[1] - columna) <= 1:
                        contador += 1

                tablero[fila][columna] = str(contador)

    return tablero, minas


tablero = []
minas = []

tablero, minas = crear_tablero(tablero, minas)


print(minas)

for fila in tablero:
    print(" ".join(fila))

# Commit 3.3 lo mas dificil del codigo crear la interfas del usuario que no vea todo sino solo lo que le corresponde segun las regals del minesweaper

jugadas = 0

def revelar(fila, columna):

    global jugadas
    global tablero
    global minas

    # viendo el buscaminas nos dimos cuenta que el primer intento siempre es en un 0

    if fila < 0 or fila > 4 or columna < 0 or columna > 4:
        print("Estas fuera del tablero")
        return

    if jugadas == 0:

        while tablero[fila][columna] != "0":
            tablero, minas = crear_tablero(tablero, minas)

        jugadas += 1

    else:

        if tablero[fila][columna] == "X":
            print("Pisaste una mina")

        else:
            pass