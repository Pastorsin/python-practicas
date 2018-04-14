imagenes = ['img1','img2','img3']
dicc = {} # Va a ser un diccionario del siguiente formato {Imagen:{coord1,coord2,coord3}} donde coord es una tupla que está dentro de un conjunto
for img in imagenes:
	dicc[img] = set()
	while len(dicc[img]) != 3:
		print("Imagen: ",img)
		dicc[img].add( (float(input("Ingrese una coordenada X:")) , float(input("Ingrese una coordenada Y:")) ) )
print(dicc)		
