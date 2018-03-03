# Entrada: es un número entero
# Restricciones: es un entero positivo mayor a cero
# Salida: suma de los dígitos
def suma_digitos(num):
    if isinstance(num, int) and (num > 0):
        return suma_digitos_aux(abs(num))
    else:
        return "Error"

def suma_digitos_aux(num):
    if (num == 0):
        return 0
    else:
        return num% 10 + suma_digitos_aux(num // 10)
