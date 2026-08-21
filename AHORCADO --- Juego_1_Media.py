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

#1.3
mostrar = ""
for letra in palabra_secreta:
    if letra == " ":
        mostrar += " "
    else:
        mostrar += "_"

print(mostrar)

#1.4
intentos = 6

#Core del juego
while intentos > 0 and "_" in mostrar:
    print(f"Intentos restantes: {intentos}")
    letra_usuario = input("Ingrese una letra: ").lower()

    if letra_usuario in palabra_secreta:
        print("¡Correcto!")
                  
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra_usuario:
                mostrar = mostrar[:i] + letra_usuario + mostrar[i+1:]
    else:
        print("¡Incorrecto!")
        intentos -= 1

    print(mostrar)