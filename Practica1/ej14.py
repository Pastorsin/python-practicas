# Ejercicio 13
print("Ejercicio 13")
imagenes = ['im1','im2','im3']
dicc = {} # Va a ser un diccionario del siguiente formato {Imagen:{coord1,coord2,coord3}} donde coord es una tupla que está dentro de un conjunto
for img in imagenes:
	dicc[img] = set()
	while len(dicc[img]) != 3:
		print("Imagen: ",img)
		dicc[img].add( (float(input("Ingrese una coordenada X:")) , float(input("Ingrese una coordenada Y:")) ) )
print(dicc)	

# Ejercicio 14
print("Ejercicio 14")
tam={'im1':[(1.0,2.0),(3.0,4.0)],'im2':[(5.0,6.0),(7.0,8.0)],'im3':[(9.0,10.0),(11.0,12.0)]}
for img in dicc:
	for coord in dicc[img]:
		if (coord[0] >= tam[img][0][0]) and (coord[1] >= tam[img][0][1]) and (coord[0] <= tam[img][1][0]) and (coord[1] <= tam[img][1][1]):
			print("* La coordenada",coord,"de la IMAGEN",img,"esta dentro de los limites: INF",tam[img][0],"SUP",tam[img][1])
		else:
			print("* La coordenada",coord,"de la IMAGEN",img,"queda fuera de los limites: INF",tam[img][0],"SUP",tam[img][1])
