# Python-Practicas
Ejercicios realizados de las pŕacticas del Seminario de Lenguajes de Python UNLP 2018






## Práctica 1 - 2018

### Parte I: Conceptos Básicos
  1. Dado el siguiente string, generar una lista donde cada elemento sea una palabra, utilizando el espacio (‘ ‘) como separador:<br>**frase** = *"Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple."*
  
2. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras (separadas por ’ ’), y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No importan las mayúsculas y minúsculas.

3. Genere una nueva lista con todas las palabras de la **frase** dada en el ejercicio 1 en mayúsculas.

4. Dada la lista de palabras generada en el ejercicio 3, arme un string con la frase armada con todas ellas separadas por un único espacio en blanco.

5. Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula. <br>**frase** = *"Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."*

6. Dada la lista generada en el ejercicio 3 genere una estructura a la que se pueda acceder directamente a una lista de strings según la cantidad de caracteres de cada uno.

7. Para registrar las actividades de un usuario en un juego dado se requiere guardar los siguientes datos: nombre del jugador, nivel alcanzado en el juego, puntaje máximo y tiempo de juego. Utilizando la estructura que considere más adecuada, almacenar la información de varios usuarios ingresados desde teclado. Tener en cuenta que se necesita acceder a un usuario determinado en forma directa sin recorrerla.

8. Con la estructura generada en el ejercicio 7, imprimir los datos de un usuario dado sin recorrer la estructura. ¿La elección sobre la estructura fue adecuada? ¿Cuál usó?

9. Con la estructura generada en el ejercicio 7, imprima solos los nombres de los usuarios que jugaron sin recorrer la estructura.

10. Dada la estructura generada en el ejercicio 7 imprimir el usuario que obtuvo mayor puntaje.

11. Dada la estructura del ejercicio 7, ingresar los datos correspondientes a la jugada de un usuario. Si el usuario existe previamente, guardar los datos de mayor puntaje. Luego imprimir el ranking de los 10 mejores puntajes.

12. Dado el siguiente diccionario donde las claves son nombres de animales y los valores representan posiciones: <br>```anim={’Gato Montes’:2,’Yacare overo’:4,’Boa acuática’:5}``` <br>Imprimir un string por cada animal de la estructura, reemplazando sus caracteres por el string *’_ ’* (inclusive los espacios en blanco) salvo el caracter correspondiente al valor del mismo. <br>**Ejemplo:** <br>Gato Montes tiene asociado el _valor_ 2: <br>_ _ t _ _ _ _ _ _ _ _ <br>0 1 2 3 4 5 6 7 8 9 10 

13. Dada una lista con nombres de imágenes:
imagenes=['im1','im2','im3']
Generar una estructura que asocie 3 coordenadas ingresadas por teclado( _x_ 1 _, y_ 1 ),( _x_ 2 _, y_ 2 )y
( _x_ 3 _, y_ 3 ), con cada elemento de la lista (en el mismo orden en que son ingresadas). Además
verifique, mientras se van ingresando las coordenadas, que no hayan repetidas para una misma
imagen; en dicho caso deberá volver a ingresarla.

14. Dada una estructura: <br>```tam={'im1':[(x_1,y_1),(x_2,y_2)],'im2':[(x_1,y_1),(x_2,y_2)],'im3':[(x_1,y_1),(x_2,y_2)]}``` <br>Donde( x 1 , y 1 ) , ( x 2 , y 2 )representan el extremo izquierdo inferior y el extremo derecho superior del tamaño de cada imagen, verifique con la estructura generada en el ejercicio 13 si cada coordenada no queda fuera del tamaño de la imagen.

### Parte II: Encontramos errores

1. Corrija los errores de los siguientes códigos:
    ```
    puntaje = {}
    puntaje[30] = 'Ada'
    puntaje[40] = 'Hedy Lammar'
    puntaje[45] = 'Colossus'
    puntaje[47] = 'Angela Ruiz Robles'
    for puntaje,nombre in puntaje.keys():
       print ('{} puntaje {}'. **format** (nombre, puntaje))
    ```
2. Usando el mismo diccionario del ejercicio anterior, ejecutar:
    ```
    for puntaje in puntaje.keys():
       print (puntaje)
    for cada in sorted (puntaje,reverse=True):
       print (puntaje[cada],cada)
    ```
3. ¿Qué sucede con el siguiente código?
    ```
    lista1 = ['perro', 4, True, (6,7)]
    lista2 = [False, 'casa', 9, [3, 4, 'gato']]
    lista3 = []
    lista_aux = lista1.extend(lista2)
    for elem in lista_aux:
       if type (elem) is str :
          lista3.append(elem)
    print (lista3)
    ```
4. Resuelva el problema:
    ```
    bb = ['Si', 'mucho', 'con', 'computadoras,', 'eventualmente', 'que', 'te']
    for each in bb
       print ( **len** (each))
    ```






## Práctica 2 - 2018

*En esta práctica vamos a trabajar con el módulo pattern.es que permite trabajar con el
análisis sintáctico del idioma.
Para más información sobre este módulo en español y en inglés.*

1. Dada una lista con nombres de colores: ```colores = ['azul','amarillo','rojo','blanco','negro']```<br>
y una lista con coordenadas:```coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]```. <br>
Generar una estructura que contenga coordenadas y un color asociado. La forma de
asociar las coordenadas con el color debe ser aleatoria sin importar que se repitan los
colores elegidos.
Generar una estructura que contenga coordenadas y un color asociado. La forma de
asociar las coordenadas con el color debe ser aleatoria sin que se repitan los colores.

2. Usando el diccionario del Ejercicio 1, acceder a las coordenadas y, según el color asociado, ejecute una función, donde las funciones planteen la resolución de ejercicios simples como ser:
    1. Suma de dos números que se generen en forma aleatoria cada vez que se llama a la
          función, reciba el resultado por teclado y verifique el resultado.
    2. Dada la estructura que contiene palabras clasificadas según su acentuación: ```palabras = [('grave',['molesto']),('aguda',['ratón']), ('esdrujula',['murciélago'])]``` cada vez que se ejecuta la función elija una palabra en forma aleatoria, consulte al usuario sobre el tipo que es por su acentuación y verifique la respuesta.

3. Utilizar como estructura de datos de referencia la generada en el Ejercicio 7 de la Práctica 1 y generar funciones que ejecuten lo siguiente:
    1. Imprimir los 10 primeros puntajes de la estructura.
    2. Imprimir los datos de los usuarios ordenados alfabéticamente por apellido.
    3. Imprimir los datos de los usuarios ordenados por nivel alcanzado.
4. Defina una función denominada **convertir** que reciba un diccionario con dos keys: ’s’ y ’p’. Donde ’s’ indica que la lista asociada contiene palabras en singular y ’p’ indica que la lista asociada contiene palabras en plural. La función debe retornar un diccionario con los sustantivos invertidos, es decir, los de singular en plural y los de plural en singular. <br><br>**Nota:** *utilice el módulopattern.es.* <br>*Ejemplo:  <br>```cambiar = {'s':['gato','caballo', 'silla'],'p': ['informaticas','psicologas', 'ingenieras']}```<br>devuelve:<br>```{'p': ['informatica', 'psicologa', 'ingeniera'], 's': ['gatos', 'caballos', 'sillas']}```*
5. Utilizando el módulo **pattern.es** defina una función denominada **verbosInfinitivos** que reciba un string, el cual puede contener varias oraciones y devuelva una lista de los verbos en infinitivo.
6. Imprima un listado de los archivos que contiene el directorio actual. La información a mostrar
    deberá ser nombre de archivo, tamaño y fecha de su último acceso. Tener en cuenta que
    funcione en cualquier plataforma.
7. Realice las siguientes operaciones utilizando funcioneslambdaen el listado de archivos del
    ejercicio anterior:
    1.  Obtener una lista de los archivos del directorio con la primer letra del nombre de cada
          uno en mayúscula
    2. Generar una lista con aquellos archivos que han sido modificados en los últimos 3 días
    3. Imprimir el tamaño total de los archivos
    4. Ordenar los archivos del directorio por tamaño
8. Dada la frase del ejercicio 1 de la Práctica 1, imprima sus 3 palabras más utilizadas mediante
    la clase Counter del módulo collections.
9. Dado un párrafo ingresado por teclado, imprima los 3 verbos más usados en él (en infinitivo,
    del más común al menos común), junto con la cantidad de apariciones de cada uno utilizando
    Counter.
    Aclaración: No importa el orden de los verbos cuando tienen igual cantidad de repeticiones.
    Utilice el módulopattern.es.
    Ejemplo:

    *   ```Este es un párrafo de prueba. El verbo ser, será el mas utilizado. El otro será crear, por eso se creó la oración de esta manera. Por último, se creará esta oración que posee el tercer verbo: poseer. Nada más que decir. ```
    * ```
      ser 4
      crear 3
      poseer 2
      ```
      
## Práctica 3 - 2018

## Práctica 4 - 2018
