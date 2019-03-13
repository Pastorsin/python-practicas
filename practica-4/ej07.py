import sys


class Puntaje():

    def __init__(self, nivel, puntos, tiempo):
        self.__nivel = nivel
        self.__puntos = puntos
        self.__tiempo = tiempo

    def getNivel(self):
        return self.__nivel

    def getPuntos(self):
        return self.__puntos

    def getTiempo(self):
        return self.__tiempo


class Jugador():

    def __init__(self, nombre, lista_puntajes):
        self.__nombre = nombre
        self.__lista_puntajes = lista_puntajes

    def getNombre(self):
        return self.__nombre

    def getListaPuntajes(self):
        return self.__lista_puntajes

    def nivelMaximo(self):
        return max(self.getListaPuntajes(), key= lambda x: x.getNivel()).getNivel()

    def cantidadTotalPuntajes(self):
        return sum(x.getPuntos() for x in self.getListaPuntajes())

    def puntajeMaximo(self, nivel):
        lista_niveles = list(filter(lambda x: x.getNivel() == nivel,self.getListaPuntajes()))
        return max(lista_niveles, key= lambda x: x.getPuntos()).getPuntos()

    def menorTiempo(self, nivel):
        lista_niveles = list(filter(lambda x: x.getNivel() == nivel,self.getListaPuntajes()))
        return min(lista_niveles, key= lambda x: x.getTiempo()).getTiempo()


if __name__ == "__main__":
    puntaje1 = Puntaje(1, 20, 30)
    puntaje2 = Puntaje(5, 50, 60)
    puntaje3 = Puntaje(2, 90, 20)
    puntaje4 = Puntaje(2, 9000, 20)
    jugador = Jugador("Andres", [puntaje1, puntaje2, puntaje3, puntaje4])
    print(jugador.nivelMaximo())
    print(jugador.cantidadTotalPuntajes())
    print(jugador.puntajeMaximo(2))
    print(jugador.menorTiempo(1))
