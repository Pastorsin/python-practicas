dicc = {}

for x in range(3):
	usuario = input("Ingrese un nombre de usuario")
	dicc[usuario] = {"Puntaje": float(input("Puntaje")),"Nivel":int(input("Nivel Alcanzado")),"Tiempo":float(input("Tiempo")) }
for x in range(3):
	ingreso = input("Ingrese el nombre de un Usuario a buscar")
	if ingreso in dicc:
		print(dicc[ingreso])
	else:
		print("No se encuentra el nombre de Usuario")