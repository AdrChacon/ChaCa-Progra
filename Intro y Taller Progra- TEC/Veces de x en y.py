'''
Dado un numero, encontrar cuantas veces aparece un digito en ese número
'''
def Aparece(num, digito):
    if num == 0:
        return 0
    else:
        if num % 10 == digito:
            return 1 + Aparece(num//10, digito)
        else:
            return Aparece(num//10, digito)
