# Calcular la serie de Fibonacci para un numero. Se debe validar que el numero es entero positivo.


def Fibonacci(num):
    if isinstance(num, int) and (num > 0):
        return Fibonacci_Aux(abs(num))
    else:
        return "Error"


def Fibonacci_Aux(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        print((num - 1) + (num - 2))
        return Fibonacci_Aux(num - 1) + Fibonacci_Aux(num - 2)


###
###
###


def SumaHasta(num):
    if isinstance(num, int) and (num > 0):
        return SumaHasta_aux(abs(num))
    else:
        return "Error"


def SumaHasta_aux(num):
    if num == 0:
        return 0
    else:
        return num + SumaHasta_aux(num - 1)
#Plantilla = tarea de intro
