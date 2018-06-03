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
