# Crear la traspuesta de una matriz de n x m.

def MatrizTraspuesta(Matriz):
    if isinstance(Matriz, list) and Matriz != []:
        return MatrizTraspuesta_aux(Matriz, [], [],0, 0, len(Matriz), len(Matriz[0]))
    else: return "Error"

def MatrizTraspuesta_aux(matriz, result, nueva_fila,fila, columna, longitud_fila, longitud_columna):
    if columna == longitud_columna:
        return result
    elif fila == longitud_fila:
        return MatrizTraspuesta_aux(matriz, result + [nueva_fila], [],0, columna+1, longitud_fila, longitud_columna)
    else:
        return MatrizTraspuesta_aux(matriz, result, nueva_fila + [matriz[fila][columna]], fila + 1, columna, longitud_fila, longitud_columna)
