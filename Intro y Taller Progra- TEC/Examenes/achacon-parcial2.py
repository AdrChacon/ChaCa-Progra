#1.- Escriba una funcion que utiliza recursion de cola e indices para invertir
#    una lista de valores ordenados. No puede utilizar una lista adicional ni
#    ni crear otra lista nueva durante la ejecucion del programa


#2.1.- Escriba una funcion que reciba un arreglo cuadrado de enteros de n x n
#      e indique si esta conformado por los numeros consecutivos desde 1 hasta
#      n**2

def consecutivos(matriz):
    if isinstance(matriz, list) and isinstance (matriz[0], list):
        return consecutivos_aux(matriz, 0, 0, len(matriz), len(matriz)**2, 1)
    else: return "Error"

def consecutivos_aux(matriz, fila, columna, max_filas, areamatriz, contador):
    if contador > areamatriz:
        return True
    elif fila == max_filas:
        return False
    elif matriz[fila][columna] == contador:
        return consecutivos_aux(matriz,0,0,max_filas, areamatriz, contador + 1)
    elif columna == max_filas:
        return consecutivos_aux(matriz, fila + 1, 0, max_filas, areamatriz, contador)
    elif matriz[fila][columna] != contador:
        return consecutivos_aux(matriz,fila, columna+1,max_filas,areamatriz,contador)

#2.2.- Escriba una funcion que reciba un arreglo e indique si se trata de
#      un cuadrado magico

def es_magico(matriz):
    if isinstance(matriz, list) and isinstance(matriz[0], list):
        return esmagico(matriz, 0, 0, len(matriz),suma(matriz[0],0,0),0)
    else:
        return "Error"

def suma(lista, indice, result):
    if indice == len(lista):
        return result
    else:
        return suma(lista, indice + 1, result + lista[indice])

def esmagico(matriz,fila,columna,maximo,suma,result):
    if (sumafilas(matriz,fila,columna,maximo,suma,result) and
        sumacolumnas(matriz,fila,columna,maximo,suma,result) and
        sumadiagonal(matriz,fila,columna,maximo,suma,result) and
        sumaantidiagonal(matriz, 0, maximo-1, 0, suma, result)):
        return True
    else:
        return False

def sumafilas(matriz, fila, columna, maximo, suma, result):
    if fila == maximo:
        return True
    elif columna == maximo and result == suma:
        return sumafilas(matriz, fila+1, 0, maximo, suma,0)
    elif columna == maximo and result != suma:
        return False
    else:
        return sumafilas(matriz,fila,columna+1, maximo, suma, result + matriz[fila][columna])

def sumacolumnas(matriz, fila, columna, maximo, suma, result):
    if columna == maximo:
        return True
    elif fila == maximo and result == suma:
        return sumacolumnas(matriz,0,columna+1,maximo,suma,0)
    elif fila == maximo and result != suma:
        return False
    else:
        return sumacolumnas(matriz, fila+1, columna, maximo, suma, result + matriz[fila][columna])

def sumadiagonal(matriz,fila,columna,maximo,suma,result):
    if fila == maximo and result == suma:
        return True
    elif fila == maximo and result != suma:
        return False
    else:
        return sumadiagonal(matriz,fila+1,columna+1,maximo,suma,result + matriz[fila][columna])

def sumaantidiagonal(matriz,fila,columna,maximo,suma,result):
    if columna < maximo and result == suma:
        return True
    elif columna < maximo and result != suma:
        return False
    else:
        return sumaantidiagonal(matriz,fila+1,columna-1,maximo,suma,result+matriz[fila][columna])

# 3.- Escriba una funcion para rotar una matriz de n x m, en donde el ultimo 
#     elemento de la fila i pasa a ser el primer elemento de la columna i,
#     como se muestra en el ejemplo de ejecucion

def rotar(matriz):
    if isinstance(matriz,list) and isinstance(matriz[0],list):
        return rotar_aux(matriz,[],[],0,0,len(matriz),len(matriz[0]))
    else: return "Error"

def rotar_aux(matriz, reordenada, result, fila, columna, max_filas, max_columnas):
    if columna == max_columnas:
        return reordenada
    elif fila == max_filas:
        return rotar_aux(matriz,[result]+reordenada,[],0,columna+1,max_filas,max_columnas)
    else:
        return rotar_aux(matriz,reordenada,[matriz[fila][columna]]+result,fila+1,columna,max_filas,max_columnas)
