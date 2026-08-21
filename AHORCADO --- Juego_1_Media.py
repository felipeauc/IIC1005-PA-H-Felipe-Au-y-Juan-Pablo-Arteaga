# Commit 0.1 Creacion del juego 1 

# Commit 1.1 Creacion de la lista de palabras

#1.2
import random

#1.1
archivo = open("palabras.txt", "r")

palabras = archivo.readlines()

archivo.close()

#1.2
palabra_secreta = random.choice(palabras).strip()
print(palabra_secreta)