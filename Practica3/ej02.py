import random


def cargarCoordenadas():
    coordenadas = open("fcoordP2", "w")
    string = ""
    for x in range(3):
        x = str(int(input("Coordenada X")))
        y = str(int(input("Coordenada Y")))
        string = string + x + '\n' + y + '\n'
    coordenadas.write(string.strip())

colores=list(open("fcolores", "r"))
cargarCoordenadas()
coordenadas=list(open("fcoordP2","r"))
estructura=open("festructura","w")

for i in range(0,len(coordenadas),2):
    estructura.write(((coordenadas[i].strip())+','+(coordenadas[i+1].strip()))+':'+random.choice(colores).strip()+'\n')
    # Armo la estructura del siguiente formato para luego poder leerlo con el mismo patrón:
    # x,y separadas por una coma (,)
    # Coordenada y colores separadas por dos puntos (:)
    # separo un elemento de otro con un salto de línea
