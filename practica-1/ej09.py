dicc = {}

for x in range(3):
	usuario = input("Ingrese un nombre de usuario")
	dicc[usuario] = {"Puntaje": float(input("Puntaje")),"Nivel":int(input("Nivel Alcanzado")),"Tiempo":float(input("Tiempo")) }

print(dicc.keys())