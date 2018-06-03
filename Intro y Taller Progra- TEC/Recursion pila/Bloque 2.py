""" Ejercicios Bloque 2"""

"""1"""

def calcularFracciones():
    return calcularFracciones_aux(1)

def calcularFracciones_aux(cont):
    print(cont, 1/(2**cont))
    if 1/(2**cont) <= 0.000001:
        return
    else:
        return calcularFracciones_aux(cont+1)

"""2"""

def multiplos(num):
    if isinstance(num,int) and num > 0:
        return multiplos_aux(abs(num) , 1)
    else: return "Error"

def multiplos_aux(num, cont):
    if cont == num:
        return
    elif cont%3 == 0 or cont%7 == 0:
        return multiplos_aux(num, cont+1)
    else: print(cont)
    return multiplos_aux(num, cont+1)

"""3"""

def divisores(num):
    if isinstance(num, int) and num > 0:
        return divisores_aux(abs(num), 2)
    else: return "Error"

def divisores_aux(num, cont):
    if cont == num:
        return []
    elif num%cont == 0:
        return [cont] + divisores_aux(num, cont+1)
    else:
        return divisores_aux(num, cont+1)
"""4"""

def sumar(lista):
    if isinstance(lista, list):
        return sumar_aux(lista)
    else: return "Error"

def sumar_aux(lista):
    if lista == []:
        return 0
    elif isinstance(lista[0], list):
        return sumar_aux(lista[0] + lista[1:])
    else: return lista[0] + sumar_aux(lista[1:])

"""5"""

def multid(digi, num):
    if isinstance(digi, int) and isinstance(num, int) and digi > 0 and num > 0:
        return multid_aux(digi, num, 0)
    else: return "Error"

def multid_aux(digi, num, pot):
    if num == 0:
        return 0
    elif (num%10)*digi > 9:
        return multid_aux(digi, num//10, pot)
    else: return ((num%10)*digi)*10**pot + multid_aux(digi, num//10, pot+1)


"""6"""

def dados():
    return dados_aux([1,2,3,4,5,6], 0)

def dados_aux(lista, cont):
    if cont == 6:
        return
    else:
        print(lista[0], lista[0])
        print(lista[0], lista[1])
        print(lista[0], lista[2])
        print(lista[0], lista[3])
        print(lista[0], lista[4])
        print(lista[0], lista[5])
        return dados_aux(lista[1:] + [lista[0]], cont+1)

"""7"""

def mayores(num, lista):
    if isinstance(lista, list):
        return mayores_aux(num, lista)
    else: return "Error"

def mayores_aux(num, lista):
    if lista == []:
        return 0
    elif lista[0] > 5:
        return 1 + mayores_aux(num, lista[1:])
    else: return mayores(num, lista[1:])

"""8"""

def multiplos2(num):
    if isinstance(num, int) and num > 0:
        return multiplos2_aux(abs(num), 1)
    else: return "Error"

def multiplos2_aux(num, mult):
    print(num, "x", mult, "=", num*mult)
    if mult == 10:
        return
    else: return multiplos2_aux(num, mult+1)

"""9"""

def Pot2Hasta(num):
    if isinstance(num, int) and num > 0:
        return Pot2Hasta_aux(abs(num), 0)
    else: return "Error"

def Pot2Hasta_aux(num, cont):
    print(2**cont)
    if cont == num:
        return
    else: return Pot2Hasta_aux(num, cont+1)

"""10"""

def multiplicaciones(lista):
    if isinstance(lista, list):
        return multiplicaciones_aux(lista,0)
    else: return "Error"

def multiplicaciones_aux(lista, pos):
    if lista == []:
        return []
    else: return [lista[0] * pos] + multiplicaciones_aux(lista[1:],pos+1)

"""11"""

def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista, 1)
    else: return "Error"

def suma_aux(lista, pos):
    if lista == []:
        return 0
    elif isinstance(lista[0], list):
        return suma_aux(lista[0] + lista[1:], pos)
    else: return lista[0]**pos + suma_aux(lista[1:], pos+1)

"""12"""

def summ(num):
    if isinstance(num, int) and num > 0:
        return summ_aux(abs(num))
    else: return "Error"

def summ_aux(num):
    if num == 0:
        return 0
    else: return prod_aux(num) + summ_aux(num-1)

def prod_aux(j):
    if j == 0:
        return 1
    else:
        return (3*(j**(2))-j)* prod_aux(j-1)
        
"""13"""

def intercambiar(num):
    if isinstance(num, int) and Tiene0(num):
        return intercambiar_aux(abs(num), 0)
    else: return "Error"

def Tiene0(num):
    if num//10 == 0:
        return True
    elif num%10 == 0:
        return False
    else: return Tiene0(num//10)

def intercambiar_aux(num,pos):
    if num == 0:
        return 0
    else: return (num%10)*10**(pos+1) + ((num//10)%10)*10**(pos) + intercambiar_aux(num//100, pos+2)

"""14"""

def invertir(num):
    if isinstance(num , int) and num >= 100 and num <= 999:
        return invertir_aux(abs(num), 2)
    else: return "Error"

def invertir_aux(num, pos):
    if num == 0:
        return 0
    else: return (num%10)*10**pos + invertir_aux(num//10, pos-1)

"""15"""

def RegresarDecimal(num):
    if isinstance(num, float):
        return RegresarDecimal_aux(num)
    else: return "Error"

def RegresarDecimal_aux(num):
    return abs(num - int(num))

"""16"""

def Bisiesto():
    valor = input("Ingrese un numero:")
    year = int(valor)
    if year > 1582:
        if BisiestoGregoriano(year):
            return print(year, "es bisiesto")
        else: return print(year, "no es bisiesto")
    elif BisiestoJuliano(year):
        return print(year, "es bisiesto")
    else: return print(year, "no es bisiesto")

def BisiestoGregoriano(year):
    if year % 400 == 0:
        return True
    elif BisiestoGregoriano_aux(year):
        return True
    else: return False

def BisiestoGregoriano_aux(year):
    if year % 10 == 0:
        return BisiestoGregoriano_aux(year//10)
    elif year % 4 == 0:
        return True
    else: return False

def BisiestoJuliano(year):
    if year % 4 == 0:
        return True
    else: return False
