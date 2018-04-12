#!/usr/bin/env python
# -*- coding: utf-8 -*-
def imprimir_ranking(dicc):
	lista_puntajes = []
	for user in dicc.values():
		lista_puntajes.extend([user['Puntaje']])
	for puntaje in lista_puntajes[:2]: #En vez de 2 serian 10
		print(puntaje)

def imprimir_por_apellido(dicc):
	lista_user = sorted(list(dicc.keys()))
	for user in lista_user:
		print(dicc[user])

def imprimir_por_nivel(dicc): #Pendiente
	lista_nivel = []
	for user in dicc.values():
		lista_nivel.extend([user['Nivel']])
	sorted(lista_nivel)
	for nivel in lista_puntajes:
		print()
	

dicc = {}
for x in range(3):
	usuario = input("Ingrese un nombre de usuario")
	dicc[usuario] = {"Puntaje": float(input("Puntaje")),"Nivel":int(input("Nivel Alcanzado")),"Tiempo":float(input("Tiempo")) }
imprimir_ranking(dicc)
imprimir_por_apellido(dicc)
imprimir_por_nivel(dicc)
