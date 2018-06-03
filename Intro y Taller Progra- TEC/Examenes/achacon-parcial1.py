"""Pregunta 1:"""

def formarLista(num):
    if isinstance(num, int) and num > 0:
        return formarLista_aux(abs(num))
    else: return "Error"

def formarLista_aux(num):
    if num == 0:
        return []
    elif (num%10)%2 == 0:
        return [num%10] + formarLista_aux(num//10)
    else: return formarLista_aux(num//10)

"""Pregunta 2:"""

def polindromo(num):
    if isinstance(num, int) and num > 0:
        return polindromo_aux(num, num, 0)
    else: return "Error"

def polindromo_aux(num, div, cont):
    if num == alrevez(num, div, cont):
        return True
    else: return False

def alrevez(num, div, cont):
    if div == 0:
        return alrevez_aux(num, cont-1)
    else: return alrevez(num, div//10, cont+1)

def alrevez_aux(div,cont):
    if div == 0:
        return 0
    else: return (div%10)*10**cont + alrevez_aux(div // 10, cont-1)

"""Pregunta 3:"""

def contarConsonantes(palabra):
    if isinstance(palabra, str): # En el cuaderno de examen es "isinstance(palabra, String)"
        return contarConsonantes_aux(palabra)
    else: return "Error"

def contarConsonantes(palabra):
    if palabra == '':
# En el cuaderno de examen es "palabra == []", no se si es error de sintaxis o
# de logica.
        return 0
    elif palabra[0] == 'a':
        return contarConsonantes(palabra[1:])
    elif palabra[0] == 'e':
        return contarConsonantes(palabra[1:])
    elif palabra[0] == 'i':
        return contarConsonantes(palabra[1:])
    elif palabra[0] == 'o':
        return contarConsonantes(palabra[1:])
    elif palabra[0] == 'u':
        return contarConsonantes(palabra[1:])
    else: return 1 + contarConsonantes(palabra[1:])

"""Pregunta 4:"""

def intercambiar(lista):
    if isinstance(lista, list):
        return intercambiar_aux(lista)
    else: return "Error"

def intercambiar_aux(lista):
    if lista == []:
        return []
    else: return [lista[1]] + [lista[0]] + intercambiar_aux(lista[2:])




    
