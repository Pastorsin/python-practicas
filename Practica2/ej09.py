from pattern.es import tag
from pattern.es import INFINITIVE
from pattern.es import conjugate
from collections import Counter
frase = "Este es un párrafo de prueba. El verbo ser, será el mas utilizado. El otro será crear, por eso se creó la oración de esta manera. Por último, se creará esta oración que posee el tercer verbo: poseer. Nada más que decir."
lista_verbos = list(filter(lambda x:  x[1]== 'VB' , tag(frase))) # Filtro de la lista solo los que son verbos
lista_verbos = list(map(lambda x: conjugate(x[0],INFINITIVE), lista_verbos)) # Convierto los verbos en infinitivo
print(Counter(lista_verbos).most_common(3))
