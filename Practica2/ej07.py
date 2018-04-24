import os
from datetime import datetime
lista_a = list(map(lambda x: x.capitalize(),(os.listdir(('.')))))
print('Consigna A:',lista_a)
lista_b = (list(filter(lambda x: (datetime.today() - datetime.utcfromtimestamp(os.path.getmtime(x) )).days < 3,os.listdir('.'))))
print('Consigna B:',lista_b)
print('Consigna D:', sorted(os.listdir('.') , key= lambda x: os.path.getsize(x)))
