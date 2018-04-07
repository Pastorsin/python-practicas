# -*- encoding: utf-8 -*-
puntaje = {}
puntaje[30] = 'Ada'
puntaje[40] = 'Hedy Lammar'
puntaje[45] = 'Colossus'
puntaje[47] = 'Angela Ruiz Robles'
for punt in puntaje:
	print(punt)
for cada in sorted(puntaje,reverse=True):
	print(puntaje[cada],cada)