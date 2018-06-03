"""
Intro - 27/04/2018
"""

# #1: Busqueda lineal de elementos: dado un elemento, recorra una lista para
# determinar si este se encuentra en la lista. Búsqueda lineal de elementos.
# Utilice índices.

def Comparar(num, lista):
    if isinstance(lista, list) and lista != []:
        return Comparar_aux(num, lista, len(lista), 0)
    else: return "Error"

def Comparar_aux(num, lista, largo, indice):
    if indice == largo:
        return False
    elif num == lista[indice]:
        return True
    else:
        return Comparar_aux(num, lista, largo, indice+1)

# #2: #1 con slicing

def CompararSli(num, lista):
    if isinstance(lista, list) and lista != []:
        return CompararSli_aux(num, lista)
    else: return "Error"

def CompararSli_aux(num, lista):
    if lista == []:
        return False
    elif num == lista[0]:
        return True
    else:
        return CompararSli_aux(num, lista[1:])

# #3: Realice una busqueda binaria de elementos en una lista ordenada.
#     Utilice índices.

def Busqueda(num, lista):
    if isinstance(lista, list) and lista != []:
        return Busqueda_aux(num, lista, len(lista)//2)
    else: return "Error"

def Busqueda_aux(num, lista, mitad):
    if lista == []:
        return False
    elif num == lista[mitad]:
        return True
    elif num > lista[mitad]:
        return Busqueda_aux(num, lista[(mitad+1):], (len(lista[(mitad+1):])-1)//2)
    elif num < lista[mitad]:
        return Busqueda_aux(num, lista[:(mitad)], (len(lista[(mitad):])-1)//2)
        














