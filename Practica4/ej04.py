try:
    archivo = open('archivo.txt')
    for num in archivo:
        try:
            int(num)
        except ValueError:
            print('No es numero:', num)
            continue
except FileNotFoundError:
    print('No existe el archivo')
