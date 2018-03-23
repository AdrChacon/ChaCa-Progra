# 23/03/2018
# Intro Progra
# 1. Desarrolle un programa que recibe como parámetro una lista y la regresa
# en orden invertido.
class Invertir:
    def _init(self):
        pass
    def Invertido(self, lista):
        if isinstance(lista, list):
            return self.Invertido_aux(lista)
        else:
            return "Error"

    def Invertido_aux(self, lista):
        if lista == []:
            return []
        else:
            return self.Invertido_aux(lista[1:]) + [lista[0]]

# inv = Invertir()          } Para
# inv.Invertido([1,2,3,4])  } ejecutar



#
#
