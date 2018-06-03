"""
02/05/2018 - Intro
"""

# #1: Dada una lista, crear una funcion para ordenar sus elementos. Utilice
# recursión de cola e índices.

def ordenar(lista):
    if isinstance(lista, list) and lista != []:
        return ordenar_aux(lista, 0, 0)
    else: return "Error"

def ordenar_aux(lista, indice1, indice2):
    if indice2 == len(lista) - 1:
        return lista
    elif indice1 == len(lista) - 1:
        return ordenar_aux(lista, 0, indice2 + 1)
    elif lista[indice1] > lista[indice1 + 1]:
        aux = lista[indice1]
        lista[indice1] = lista[indice1 + 1]
        lista[indice1 + 1] = aux

        return ordenar_aux(lista, indice1 + 1, indice2)
    else: return ordenar_aux(lista, indice1 + 1, indice2)


#
#

def suma_matriz(elem, matriz):
    if isinstance(matriz, list) and matriz != [] and isinstance(elem, int):
        return matriz_aux(elem, matriz, len(matriz), len(matriz[0]), 0, 0,[],[])
    else: return "Error"

def matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna,suma,f):
    if fila == num_filas:
        return suma
    elif columna == num_columnas:
        return matriz_aux(elemento, matriz, num_filas, num_columnas, fila + 1, 0, suma + [f], [])
    else: return matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna + 1, suma, f + [matriz[fila][columna] + elemento])











