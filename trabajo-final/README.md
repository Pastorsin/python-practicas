# Aplicación de clips para armar historias
Aplicación que genera clips cortos de videos desarrollada por Andrés Milla, Leonel Mandarino para el Seminario de Lenguajes Python 2018
## Ejecución
Para ejecutar la aplicación
1. <b>Asegurese de tener mysqclient</b>
    <br>``` apt-get install libmysqlclient-dev``` 
2. <b>Instale las dependencias:</b>
    <br>``` pip3 install -r requirements.txt```
3. <b>Ejecute app.py con python3:</b>
    <br>```python3 app.py```

* <i>La aplicación fue testeada en <b>Ubuntu 18.04 LTS</b></i>

## Clip educativo
Para ver el clip educativo elija como nombre de usuario: <b>grupo 7</b> y seleccione el clip: <b>Lina desobediente</b>
* <i>Dicho clip es una versión modificada del siguiente cuento: http://www.waece.org/cuentos/77.htm</i>

## Recursos
<i>Todos los recursos son de libre uso.</i>
* Imágenes:
    * Fondo de la aplicación: https://pixabay.com/es/resumen-de-fondo-rojo-1780374/ | Autor: [Tomislav Jakupec](https://pixabay.com/es/users/tommyvideo-3092371/)
    * Botón de check: https://es.wikipedia.org/wiki/Archivo:Light_green_check.svg | Autor: [Gmaxwell](https://commons.wikimedia.org/wiki/User:Gmaxwell)
    * <i>Las demás imágenes son contenido propio desarrolladas en Photoshop, también son de libre uso</i>
    * <i>Algunas imágenes se extraen desde [Flickr](https://www.flickr.com/) sin copyright mediante el módulo [pattern](https://www.clips.uantwerpen.be/pages/pattern) </i>
* Sonidos:
    * agua.ogg : https://freesound.org/people/InspectorJ/sounds/421184/ | Autor: [InspectorJ](https://freesound.org/people/InspectorJ/)
    * aplausos.ogg : https://freesound.org/people/Camo1018/sounds/425663/ | Autor: [Camo1018](https://freesound.org/people/Camo1018/)
    * explosion.ogg : https://freesound.org/people/Iwiploppenisse/sounds/156031/ | Autor: [Iwiploppenisse](https://freesound.org/people/Iwiploppenisse/)
    * festejo.ogg : https://freesound.org/people/chripei/sounds/165491/ | Autor: [chripei](https://freesound.org/people/chripei/)
    * pasos.ogg : https://freesound.org/people/abel_K/sounds/69296/ | Autor: [InspectorJ](https://freesound.org/people/InspectorJ/)
    * risa malvada.ogg: https://freesound.org/people/ZyryTSounds/sounds/219110/ | Autor: [ZyryTSounds](https://freesound.org/people/ZyryTSounds/)
* Fuentes:
    * Josefin Sans: https://fonts.google.com/specimen/Josefin+Sans | Autor: [Santiago Orozco]()
    * Open Sans: https://fonts.google.com/specimen/Open+Sans | Autor: [Steve Matteson](https://twitter.com/@SteveMatteson1)
    * Shrikhand: https://fonts.google.com/specimen/Shrikhand | Autor: [Jonny Pinhorn](https://twitter.com/jonpinhorn_type)
    * Wendy One: https://fonts.google.com/specimen/Wendy+One | Autor: [Alejandro Inler]()
* Música:
    * Lullaby-for phil : https://www.jamendo.com/track/1408401/lullaby-for-phil | Autor: [Alexey Baranov](https://www.jamendo.com/artist/496168/alexey-baranov)
    * J'm'imaginais (version brésilienne) : https://www.jamendo.com/track/3096/j-m-imaginais-version-bresilienne | Autor: [Drdjekill](https://www.jamendo.com/artist/486/drdjekill)
    * Universal Funk : https://www.jamendo.com/track/1466090/universal-funk | Autor: [Duo Teslar](https://www.jamendo.com/artist/501885/duo-teslar)
    * Constellate : https://www.jamendo.com/track/1549463/constellate | Autor: [Fleurie](https://www.jamendo.com/artist/509188/fleurie)
    * Work At Night: https://www.jamendo.com/track/524772/work-at-night | Autor: [Professor Kliq](https://www.jamendo.com/artist/339989/professor-kliq)
    * Day's End: https://www.jamendo.com/track/603761/day-s-end | Autor: [Shearer](https://www.jamendo.com/artist/2485/shearer)
    * God Save The DJ : https://www.jamendo.com/track/887210/god-save-the-dj | Autor: [We are FM](https://www.jamendo.com/artist/376782/we-are-fm)
    * IDK : https://www.jamendo.com/track/1531154/idk | Autor: [DLX](https://www.jamendo.com/artist/474132/the-dlx)
* <i>La música y los sonidos fueron convertidos a .ogg mediante https://audio.online-convert.com/es/convertir-a-ogg</i>

* Juegos:
    * Snake : https://github.com/apaar97/SnakeGame | Autor: [apaar97](https://github.com/apaar97)

## Presentación
* Introducción
    * [MODELADO](https://gitlab.catedras.linti.unlp.edu.ar/python2018/trabajo/grupo7/blob/master/modelado/modelo.jpg)
    * Secciones / Escenas » Dividimos cada sección en clases con su comportamiento.
    * Cambio de escena » Diccionario.
    * Eventos: 
        * Funcionalidad de los manejadores (botones, tipeo, etc).
    * Estructura de los directorios, Archivos, Base de datos:
        * Puntaje SNAKE
        * [Clips](https://gitlab.catedras.linti.unlp.edu.ar/python2018/trabajo/grupo7/blob/master/modelado/guardado_de_clips.json)
* Secciones FUNCIONALIDAD
    * MENU
        * Inicio de Sesión 
            * Funcionamiento con String
            * Directorio (Usuario existente, usuario nuevo)
    * JUEGO
        * Guarda el puntaje más alto del jugador
        * Top 10
        * Archivo de score
    * CLIPS
        * MIS CLIPS
            * Carga los clips desde el JSON
        * ARMADO
            * Música
            * Obtención de imágenes » Elegir y llevar al editor de fotos
            * Finalizado » Chequea que no exista un nombre igual
        * EDITOR DE FOTOS
            * Imágenes de resplado » FILTRO / CTRL+Z
            * Sonido
            * Guardar la imagen editada » SCREENSHOT
            * Agregar Clip » YA GUARDA LA IMAGEN
        * EDITOR DEL CLIP
        * REPRODUCTOR
            * Como funciona sin congelar el programa
        