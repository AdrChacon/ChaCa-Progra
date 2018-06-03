# Calcular la suma de todos los valores de una matriz de n x m y determinar el valor promedio de estos.

def PromedioMatriz(matriz):
    if isinstance(matriz, list) and matriz != []:
        return PromedioMatriz_aux(matriz, 0, 0, 0, len(matriz), len(matriz[0]))
    else: return "Error"

def PromedioMatriz_aux(matriz, fila, columna, result, Longitud_fila, Longitud_columna):
    if fila == Longitud_fila:
        return result / (Longitud_fila*Longitud_columna)
    elif columna == Longitud_columna:
        return PromedioMatriz_aux(matriz, fila+1, 0, result, Longitud_fila, Longitud_columna)
    else:
        return PromedioMatriz_aux(matriz, fila, columna+1, result + matriz[fila][columna], Longitud_fila, Longitud_columna)
