def Operacion2(num):
  if isinstance(num, int) and (num > 0):
    return Operacion2_aux(abs(num))
  else:
    return "Error"
    
def Operacion2_aux(num):
  if num == 0:
    return 0
  else:
    return (num * num ** 3) + Operacion2_aux(num-1)
    
#
#
#

def Operacion3(num):
  if isinstance(num, int) and (num > 0):
    return Operacion3_aux(abs(num))
  else:
    return "Error"
    
def Operacion3_aux(num):
  if num == 0:
    return 0
  else:
    return (num + 5*(num*num)**2) + Operacion3_aux(num - 1)
    
#
#
#

def Operacion4(num):
  if isinstance(num, int) and (num > 0):
    return Operacion4_aux(abs(num))
  else:
    return "Error"

def Operacion4_aux(num):
  if num == 0:
    return 1
  else:
    return (3*num-2) * Operacion4_aux(num-1)
    
#
#
#

def Operacion5(n):
  if isinstance(n, int) and (n > 0):
    return Op5_Sumatoria(abs(n))
  else:
    return "Error"

def Op5_Sumatoria(n):
  if n == 0:
    return 0
  else:
    return Op5_Producto(n) + Op5_Sumatoria(n - 1)

def Op5_Producto(j):
  if j == 0:
    return 1
  else:
    return (3 * j ** 2 - j) * Op5_Producto(j-1)
