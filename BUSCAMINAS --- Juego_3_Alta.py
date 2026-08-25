# Commit 0.1 Creacion del juego 3

# Commit 3.1 crar el tablero y colocar minas

from random import *

perdiste = False
ganaste = False

def crear_tablero():

    tablero = []

    for i in range(5):
        fila = ["?", "?", "?", "?", "?"]
        tablero.append(fila)

    minas = []

    while len(minas) < 4:
        fila = randint(0, 4)
        columna = randint(0, 4)

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

def fuera(fila,columna):
    if fila < 0 or fila > 4 or columna < 0 or columna > 4:
        return True
    else:
        return False

tablero, minas = crear_tablero()

print(minas)

for fila in tablero:
    print(" ".join(fila))

# Commit 3.3 lo mas dificil del codigo crear la interfas del usuario que no vea todo sino solo lo que le corresponde segun las regals del minesweaper

jugadas = 0

# commit 3.4 cree el tablero visible y trabaje con el en la funcion revelar
tablero_visible = []

for i in range(5):
    fila = ["?", "?", "?", "?", "?"]
    tablero_visible.append(fila)

def revelar(fila, columna):

    global jugadas
    global tablero
    global minas
    global tablero_visible
    global perdiste
    global ganaste

    # fuera del tablero
    if fuera(fila, columna):
        return

    # primera jugada
    if jugadas == 0:

        while tablero[fila][columna] != "0":
            tablero, minas = crear_tablero()

        jugadas += 1

    # MUY IMPORTANTE:
    # esto debe funcionar SIEMPRE, no solo en la primera jugada
    if tablero_visible[fila][columna] != "?":
        return

    # si pisa mina
    if tablero[fila][columna] == "X" and mina == 0:
        print("PISASTE UNA MINA")
        perdiste = True
        return

    # revelar primero
    tablero_visible[fila][columna] = tablero[fila][columna]

    # solamente los 0 expanden
    if tablero[fila][columna] == "0":

        for desp_fila in range(-1, 2):
            for desp_columna in range(-1, 2):

                n_fila = fila + desp_fila
                n_columna = columna + desp_columna

                if fuera(n_fila, n_columna):
                    continue

                if tablero[n_fila][n_columna] == "X":
                    continue

                revelar(n_fila, n_columna)

# while del juego: 

while True:
    for fila in tablero_visible:
        print(f"{fila}")

    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    mina = int(input("Mina (1) o no mina (0): "))

    revelar(fila, columna)

    if perdiste:
        print("PISASTE UNA MINA, PERDISTE")
        break

    if ganaste == True:
        print("GANASTE, FELICIDADES")
        break