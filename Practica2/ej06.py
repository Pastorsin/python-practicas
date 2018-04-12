import os
lista_de_archivos = (os.listdir((os.getcwd())))
for archivo in lista_de_archivos:
	print("Nombre: {} | Tamaño: {}bytes | Fecha de ultimo acceso: {}".format(archivo , os.path.getsize(archivo) , os.path.getatime(archivo)))