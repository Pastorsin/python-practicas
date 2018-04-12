#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pattern.es import singularize, pluralize
def convertir(cambiar): #Diccionario con {'s':[palabrassingulares],'p':[palabrasplurales]}
	""" Devuelve un diccionario con palabras singulares en plurales y viceversa """
	invertido = {'p':[],'s':[]}
	for singulares in cambiar['s']:
		invertido['p'].append(pluralize(singulares))
	for plurales in cambiar['p']:
		invertido['s'].append(singularize(plurales))
	return invertido

cambiar = {'s':['gato','caballo', 'silla'],'p': ['informaticas','psicologas', 'ingenieras']}
print(convertir(cambiar))