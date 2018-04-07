dicc = { "Andres":{"Puntaje":8,"Relleno":'a'}, "Ariel":{"Puntaje":2,"Relleno":'b'}, "Tomas":{"Puntaje":55,"Relleno":'c'}}

usuario = input("Nombre de usuario:")
puntaje = int(input("Puntaje:"))
relleno = input("Relleno:")
if usuario in dicc:
	if dicc[usuario]["Puntaje"] < puntaje:
		dicc[usuario]["Puntaje"] = puntaje
else:
	dicc[usuario] = {"Puntaje":puntaje,"Relleno":relleno}

print(dicc)

# * * * IMPRIMIR RANKING * * *
ranking = {}
cont = 0
for user in dicc:
	ranking[dicc[user]["Puntaje"]] = user # Creo un nuevo dicc del siguiente formato: {Puntaje:Usuario}
lista = sorted(ranking,reverse=True) # Creo una lista ordenada por puntajes de mayor a menor
print("• Ranking de los 2 mayores puntajes:")
for puntaje in lista:
	cont += 1
	print("PUESTO ",cont," | Usuario: ",ranking[puntaje], " | Puntaje: ",puntaje) # Imprimo el nombre del mayor puntaje
	if cont == 2:
		break