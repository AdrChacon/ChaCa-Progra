# Calcular la suma de todos los valores de una matriz de n x m y determinar el valor promedio de estos.

def SumaMatriz(matriz):
    if isinstance(matriz, list):
        return SumaMatriz_aux(matriz, 0, 0, 0, len(matriz), len(matriz[0]))
    else: return "Error"

def SumaMatriz_aux(matriz, fila, columna, result, Longitud_fila, Longitud_columna):
    if fila == Longitud_fila:
        return result / (Longitud_fila*Longitud_columna)
    elif columna == Longitud_columna:
        return SumaMatriz_aux(matriz, fila+1, 0, result, Longitud_fila, Longitud_columna)
    else:
        return SumaMatriz_aux(matriz, fila, columna+1, result + matriz[fila][columna], Longitud_fila, Longitud_columna)
