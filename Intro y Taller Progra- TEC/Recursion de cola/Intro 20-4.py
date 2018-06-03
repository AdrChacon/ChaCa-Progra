"""
Intro Progra 20/04/2018

1.- Usando recursion de cola, programe una funcion que recibe un numero entero
y elimina los digitos que son divisibles entre 3. Usar recursión de cola
"""

def EliminarImpares(num):
    if isinstance(num, int):
        return EliminarImpares_aux(num, 0, 0)
    else: return "Error"

def EliminarImpares_aux(num, pos, result):
    if num == 0:
        return result
    elif (num%10)%3 == 0: # and (num % 10) != 0: Si cero no es divisible entre 3
        return EliminarImpares_aux(num//10, pos, result)
    else:
        return EliminarImpares_aux(num//10, pos + 1, result + (num%10)*(10**pos))


"""
2.- Hacer una funcion que multiplique los elementos de una lista por
el resultado de las multiplicaciones anteriores """ #Repetida
""""""

def multipLista(lista):
    if isinstance(lista, list) and lista != []:
        return multipLista_aux(lista, 1)
    else: return "Error"

def multipLista_aux(lista, result):
    if lista == []:
        return result
    elif isinstance(lista[0], list):
        return multipLista_aux(lista[0] + lista[1:], result)
    else: return multipLista_aux(lista[1:], result * lista[0])

"""
3.- Programar funcion que recibe una lista y obtenga otra lista con los numeros
pares. Usar indices

"""

def ListaPares(lista):
    if isinstance(lista, list) and lista != 0:
        return ListaPares_aux(lista, [], len(lista)-1)
    else: return "Error"

def ListaPares_aux(lista, resultado, indice):
    if indice == -1:
        return resultado
    elif isinstance(lista[indice], list):
        return ListaPares_aux(lista[indice], [], len(lista[indice]) - 1) + ListaPares_aux(lista, resultado, indice - 1)
    elif lista[indice] % 2 == 0:
        return ListaPares_aux(lista, [lista[indice]] + resultado, indice - 1)
    else:
        return ListaPares_aux(lista, resultado, indice-1)


"""
"""

def ListaPares2(lista):
    if isinstance(lista, list) and lista != 0:
        return ListaPares2_aux(lista, len(lista), [], 0)
    else: return "Error"

def ListaPares2_aux(lista, largo, result, indice):
    if largo == indice:
        return result
    elif lista[indice] % 2 == 0:
        return ListaPares2_aux(lista, largo, result + [lista[indice]], indice + 1)
    else: return ListaPares2_aux(lista, largo, result, indice + 1)












