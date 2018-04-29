import csv


def informar_mujeres(dicc):
    datos = "{0:^90} | {1:^10}".format("UNIVERSIDAD", "MUJERES")
    print("-" * len(datos))
    print(datos)
    print("-" * len(datos))
    for universidad, total in sorted(list(dicc.items()), key=lambda x: x[1], reverse=True):
        datos = "{0:90} | {1:10d}".format(universidad, total)
        print(datos)
        print("-" * len(datos))

archivo = open("fTodas.las.carreras27032018.csv", "r")
dicc = {}
for x in list(csv.reader(archivo))[1:]:
    if x[2] in dicc:
        dicc[x[2]] += (0 if x[10] == '' else int((''.join(list(filter(lambda x: x.isdigit(), x[10]))))))
    else:
        dicc[x[2]] = (0 if x[10] == '' else int((''.join(list(filter(lambda x: x.isdigit(), x[10]))))))
informar_mujeres(dicc)
