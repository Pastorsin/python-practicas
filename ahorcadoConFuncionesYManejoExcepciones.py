# Las imágenes del ahorcado fueron sacadas del ejemplo incluído en: http://inventwithpython.com/invent4thed/chapter9.html

import random
import json

ahorcado = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

# Eliminamos la definición del diccionario "palabras"


# La función defino_palabra NO recibe parámetros (palabras) porque se crea
# el diccionario adentro de la función

def defino_palabra():
    ''' Esta función retorna la palabra a adivinar.'''
    #Encierro la lectura del archivo en un bloque try except
    try:
        # Abro archivo de palabras
        conj_palabras= open ('palabrasJuego.txt','r')
        palabras = json.load(conj_palabras)
    #En caso de levantarse la excepción inicializo palabras con datos fijos
    #Obsevar que se cambiaron algunas cosas:
    #       1- La clave es cadena e incorporamos
    #       2- Incorporamos el tema
    except:
        palabras = {'1':['animales',['gato', 'perro','pato','elefante','lobo']],
                    '2':['colores', ['rojo','azul','verde','amarillo']],
                    '3':['comidas', ['milanesa','pure','pizza','salchicha']]
                    }

    # Pido que el jugador elija un tema. CAMBIADO porque ahora el tema depende
    # de lo que se levantó del archivo

    print ('Elije un tema:')
    for tema in palabras:
        print('\t', tema, ':', palabras[tema][0])

    #CAMBIO porque ahora la clave del archivo es texto.
    tema=input ('Ingresa la opción: ')

    #Selecciono la palabra a trabajar
    #MODIFICADO:
    try:
        pal = palabras[tema][1][random.randrange(len(palabras[tema][1]))]
    except:
        print("\t¡¡¡TEMA ERRÓNEO!!!")
        pal = defino_palabra_al_azar(palabras)


    return pal


def defino_palabra_al_azar(palabras):
    ''' Esta función retorna la palabra a adivinar elegida al azar.'''

    tema = random.choice(list(palabras.keys()))
    print('\tLa palabra corresponde al siguiente tema elegido al azar:',palabras[tema][0])
    return palabras[tema][1][random.randrange(len(palabras[tema]))]

def muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta):
    ''' Esta  función muestra el tablero de acuerdo al estado del juego'''

    print(ahorcado[cantidad_partes_cuerpo])
    print()

    pal_separada = '_' * len(pal_secreta)

    for i in range(len(pal_secreta)): # reemplaza los guines por las letras correctas
        if pal_secreta[i] in letras_correctas:
            pal_separada = pal_separada[:i] + pal_secreta[i] + pal_separada[i+1:]

    for letra in pal_separada: # muestra la palabra con los espacios que faltan completar
        print(letra, end=' ')



def jugada():
    ''' Obtiene la letra que el jugador ingrese'''

    letra = input('Ingresa una letra: ')
    return letra.lower()



#Selecciono la palabra a trabajar
pal_secreta = defino_palabra()

cantidad_partes_cuerpo = 0
letras_correctas = ''

#comienza el juego
sigue = True

while sigue:

    muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta)

    letra = jugada()

    # Si hay al menos una aparición de la letra..
    if letra in pal_secreta:
        letras_correctas = letras_correctas + letra

        # Chequeamos si ganó
        gane = True
        i = 0
        while gane and i < len(pal_secreta):
            if pal_secreta[i] not in letras_correctas:
                gane = False
            i = i + 1

        if gane:
            print('Ganaste')
            muestro_tablero(letras_correctas, cantidad_partes_cuerpo, pal_secreta)
            sigue = False

    else:
        #si se equivocó completo el cuerpo
        cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1

        if cantidad_partes_cuerpo == len(ahorcado):
            print ('Perdiste!. La palabra era:', pal_secreta)
            sigue = False
