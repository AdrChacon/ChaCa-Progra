class Multiples:
    def table(self):
        Numero = int(input("Ingrese un numero: "))
        for n in range(1, 11):
            print(str(Numero) + " x " + str(n) + " = ", Numero*n)
