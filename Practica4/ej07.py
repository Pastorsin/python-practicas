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
        nivel_maximo = -1
        for puntaje in self.getListaPuntajes():
            nivel_maximo = max(nivel_maximo, puntaje.getNivel())
        return nivel_maximo

    def cantidadTotalPuntajes(self):
        suma = 0
        for puntaje in self.getListaPuntajes():
            suma += puntaje.getPuntos()
        return suma

    def puntajeMaximo(self, nivel):
        puntaje_maximo = -1
        for puntaje in self.getListaPuntajes():
            if puntaje.getNivel() == nivel:
                puntaje_maximo = max(puntaje_maximo, puntaje.getPuntos())
        return puntaje_maximo

    def menorTiempo(self, nivel):
        tiempo_minimo = sys.maxsize
        for puntaje in self.getListaPuntajes():
            if puntaje.getNivel() == nivel:
                tiempo_minimo = min(tiempo_minimo, puntaje.getTiempo())
        return tiempo_minimo


if __name__ == "__main__":
    puntaje1 = Puntaje(1, 20, 30)
    puntaje2 = Puntaje(5, 50, 60)
    puntaje3 = Puntaje(2, 90, 20)
    jugador = Jugador("Andres", [puntaje1, puntaje2, puntaje3])
    print(jugador.nivelMaximo())
    print(jugador.cantidadTotalPuntajes())
    print(jugador.puntajeMaximo(2))
    print(jugador.menorTiempo(1))


# env
# git
# gitignore env
# pip install -r requirements
