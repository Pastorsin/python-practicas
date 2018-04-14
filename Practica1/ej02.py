frase = input("Ingrese una frase: ")
string = input("Ingrese un string: ")
cadena = (frase+' '+string).split(' ')			# Le sumo el espacio para tener en cuenta la palabra en la unión
print("Cantidad de palabras: ",len(cadena))
