from pattern.es import tag


def verbos(oracion):
    # Devuelve una tupla con el siguiente formato: (palabra,tipo) -- tipo:
    # adjetivo,verbo,etc.
    oracion = tag(oracion)
    for palabra, tipo in oracion:
        if (tipo == 'VB'):  # Veo cuales son los verbos
            print(palabra)

oracion = "Los polinomios son objetos muy utilizados en matemáticas y en ciencia. En la práctica, son utilizados en cálculo y análisis matemático para aproximar cualquier función derivable; las ecuaciones polinómicas y las funciones polinómicas tienen aplicaciones en una gran variedad de problemas, desde la matemática elemental y el álgebra hasta áreas como la física, química, economía y las ciencias sociales."
verbos(oracion)
