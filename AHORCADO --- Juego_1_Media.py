# Commit 0.1 Creacion del juego 1 

# Commit 1.1 Creacion de la lista de palabras

#1.2
import random

#1.1
archivo = open("palabras.txt", "r")

palabras = archivo.readlines()

archivo.close()

inputs = []

#1.2
palabra_secreta = random.choice(palabras).strip()


#1.3
mostrar = ""
for letra in palabra_secreta:
    if letra == " ":
        mostrar += " "
    else:
        mostrar += "_"

#1.5 dibujo del colgado
colgado_6 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
   /|\  |\n
   / \  |\n        
===========
"""

colgado_5 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
   /|\  |\n
   /    |\n        
===========
"""
colgado_4 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
   /|\  |\n
        |\n        
===========
"""

colgado_3 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
   /|   |\n
        |\n        
===========
"""

colgado_2 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
    |   |\n
        |\n        
===========
"""

colgado_1 = """
===========\n
    +---+\n
    |   |\n
    O   |\n
        |\n
        |\n        
===========
"""

colgado_0 = """
===========\n
    +---+\n
    |   |\n
        |\n
        |\n
        |\n        
===========
"""

#1.4
intentos = 6

#1.5
contador = 0

#1.4
#Core del juego
print("¡Bienvenido al juego del ahorcado!\n")
while intentos > 0 and "_" in mostrar:
    print(mostrar)
    if len(palabra_secreta) == contador:
        break
    print(locals().get(f"colgado_{intentos}"))
    print(f"Intentos restantes: {intentos}")
    
    letra_usuario = input("Ingrese una letra/frase: ").lower()
    
    if letra_usuario == palabra_secreta:
        break
    else:
        if letra_usuario in inputs:
            print('Ya intentaste esa letra')
        elif letra_usuario in palabra_secreta:
            print("¡Correcto!")
            inputs.append(letra_usuario)
            contador += 1
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra_usuario:
                    mostrar = mostrar[:i] + letra_usuario + mostrar[i+1:]
        else:
            print("¡Incorrecto!")
            inputs.append(letra_usuario)
            intentos -= 1
    
#1.5
if len(palabra_secreta) >= contador and intentos > 0:
    print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
else:
    print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")
