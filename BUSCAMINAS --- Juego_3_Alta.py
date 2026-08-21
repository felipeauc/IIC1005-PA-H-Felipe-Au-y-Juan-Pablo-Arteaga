# Commit 0.1 Creacion del juego 3

# Commit 3.1 crar el tablero y colocar minas

import random

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


print(minas)

for fila in tablero:
    print(fila)

