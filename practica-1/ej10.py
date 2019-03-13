dicc = {}
for x in range(3):
	usuario = input("Ingrese un nombre de usuario")
	dicc[usuario] = {"Puntaje": float(input("Puntaje")),"Nivel":int(input("Nivel Alcanzado")),"Tiempo":float(input("Tiempo")) }

max = -1;
for user in dicc:
	if dicc[user]["Puntaje"] > max:
		max = dicc[user]["Puntaje"]
		usuario = user

print("El usuario con el puntaje maximo es :", usuario)
