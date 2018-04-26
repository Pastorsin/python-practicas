import json
from pattern.es import tag
from pattern.es import conjugate
from pattern.es import INFINITIVE

archivo = open("texto", "r")
verbos = open("verbos.json", "w")
dicc = {}
listaVerbos = []
# Almaceno todos los verbos
for palabra, tipo in tag(archivo.read()):
    if (tipo == 'VB'):
        listaVerbos.append(conjugate(palabra, INFINITIVE))
# Creo el dicc para el json verbo:apariciones
for verbo in set(listaVerbos):
    dicc[verbo] = listaVerbos.count(verbo)
# Preparo la lista para el JSON
listaVerbos = []
for verbo, cantidad in dicc.items():
    listaVerbos.append({verbo: cantidad})
# Escribo el JSON
json.dump(listaVerbos, verbos)
archivo.close()
