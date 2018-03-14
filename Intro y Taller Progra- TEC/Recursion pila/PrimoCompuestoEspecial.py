def PrimoCompuesto(num):
    if isinstance(num, int) and (num >= 0):
        if num == 0:
            return print(num, "es un número especial")
        elif num == 1:
            return print(num, "es un número especial")
        else:
            return PrimoCompuesto_aux(num, num - 1)
    else:
        return "Error"


def PrimoCompuesto_aux(num, div):
    if div == 1:
        return print(num, "es primo")
    elif num % div == 0:
        return print(num, "es compuesto")
    else: PrimoCompuesto_aux(num, div - 1)
