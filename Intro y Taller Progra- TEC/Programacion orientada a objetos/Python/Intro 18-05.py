import math

class Fig:
    def __init__(self,x,y):
        self.__X = x
        self.__y = y

    def getX(self):
        return self.__x
    def setX(self,x):
        if 0 <= x and x<= 1023:
            self.__x = x
        else: print("El valor de x debe ser mayor o igual a 0 y menor o igual a 1024")
    def getY(self):
        return self.__y
    def setY(self,y):
        if y >= 0 and y <= 768:
            self.__y = y
        else: print("El valor de y debe ser mayor o igual a 0 y menor o igual a 767")

class Circulo(Fig):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__r = r

    def getRadio(self):
        return self.__radio
    def setRadio(self, r):
        self.__radio = r
    def calcularArea(self):
        return math.pi * (self.__radio**2)

class Rectangulo(Fig):
    def __init__(self, x, y, alto, ancho):
        super().__init__(x,y)
        self.__alto = alto
        self.__ancho = ancho
    def getAlto(self):
        return self.__alto
    def setAlto(self, alto):
        self.__alto = alto
    def getAncho(self):
        return self.__ancho
    def setAncho(self,ancho):
        self.__ancho = ancho
    def calcularArea(self):
        return self.__alto * self.__ancho








    
