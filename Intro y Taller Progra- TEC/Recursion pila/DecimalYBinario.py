"""
Decimal a Binario
"""

def DecimalBinario(num):
    if isinstance(num, int) and num > 0:
        return DecimalBinario_aux(abs(num), 0)
    else: return "Error"

def DecimalBinario_aux(num, pos):
    if num == 1:
        return 1*(10**pos)
    else: return (num%2)*(10**pos) + DecimalBinario_aux(num//2,pos+1)

"""
-------------------------------------------------------------------------

Binario a Decimal
"""

def BinarioDecimal(num):
    if isinstance(num,int) and EsBinario(num):
        return BinarioDecimal_aux(abs(num), 0)
    else: return "Error"

def EsBinario(num):
    if num == 1 and num//10 == 0:
        return True
    elif num%10 == 0 or num%10 == 1:
        return EsBinario(num//10)
    else: return False

def BinarioDecimal_aux(num, pos):
    if num == 0:
        return 0
    elif num%10 == 1:
        return (num%10)*2**pos + BinarioDecimal_aux(num//10,pos+1)
    elif num%10 == 0:
        return BinarioDecimal_aux(num//10,pos+1)




