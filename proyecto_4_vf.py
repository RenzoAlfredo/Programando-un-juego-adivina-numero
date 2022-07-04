## PROGRAMANDO EL JUEVO 'ADIVINA EL NUMERO'
from random import randint
nombre = input('¿cual es tu nombre? ')
print(f'{nombre}, he pensado en un numero entre el 1 y el 100 \n y tienes 8 intententos para adivinar cual es el numero')
n = 8
nro_intentos = n
aleatorio = randint(1,101)
intentos = []
intentos_validos = []
while nro_intentos > 0:
    intentos.append(int(input(f"ingresa el valor de tu intento numero {nro_intentos} ")))
    if (intentos[-1] < 1 or intentos[-1] > 100):
        print("Numero fuera del rango permitido")
    else:
        intentos_validos.append(intentos[-1])
        if intentos_validos[n-nro_intentos] == aleatorio:
            print("Numero adivinado, GANASTE!")
            break
        elif intentos_validos[n-nro_intentos] < aleatorio:
            print('El numero ingresado es menor al numero secreto')
        elif intentos_validos[n-nro_intentos] > aleatorio:
            print('El numero ingresado es mayor al numero secreto')
        nro_intentos -= 1
        print(f'tus intentos hasta ahora: {intentos_validos} \n le quedan {nro_intentos} intentos ')

if nro_intentos == 0:
    print(f'los intenteos ingresados {intentos} no acertaron \n PERDISTE :( \n el numero secreto era {aleatorio}')

