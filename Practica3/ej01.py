import random;
colores = list(open("fcolores","r"))
coordenadas = list(open("fcoord","r"))
dicc = {}

for i in range(0,len(coordenadas),2):
    dicc[(int(coordenadas[i]),int(coordenadas[i+1]))] = random.choice(colores).strip()
for clave,valor in dicc.items():
    print( ('\n {0:>30} '+('{},{} : {}'.format(clave[0],clave[1],valor))).format('') )
