# Dado un numero, determine su longitud (numero de digitos)
# Entrada: es un numero entero
# Restricciones:  es un entero positivo mayor a cero
# Salida: suma de los digitos


def longitud_numero(num):
    if isinstance(num, int) and (num > 0):
        return longitud_numero_aux(abs(num))
    else:
        return "Error"

def longitud_numero_aux(num):
    if (num == 0):
        return 0
    else:
        return 1 + longitud_numero_aux(num // 10)

