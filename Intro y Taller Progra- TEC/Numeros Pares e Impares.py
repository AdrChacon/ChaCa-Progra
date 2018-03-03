#
# Crear función para determinar cuantos digitos pares e impares tiene un número
#


def Numeros_Pares_Impares(num):
   if isinstance(num, int) and (num > 0):
      print("La cantidad de números pares es:" , Numeros_Pares_Aux(num))
      print("La cantidad de números impares es:" , Numeros_Impares_Aux(num))
   else:
      return "Error"

def Numeros_Pares_Aux(num):
   if num == 0: # Condicion de parada *Tiene que ir antes de lo demas*
      return 0
   else:
      if ((num % 10) % 2) == 0:
         return 1 + Numeros_Pares_Aux(num // 10)
      elif ((num % 10) % 2) == 1:
         return Numeros_Pares_Aux(num // 10)

def Numeros_Impares_Aux(num):
   if num == 0:
      return 0
   else:
      if ((num % 10) % 2) == 1:
         return 1 + Numeros_Impares_Aux(num // 10)
      elif ((num % 10) % 2) == 0:
         return Numeros_Impares_Aux(num // 10)

#
# Verificar que todos los digitos del número se encuentren entre 0 y 4.
#

def CuatroMaximo(num):
   if isinstance(num, int) and (num > 0):
      return CuatroMaximoAux(abs(num))
   else:
      return "Error"

def CuatroMaximoAux(num):
   if num == 0:
      return True
   if (num % 10) >= 0 and (num % 10) <= 4:
      return CuatroMaximoAux(num // 10)
   else:
      return False

#
#  Calcular el factorial de un numero
#

def FactorialNumero(num):
   if num == 0:
      return 1
   else:
      return num * FactorialNumero(num - 1)


