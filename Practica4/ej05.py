def sumar(*args):
    try:
        return sum(args)
    except TypeError:
        print('No es numerico')
        return 0


def imprimir(**kwargs):
    try:
        print('Nombre:', kwargs['nombre'])
    except KeyError:
        print('Falta el campo nombre')

    try:
        print('Apellido:', kwargs['apellido'])
    except KeyError:
        print('Falta el campo apellido')

    try:
        print('Sexo', kwargs['sexo'])
    except KeyError:
        print('Falta el campo apellido')


print(sumar(3, 4, 5, 6, 7, 8, 9, 'a', 10))
print(sumar(3, 4, 5, 6, 7))
imprimir(nombre='andres', apellido='milla', sexo='M')
