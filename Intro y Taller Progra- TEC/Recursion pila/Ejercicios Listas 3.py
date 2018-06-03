# 21/03/2018
# Intro Progra
# 1 - Programar una funcion que recibe como parametro una lista de numeros,
# determinar cuales numeros son primos y regresa una lista que contiene solo
# los numeros primos. Utilice una funcion para verificar la entrada, otra para
# determinar cuando un numero es primo y otra para devolver la lista con el
# resultado. [15,7,8,11,13]
# Tarea - Pasar a plantilla

def NumerosPrimos(lista):
    if isinstance(lista, list):
        return NumerosPrimos_aux(lista)
    else:
        return "Error: valor ingresado no es una lista"

def NumerosPrimos_aux(lista):
    if lista == []:
        return []
    elif Primo(lista[0], lista[0] - 1):
        return [lista[0]] + NumerosPrimos_aux(lista[1:])
    else:
        return NumerosPrimos_aux(lista[1:])

def Primo(num, div):
    if num == 0 or num == 1 or num == 2 or num == 3:
        return True
    elif div == 1:
        return True
    elif num % div == 0:
        return False
    else: return Primo(num, div - 1)

#
#
#
    
