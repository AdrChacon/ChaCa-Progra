"""
Intro - 25/04/2018
"""

#  1.-Hacer dos funciones que reciben una lista y obtienen el numero mayor y
#     menor. Utilizar indices.

def MayorMenorLista(lista):
    if isinstance(lista, list) and lista != []:
        print("El número mayor en la lista es:", MayorLista(lista, 0, 0, len(lista)))
        print("El número menor en la lista es:", MenorLista(lista, 0, 0, len(lista)))
        return
    else: return "Error"

def MayorLista(lista, indice, mayor, largo):
    if indice == largo:
        return lista[mayor]
    elif lista[mayor] >= lista[indice]:
        return MayorLista(lista, indice+1, mayor, largo)
    elif lista[mayor] < lista[indice]:
        return MayorLista(lista, indice+1, indice, largo)

def MenorLista(lista, indice, menor, largo):
    if indice == largo:
        return lista[menor]
    elif lista[menor] >= lista[indice]:
        return MenorLista(lista, indice+1, indice, largo)
    elif lista[menor] < lista[indice]:
        return MenorLista(lista, indice+1, menor, largo)

# 2.- Hacer #1 con slicing

def MayMenLista(lista):
    if isinstance(lista, list) and lista != []:
        print("El número mayor en la lista es:", MayLista(lista, lista[0],))
        print("El número menor en la lista es:", MenLista(lista, lista[0],))
        return
    else: return "Error"

def MayLista(lista, result):
    if lista == []:
        return result
    elif result >= lista[0]:
        return MayLista(lista[1:], result)
    elif result < lista[0]:
        return MayLista(lista[1:], lista[0])

def MenLista(lista, result):
    if lista == []:
        return result
    elif result >= lista[0]:
        return MenLista(lista[1:], lista[0])
    elif result < lista[0]:
        return MenLista(lista[1:], result)



























