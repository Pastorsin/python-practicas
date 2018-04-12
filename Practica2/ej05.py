from pattern.es import tag
from pattern.es import INFINITIVE, PRESENT, PAST, SG, SUBJUNCTIVE, PERFECTIVE
from pattern.es import conjugate

def verbos_infinitivos(oracion):
	lista_infinitivos = []
	oracion = tag(oracion) # Devuelve una tupla con el siguiente formato: (palabra,tipo) -- tipo: adjetivo,verbo,etc. 
	for palabra, tipo in oracion:
		if (tipo == 'VB'):  # Veo cuales son los verbos
			lista_infinitivos.append(conjugate(palabra,INFINITIVE))
	return lista_infinitivos
			

oracion = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias."
print(verbos_infinitivos(oracion))
