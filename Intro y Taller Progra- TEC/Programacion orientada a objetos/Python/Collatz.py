class Collatz:
    def conjecture(self):
        sequence = ""
        Inicio = int(input("Ingrese el valor de n: "))
        sequence = sequence + str(Inicio)
        print("n:", Inicio)
        while Inicio != 1:
            if Inicio % 2 == 0:
                Inicio = Inicio // 2
                sequence = sequence + " " + str(Inicio)
            else:
                Inicio = Inicio * 3 + 1
                sequence = sequence + " " + str(Inicio)
        print(sequence)
    def Imprimir(self):
        Inicio = int(input("Ingrese el valor de n: "))
        sequence = ""
        print("n:", Inicio)
        for g in range(Inicio):
            sequence = sequence + "*"
        print(str(Inicio), sequence)
        sequence = ""
        while Inicio != 1:
            if Inicio % 2 == 0:
                Inicio = Inicio // 2
                for g in range(Inicio):
                    sequence = sequence + "*"
                print(str(Inicio), sequence)
                sequence = ""
            else:
                Inicio = Inicio * 3 + 1
                for g in range(Inicio):
                    sequence = sequence + "*"
                print(str(Inicio), sequence)
                sequence = ""
