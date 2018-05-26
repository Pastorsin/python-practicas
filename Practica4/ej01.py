import random


def color(x, y):
    colores = ['azul', 'amarillo', 'rojo', 'blanco', 'negro']
    coordenadas = [(2, 3), (5, 6), (8, 8), (10, 2), (-5, -8)]
    random.shuffle(colores)
    dicc = dict(zip(coordenadas, colores))
    try:
        return dicc[(x, y)]
    except KeyError:
        print('Coordenada no válida')
        return False


print(color(2, 3))
print(color(2, 88))
