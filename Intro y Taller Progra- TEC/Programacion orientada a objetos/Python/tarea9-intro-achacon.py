class Suma:
    def Sumaringresados(self):
        result = 0
        ValIngresado = 0
        NoCero = True
        while NoCero:
            ValIngresado = int(input())
            result = result + ValIngresado
            if ValIngresado == 0:
                NoCero = False
        print(result)
        
