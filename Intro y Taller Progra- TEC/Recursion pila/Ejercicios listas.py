# 14 / 03 / 2018

def suma(lista):
    # if type(lista) == list
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: el valor ingresado no es una lista"

def suma_aux(lista):
    if lista == [] :
        return 0
    else:
        return lista[0] + suma_aux(lista[1:])

###
### Sumar todos los numeros pares de una lista
###

def SumaParesImpares(lista):
    if isinstance(lista, list):
        print("La suma de los numeros pares es:" , SumaPares_aux(lista))
        print("La suma de los numeros impares es:" , SumaImpares_aux(lista))
    else:
        return "Error: valor ingresado no es una lista"

def SumaPares_aux(lista):
    if lista == [] :
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + SumaPares_aux(lista[1:])
    else:
        return SumaPares_aux(lista[1:])

def SumaImpares_aux(lista):
    if lista == [] :
        return 0
    elif lista[0] % 2 == 1:
        return lista[0] + SumaImpares_aux(lista[1:])
    else:
        return SumaImpares_aux(lista[1:])

###
### Pasar a plantilla de suma y sumapares = intro
###----------------------------------------------------------------------------------------------------------
###----------------------------------------------------------------------------------------------------------
###----------------------------------------------------------------------------------------------------------
###                     Taller
### Pasar a plantilla
###

def TieneCero(lista):
    if isinstance(lista, list):
        return TieneCero_aux(lista)
    else:
        return "Error: valor ingresado no es una lista"

def TieneCero_aux(lista):
    if lista == []:
        return False
    elif lista[0] == 0:
        return True
    else: return TieneCero_aux(lista[1:])

#
# ElementoPositivo =/= tarea
#

def ElementoPositivo(lista):
    if isinstance(lista, list):
        return ElementoPositivo_aux(lista)
    else:
        return "Error: valor ingresado no es una lista"

def ElementoPositivo_aux(lista):
    if lista == []:
        return True
    elif lista[0] < 0:
        return False
    else: return ElementoPositivo_aux(lista[1:])

#
# Lista y eliminar = Tarea
#

def Eliminar(lista, num):
    if isinstance(lista, list):
        return Eliminar_aux(lista, num)
    else:
        return "Error: valor ingresado no es lista"

def Eliminar_aux(lista, num):
    if lista == []:
        return []
    elif lista[0] == num:
        return Eliminar_aux(lista[1:], num)
    else: return [lista[0]] + Eliminar_aux(lista[1:], num)

