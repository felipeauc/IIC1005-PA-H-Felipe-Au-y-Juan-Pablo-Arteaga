# Commit 0.1 Creacion del juego 3

# Commit 3.1

import random

tablero = []

for i in range(5):
    fila = ["?", "?", "?", "?", "?"]
    tablero.append(fila)

minas = []

while len(minas) < 5:
    fila = random.randint(0, 4)
    columna = random.randint(0, 4)
    if (fila, columna) not in minas:
        minas.append((fila, columna))
        
print(minas)