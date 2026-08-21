from time import *
from random import *

lista_operaciones = ['+', '-', '*']

def calculo():
    operacion = lista_operaciones[randint(0,2)]

    if operacion == '+':
        num1 = randint(100, 999)
        num2 = randint(100, 999)
        return operacion, num1, num2, num1 + num2

    elif operacion == '-':
        num1 = randint(100, 999)
        num2 = randint(100, 999)
        return operacion, max(num1, num2), min(num1, num2), abs(num1 - num2)

    elif operacion == '*':
        num1 = randint(10, 99)
        num2 = randint(10, 99)
        return operacion, num1, num2, num1 * num2

inicio = time()

for i in range(10):
    res = calculo()
    operacion, num1, num2, respuesta = res[0], res[1], res[2], res[3]

    bien = False

    while not bien:
        res_jugador = int(input(f'{num1} {operacion} {num2} = ?'))
        if res_jugador == respuesta:
            print('Bien hecho!!')
            bien = True
        else:
            print('Intenta nuevamente.')

termino = time()

tiempo_calcular = termino - inicio

print('------- Terminaste las 10 operaciones -------')
print(f'--- Has demorado un total de {tiempo_calcular} segundos ---')