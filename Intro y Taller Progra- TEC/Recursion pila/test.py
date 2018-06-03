"""
Intro 06/04/2018
"""


def ExPosicion(lista):
    if isinstance(lista, list) and len(lista) > 0:
        return ExPosicion_aux(lista, 0)
    else: return 'Error'

def ExPosicion_aux(lista, num):
    if lista == []:
        return 0
    elif isinstance(lista[0], list):
        return ExPosicion_aux(lista[0] + lista[1:], num)
#        return ExPosicion_aux(lista[0], num) + ExPosicion_aux(lista[1:], num+len(lista[0]))
    else:
        num +=1
        return lista[0]**(num) + ExPosicion_aux(lista[1:], num)

"""
Taller

185412
"""

def Intercambiar(num):
    if isinstance(num, int):
        return Intercambiar_aux(num, 0)
    else: return "Error"

def Intercambiar_aux(num, pot):
    if num == 0:
        return 0
    else: return (num%10)*(10**(pot+1))+(num%100//10)*(10**(pot)) + Intercambiar_aux(num//100, pot+2)

"""
---
"""

def Multiplicaciones(lista):
    if isinstance(lista, list):
        return Multiplicaciones_aux(lista, 0)
    else: return "Error"

def Multiplicaciones_aux(lista, pos):
    if lista == []:
        return []
    else: return [lista[0]*pos]+Multiplicaciones_aux(lista[1:], pos+1)



