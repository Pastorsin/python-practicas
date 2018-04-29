#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import csv


def exportar_csv_a_json(nombre):
    archivo_json = open(nombre + ".json", "w")
    archivo_csv = open(nombre + ".csv", "r")
    lista_csv = list(csv.reader(archivo_csv))
    encabezado_csv = lista_csv[0]
    lista_json = []

    for valor_csv in lista_csv[1:]:
        dicc_json = {}
        for i in range(len(encabezado_csv)):
            #print("{0:50} : {1:90}".format(encabezado_csv[i],valor_csv[i]))
            dicc_json[encabezado_csv[i].strip()] = valor_csv[i].strip()
        lista_json.append(dicc_json)

    json.dump(lista_json, archivo_json, ensure_ascii=False)

    archivo_json.close()
    archivo_csv.close()


def imprimir_json(nombre):
    archivo = open(nombre+".json", "r")
    datos = json.load(archivo)
    print((json.dumps(datos, sort_keys=True, indent=4, ensure_ascii=False)))
    archivo.close()

exportar_csv_a_json("fTodas.las.carreras27032018")
imprimir_json("fTodas.las.carreras27032018")
