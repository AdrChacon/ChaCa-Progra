def sumartodo(lista):
    if isinstance(lista,list):
        return sumartodo_aux(lista)
    else: return "Error"

def sumartodo_aux(lista):
    if lista == []:
        return 0
    elif isinstance(lista[0], int):
        return lista[0] + sumartodo_aux(lista[1:])
    else: return listalista(lista[0]) + sumartodo_aux(lista[1:])

def listalista(lista):
    if lista == []:
        return 0
    else: return lista[0] + listalista(lista[1:])
