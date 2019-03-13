import math


class Punto():

    def __init__(self, x, y):
        self.__coordX = x
        self.__coordY = y

    def getX(self):
        return self.__coordX

    def getY(self):
        return self.__coordY

    def calcularDistancia(self, x, y):
        return math.hypot(math.fabs(self.getX() - x),
                          math.fabs(self.getY() - y))

    def esIgual(self, x, y):
        return (x == self.getX() and y == self.getY())

    def sumarX(self, x):
        return (self.getX() + x, self.getY())

    def sumarY(self, y):
        return (self.getX(), self.getY() + y)


punto = Punto(2, 3)
print(punto.calcularDistancia(2, 3))
print(punto.esIgual(2, 3))
print(punto.sumarX(1))
print(punto.sumarY(1))
