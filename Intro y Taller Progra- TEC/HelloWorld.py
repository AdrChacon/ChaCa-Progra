class HelloWorld:
    def Simple(self):
        print("Hello World")

    def IteracionFor(self):
        hello = "Hello World"
        for x in hello:
            print(x)

    def IteracionWhileFor(self):
        hello = "Hello World"
        Cero = True
        while Cero:
            cant = int(input("Cantidad de lineas: "))
            if cant == 0:
                Cero = False
            else:
                for x in range(cant):
                    print(hello + " " + str(x + 1))
            
