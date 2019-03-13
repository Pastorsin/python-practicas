import random;
colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dicc1 = {}
for coord in coordenadas:
	dicc1[coord] = random.choice(colores)
print (dicc1)
dicc2 = {}
for coord in coordenadas:
	color = random.choice(colores)
	dicc2[coord] = color;
	colores.remove(color)
print(dicc2)
	
