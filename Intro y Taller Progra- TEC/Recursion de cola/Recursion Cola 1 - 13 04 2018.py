"""
Intro Progra 13/04/2018
"""

def largo(num):
    if isinstance(num, int):
        return largo_aux(num, 0)
    else:
        return "Error: el numero no es un entero"

def largo_aux(num, resultado):
    if (num == 0):
        return resultado
    else:
        return largo_aux(num // 10, resultado + 1)

"""
Hacer funcion que reciba numero entero y elimine digitos que sean divisibles
entre 3
"""

def DivisibleTres(num):
    if isinstance(num, int):
        return DivisibleTres_aux(num, 0, 0)
    else: "Error"

def DivisibleTres_aux(num, result, pot):
    if num == 0:
        return result
    elif (num%10)%3 == 0:
        return DivisibleTres_aux(num//10, result, pot)
    else:
        return DivisibleTres_aux(num//10, result + (num%10)*10**pot, pot+1)

"""
Funcion que multiplique los elementos de una lista por el resultado
de multiplicaciones previas usando slicing
"""

def Multip(lista):
    if isinstance(lista,list):
        return Multip_aux(lista, 1)
    else: return "Error"

def Multip_aux(lista, resultado):
    if lista == []:
        return resultado
    elif isinstance(lista[0], list):
        return Multip_aux(lista[0] + lista[1:], resultado)
    else: return Multip_aux(lista[1:], resultado * lista[0])







