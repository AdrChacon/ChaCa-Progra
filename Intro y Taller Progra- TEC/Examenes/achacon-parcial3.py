class Examen:
    def contar(self):
        num = int(input("Ingrese numero: "))
        result = num
        contador = 0
        if num == 0:
            print("0 tiene 1 digito")
        else:
            while result != 0:
                result = result//10
                contador += 1
            print(str(num) + " tiene " + str(contador) + " digitos")

    def ordenar(self, lista):
        Largo = len(lista)
        listaresult = [] + lista # En cuaderno de examen olvide el +
        contador = 0
        for x in range(Largo):
            for y in range(Largo):
                if lista[x] > lista[y]:
                    contador = contador + 1
                else:
                    contador = contador
            listaresult[contador] = lista[x]
            contador = 0
        print("El resultado de ordenar la lista ", lista, " es ", listaresult)
