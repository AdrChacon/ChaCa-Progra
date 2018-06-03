# Intro a la programación 16/03/2018
#
# 1.- Hacer funcion que encuentre el valor mínimo en una lista

def Minimo(lista):
    if isinstance(lista, list):
        print("El valor mas bajo en la lista es:", Minimo_aux(lista))
        print("El valor mas alto en la lista es:", Maximo_Op(lista))
    else:
        return "Error: valor ingresado no es una lista"

def Minimo_aux(lista):
    if len(lista) == 1:
        return lista[0]
    elif lista[0] <= lista[1]:
        return Minimo_aux([lista[0]]+lista[2:])
    elif lista[0] > lista[1]:
        return Minimo_aux(lista[1:])

def Maximo_Op(lista):
    if len(lista) == 1:
        return lista[0]
    elif lista[0] >= lista[1]:
        return Maximo_Op([lista[0]] + lista[2:])
    elif lista[0] < lista[1]:
        return Maximo_Op(lista[1:])



# Tarea 3 Intro: Mínimo (no maximo)
#
#2.- Sumar raíz cuadrada de los valores de una lista


def SumaRaices(lista):
    if isinstance(lista, list):
        return SumaRaices_aux(lista)
    else:
        return "Error: valor ingresado no es una lista"

def SumaRaices_aux(lista):
    if lista == []:
        return 0
    else:
        return lista[0]**(1/2) + SumaRaices_aux(lista[1:])

# Tarea 3 Intro: SumaRaices
#----------------------------------------------------------
# Taller Programacion
#
#










