anim = {"Gato Montes":2,"Yacare overo":4,"Boa acuática":5,"Andres":0}
for nombre_animal in anim: # Recorro diccionario
	resultado = ("_"*len(nombre_animal)) # Hago un string con tantos "_" como tenga la palabra
	lim = anim[nombre_animal]	
	print(" ".join(resultado[0:lim]+nombre_animal[anim[nombre_animal]]+resultado[lim+1:len(resultado)])) # Corto el string en los limites donde corresponda la letra y lo concateno con esta misma