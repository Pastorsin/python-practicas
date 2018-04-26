import json
archivo = open("jugadores2.txt","w")
listaDicc = []
dicc = {}
for x in range(3):
    usuario = input("Ingrese un nombre de usuario")
    dicc[usuario] = {"Puntaje": str(float(input("Puntaje"))),
                     "Nivel": str(int(input("Nivel Alcanzado"))),
                     "Tiempo": str(float(input("Tiempo")))
                     }
    listaDicc.append({usuario:dicc[usuario]})
json.dump(listaDicc,archivo)
archivo.close()

##
archivo = open("jugadores2.txt","r")
print(json.dumps(json.load(archivo), sort_keys=True, indent=4))
archivo.close()
