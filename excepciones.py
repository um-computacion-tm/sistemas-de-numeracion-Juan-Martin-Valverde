class NumeroMenorA1Exception(Exception):
    pass

class NumeroMayorA10Exception(Exception):
    pass


def calcular_1_al_10(numero):
    if(numero < 1):
        raise NumeroMenorA1Exception('numero es menor a 1')
    if(numero > 10):
        raise NumeroMayorA10Exception('numero es mayor a 10')
    print('tu numero ' + str(numero) + ' es del 1 al 10')


while True:
    try:
        numero = int(input('ingrese un numero del 1 al 10: '))
        calcular_1_al_10(numero)
        break
    except ValueError as value_error_excepcion:
        print("burro: por favor ingresa un numero")
    except NumeroMayorA10Exception as mi_excepcion:
        print("burro: " + str(mi_excepcion))
    except NumeroMenorA1Exception as mi_excepcion:
        print("burro: " + str(mi_excepcion))
