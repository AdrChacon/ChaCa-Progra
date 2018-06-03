#
# Intro Progra 04/04/2018
#
# Ejemplo

def revise_num(num):
    if isinstance(num,int):
        entre0y4 = lambda digito : digito <=4
        entre5y9 = lambda digito : digito >=5
        return revise_aux(num, entre0y4), revise_aux(num, entre5y9)
    else: return "Error"

def entreCeroyCuatro(digito):
    return digito <=4

def entreCincoyNueve(digito):
    if digito >=5:
        return True
    else: return False

def revise_aux(num, condicion):
    if num == 0:
        return 0
    elif condicion(num % 10):
        return 1 + revise_aux(num // 10, condicion)
    else: return revise_aux(num // 10, condicion)

#
# Programe una funcion que indique si una lista tiene al menos un cero.
# La funcion debe regresar True o False
#

def TieneCeroL(lista):
    if isinstance(lista, list) and len(lista) >= 1:
        Es0 = lambda digito: digito == 0
        return TieneCeroL_aux(lista, Es0)
    else: return "Error"

def TieneCeroL_aux(lista, condicion):
    if lista == []:
        return False
    elif condicion(lista[0]):
        return True
    else: return TieneCeroL_aux(lista[1:], condicion)

# Hacer una funcion que indique si todos los elementos de una lista
# son positivos. La funcion debe regresar True o False
#

def PositivoL(lista):
    if isinstance(lista, list) and lista != []:
        Posi = lambda digito : digito >= 0
        return PositivoL_aux(lista, Posi)
    else:
        return "Error"

def PositivoL_aux(lista, condicion):
    if lista == []:
        return True
    elif condicion(lista[0]):
        return PositivoL_aux(lista[1:], condicion)
    else: return False

# --- Taller ---
# Dado un numero determine cuantos de sus digitos son pares y cuandos son
# impares. Utilice funciones lambda
#

def ParesImparesL(num):
    if isinstance(num, int) and (num > 0):
        Par = lambda digito: (digito % 10) % 2 == 0
        Impar = lambda digito: (digito % 10) % 2 == 1
        print("La cantidad de números pares es:" , Pares_aux(num, Par))
        print("La cantidad de números impares es:" , Impares_aux(num, Impar))
        return
    else: return "Error"

def Pares_aux(num, condicion):
    if num == 0:
        return 0
    elif condicion(num):
        return 1 + Pares_aux(num // 10 , condicion)
    else: return Pares_aux(num // 10 , condicion)

def Impares_aux(num, condicion):
    if num == 0:
        return 0
    elif condicion(num):
        return 1 + Impares_aux(num // 10 , condicion)
    else: return Impares_aux(num // 10 , condicion)

# Programe una funcion que indique cuantas veces se repite un digito en una
# lista. Utilice funcion lamba. La funcion debe regresar True o False
#

def VecesEnListaL(num, lista):
    if isinstance(lista, list):
        Esta = lambda x , y: x == y
        return VecesEnListaL_aux(num, lista, Esta)
    else: return "Error"

def VecesEnListaL_aux(num, lista, condicion):
    if lista == []:
        return 0
    elif condicion(num,lista[0]):
        return 1 + VecesEnListaL_aux(num, lista[1:], condicion)
    else: return VecesEnListaL_aux(num, lista[1:], condicion)

# 
# 
# 
        










