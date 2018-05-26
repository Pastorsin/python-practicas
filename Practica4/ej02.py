def abrir_archivo(nombre):
    try:
        archivo = open(nombre)
    except FileNotFoundError:
        print('No se encuentra el archivo con dicho nombre')


abrir_archivo('ej01.py')
abrir_archivo('pepehands')
