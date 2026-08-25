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

                for mina_pos in minas:

                    if abs(mina_pos[0] - fila) <= 1 and abs(mina_pos[1] - columna) <= 1:
                        contador += 1

                tablero[fila][columna] = str(contador)

    return tablero, minas

def fuera(fila, columna):

    if fila < 0 or fila > 4 or columna < 0 or columna > 4:
        return True

    else:
        return False

tablero, minas = crear_tablero()

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

    # primera jugada tiene que ser 0 todos los buscaminas web son asi

    if jugadas == 0 and mina == 0:

        while tablero[fila][columna] != "0":
            tablero, minas = crear_tablero()

        jugadas += 1

    # no revelar una casilla que ya esta revelada

    if tablero_visible[fila][columna] != "?":
        return

    # si dice que es mina pero NO es mina, pierde

    if mina == 1 and tablero[fila][columna] != "X":
        print("MARCASTE COMO MINA UNA CASILLA QUE NO ERA MINA")
        perdiste = True
        return

    # si dice que es mina y SI es mina, la marca

    if mina == 1 and tablero[fila][columna] == "X":
        tablero_visible[fila][columna] = "X"
        return


    # si pisa mina sin marcarla

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

    print("\n    0  1  2  3  4")
    print("   ---------------")

    for i in range(5):
        print(i, "|", end=" ")

        for j in range(5):
            print(tablero_visible[i][j], end="  ")

        print()

    try:
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        mina = int(input("Mina (1) o no mina (0): "))

    except:
        print("Por favor, ingrese valores válidos.")
        continue


    revelar(fila, columna)


    # comprobar si perdio

    if perdiste:
        for i in range(5):
                print(i, "|", end=" ")
        
                for j in range(5):
                    print(tablero_visible[i][j], end="  ")
        
                print()
        print("PISASTE UNA MINA, PERDISTE")
        break


    # comprobar si gano

    revelado = 0
    bomba = 0

    for f in range(5):
        for c in range(5):

            if tablero[f][c] != "X" and tablero_visible[f][c] != "?":
                revelado += 1

            if tablero[f][c] == "X" and tablero_visible[f][c] == "X":
                bomba += 1


    if revelado == 25 - len(minas) or bomba == len(minas):
        ganaste = True


    if ganaste:
        for i in range(5):
                print(i, "|", end=" ")
        
                for j in range(5):
                    print(tablero_visible[i][j], end="  ")
        
                print()
        print("FELICIDADES, GANASTE")
        break