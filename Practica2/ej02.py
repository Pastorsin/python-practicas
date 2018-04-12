#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random;

def suma():
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)
	print(num1,'+',num2,'=',num1+num2, ". . . Es correcto?")
	input("Si o No")

def palabras():
	palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
	seccionAleatoria = random.choice(palabras)
	acentuacion = input("Que tipo de acentuacion posee la siguiente palabra: "+seccionAleatoria[1][0]+"?  ").lower()
	if (acentuacion == seccionAleatoria[0]):
		print("Correcto!")
	else:
		print("Incorrecto, la palabra tiene acentuacion: "+seccionAleatoria[0])



colores = ['azul','amarillo','rojo','blanco','negro']
listaFunciones = [suma,palabras]
funciones = {
    'azul':     random.choice(listaFunciones), 
	'amarillo': random.choice(listaFunciones),
	'rojo':		random.choice(listaFunciones),
	'blanco':	random.choice(listaFunciones),
	'negro':	random.choice(listaFunciones)
}
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dicc = {}
for coord in coordenadas:
	dicc[coord] = random.choice(colores)

ingreso = ( int(input("Ingrese una coordenada X")), int(input("Ingrese una coordenada Y")) )
if ingreso in coordenadas:
	funciones[dicc[ingreso]]()
