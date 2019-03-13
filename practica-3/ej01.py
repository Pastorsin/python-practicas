import random
import os
colores = list(open(os.path.join("archivos","colores"),"r"))
coordenadas = list(open(os.path.join("archivos","coord"),"r"))
dicc = {}

for i in range(0,len(coordenadas),2):
    dicc[(int(coordenadas[i]),int(coordenadas[i+1]))] = random.choice(colores).strip()
for clave,valor in dicc.items():
    print( ('\n {0:>30} '+('{},{} : {}'.format(clave[0],clave[1],valor))).format('') )
