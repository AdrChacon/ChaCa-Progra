class Sequence:
    def serie(self):
        Inicio = int(input("Ingrese numero: ")) + 1
        Final = int(input("Ingrese numero: "))
        result = 0
        while Inicio < Final:
            result = result + Inicio
            Inicio = Inicio + 1
        print("La suma es ", result)
