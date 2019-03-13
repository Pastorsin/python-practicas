# -*- coding: utf-8 -*-

import pygame
import pygame.camera
import os
import time
import json
from pattern.web import Flickr, extension
from herramientas.Utilidades import Tools


class ArmarClip():
    """ Permite la creacion del clip a traves de la seleccion
        y edición de imagenes
    """

    def __init__(self, pantalla, ancho, alto, usuario):
        """ Valores por defecto de la pestaña """

        # Pantalla
        self.ALTO = alto
        self.ANCHO = ancho
        self.pantalla = pantalla

        # Colores
        self.NEGRO = (0, 0, 0)
        self.ROJO = (244, 36, 40)
        self.OXFORD_BLUE = (3, 15, 69)
        self.VERDE = (79, 170, 90)
        self.DEEP_CARMINE = (170, 40, 57)
        self.BLANCO = (241, 241, 241)
        self.CELESTE_LINDO = (40, 152, 178)
        self.BLANCO_LINDO = (253, 250, 251)
        self.TIGERS_EYE = (224, 159, 62)
        self.VERDE_FUERTE = (51, 255, 51)
        self.GRIS = (194, 214, 214)

        # Fuente
        self.font_50 = pygame.font.SysFont('Bank Gothic', 70)
        self.font_30 = pygame.font.SysFont('Bank Gothic', 30)
        self.font_20 = pygame.font.SysFont('Bank Gothic', 20)

        # Inicializaciones
        self.tools = Tools(self.pantalla)
        self.interfaz()

        # Usuario
        self.usuario = usuario

    def interfaz(self):
        """ Manejo de la intefaz principal """

        # Tamaños formato x-y
        self.rec_pequeño = (100, 50)
        self.rec_medio = ((self.ANCHO - 300) / 3 - 20, 50)
        self.rec_grande = (self.ANCHO - 300, 75)
        self.cuadrado = ((self.ANCHO - 300) / 3 - 20,
                         (self.ANCHO - 300) / 3 - 20)

        # Botones principales
        self.botones()

        # Render del texto sobre los botones
        self.texto_botones()

        # Grilla de rectangulos para las imagenes
        self.grilla_imagenes()

    def botones(self):
        """ Coloca los botones sobre la pantalla """
        self.musica = pygame.draw.rect(self.pantalla, self.ROJO,
                                       (self.ANCHO / 2 - self.rec_medio[0] / 2,
                                        10) + self.rec_medio)
        self.imagenes = pygame.draw.rect(self.pantalla, self.ROJO,
                                         (self.ANCHO / 2 - self.rec_grande[0] / 2,
                                          75) + self.rec_grande)
        self.finalizar = pygame.draw.rect(self.pantalla, self.VERDE,
                                          (self.ANCHO - 100, self.ALTO - 50) +
                                          self.rec_pequeño)
        self.atras = pygame.draw.rect(self.pantalla, self.DEEP_CARMINE,
                                      (0, self.ALTO - 50) + self.rec_pequeño)

        self.pos_titulo = self.imagenes.topleft

        # Opciones de imagenes
        self.predefinidas = pygame.draw.rect(self.pantalla, self.DEEP_CARMINE,
                                             (self.pos_titulo[0] + 10, 150) +
                                             self.rec_medio)

        self.camara = pygame.draw.rect(self.pantalla, self.CELESTE_LINDO,
                                       (self.pos_titulo[0] + 10 + 2 * self.imagenes.width / 3, 150) +
                                       self.rec_medio)
        self.caja_buscar()

        self.caja_de_imagenes()

    def texto_botones(self):
        """ Render del texto sobre los botones """
        self.clicks = {'Elegir Musica': (self.musica, self.font_30),
                       'AGREGAR IMAGENES': (self.imagenes, self.font_50),
                       'Finalizar': (self.finalizar, self.font_30),
                       'Atras': (self.atras, self.font_30),
                       'Predefinidas': (self.predefinidas, self.font_30),
                       'Buscar': (self.buscar, self.font_30),
                       'Camara': (self.camara, self.font_30)
                       }
        for clave, valor in self.clicks.items():
            self.tools.sombrear(clave, self.BLANCO, self.OXFORD_BLUE,
                                valor[1], valor[0])

    def grilla_imagenes(self):
        """ Renderización de la grilla donde van a estar las imagenes """
        pos = 0
        self.pos_caja = self.caja_imagenes.topleft
        ejeY = self.pos_caja[1]
        self.grilla = []
        for columna in range(2):
            for fila in range(3):
                img = pygame.draw.rect(self.pantalla, self.TIGERS_EYE,
                                       (self.pos_caja[0] + 10 + fila * self.imagenes.width / 3,
                                        ejeY + 10) + self.cuadrado)
                self.clicks[str(pos)] = (img, 0)
                self.grilla.append(img)
                pos += 1
            ejeY += 240

    def caja_de_imagenes(self):
        """Coloca la caja en donde van a estar las imagenes,
           se usa principalmente para limpiar"""
        self.caja_imagenes = pygame.draw.rect(self.pantalla, self.BLANCO_LINDO,
                                              (self.pos_titulo[0],
                                               self.pos_titulo[1] + 135,
                                               self.ANCHO - 300, 480))

    def caja_buscar(self):
        """ Coloca la caja en donde el usuario va a escribir """
        self.buscar = pygame.draw.rect(self.pantalla, self.VERDE,
                                       (self.pos_titulo[0] + 10 + self.imagenes.width / 3, 150) +
                                       self.rec_medio)

# Funcionalidades

    def chequear_botones(self, pos_mouse):
        """ Identifica cual de los botones del menú fue presionado """
        return self.tools.consulta_botones(pos_mouse, self.clicks)

    def actualizar_grilla(self, seccion):
        """ Inserta las imagenes del directorio de imagenes en la grilla """

        # Limpio lo que haya:
        self.caja_de_imagenes()
        self.grilla_imagenes()
        # Actualizacion de imagenes:
        directorio = os.path.join(os.getcwd(), 'imagenes', seccion)
        list_dir = os.listdir(directorio)
        list_dir.sort()
        i = 0
        for img in list_dir[:6]:
            imagen = pygame.image.load(os.path.join(directorio, img))
            imagen = pygame.transform.scale(imagen, ((self.ANCHO - 300) // 3 - 20,
                                                     (self.ANCHO - 300) // 3 - 20))
            self.pantalla.blit(imagen, self.grilla[i].topleft)
            i += 1

    def actualizar_camara(self):
        """ Saca una foto y la coloca en la caja de imagenes"""

        # Limpio lo que haya
        self.caja_de_imagenes()
        # Camara
        try:
            pygame.camera.init()
            self.cam = pygame.camera.Camera('/dev/video0', (640, 480), 'RGB')
            self.cam.start()
            self.captura = pygame.surface.Surface((640, 480), 0, self.pantalla)
            self.captura = self.cam.get_image(self.captura)
            pygame.image.save(self.captura, os.path.join('imagenes', 'camara', '0.jpg'))
            self.pantalla.blit(
                self.captura, (self.pos_caja[0] + 30, self.pos_caja[1]))
            self.cam.stop()
        except Exception:
            self.caja_de_imagenes()
            self.tools.sombrear('Se ha producido un error intentando obtener la camara lo sentimos...',
                                self.NEGRO, self.BLANCO_LINDO,
                                self.font_30, self.caja_imagenes)

    def interfaz_cancion(self):
        """ Muestra las canciones en pantalla """
        self.caja_imagenes = pygame.draw.rect(self.pantalla, self.TIGERS_EYE,
                                              (self.pos_titulo[0],
                                               self.pos_titulo[1] + 135,
                                               self.ANCHO - 300, 480))
        self.mostrar_canciones()

    def mostrar_canciones(self):
        """ Busca las canciones en el directorio y las imprime en pantalla """
        # obtengo las canciones
        directorio_canciones = os.path.join('audio', 'canciones')
        canciones = os.listdir(directorio_canciones)
        canciones = list(sorted(canciones))
        # las muestro en la grilla
        altura_fila = self.caja_imagenes.height/len(canciones)
        i = 0
        for cancion in canciones:
            linea = pygame.draw.rect(self.pantalla, self.NEGRO,
                                     (self.caja_imagenes[0],
                                      self.caja_imagenes[1] + altura_fila*i) +
                                     (self.caja_imagenes.width, altura_fila),
                                     1)
            elemento = self.font_30.render(cancion.rstrip('.ogg'), True,
                                           self.OXFORD_BLUE)
            self.pantalla.blit(elemento, (linea.topleft[0] + 20,
                                          linea.topleft[1] + 20))
            self.clicks[str(i)] = (linea, 0)
            i += 1

    def boton_loop(self):
        """ Boton que permite el loop de la cancion en el clip """
        # me quedo con la pos del boton del loop
        pos = self.caja_imagenes.topright
        pos = (pos[0]+20, pos[1]+15)
        loop = pygame.draw.rect(self.pantalla, self.ROJO, pos + (30, 30))
        texto_loop = self.font_30.render('Loop', True,
                                         self.BLANCO_LINDO)
        self.pantalla.blit(texto_loop, (loop.topright[0]+5,
                                        loop.topright[1]+8))
        self.cancion_loop = False
        self.clicks['Loop'] = (loop, 0)

    def switch_loop(self):
        """ switch grafico del prendido y apagado del loop """
        pos = self.caja_imagenes.topright
        pos = (pos[0]+20, pos[1]+15)
        if self.cancion_loop:
            pygame.draw.rect(self.pantalla, self.ROJO, pos + (30, 30))
            self.cancion_loop = False
        else:
            pygame.draw.rect(self.pantalla, self.VERDE, pos + (30, 30))
            self.cancion_loop = True

    def seleccionar_cancion(self, ruta, boton):
        """ Check al clickear una cancion """
        self.interfaz_cancion()
        # tengo que poner el visto en la cancion que clickeó
        seleccion = pygame.image.load(os.path.join('imagenes', 'check_ok.png'))
        seleccion = pygame.transform.scale(seleccion, (50, 50))
        pos_visto = self.clicks[boton][0].topright
        pos_visto = (pos_visto[0]-60, pos_visto[1]+5)
        self.pantalla.blit(seleccion, pos_visto)
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()

# Lógica del buscar:

    def espera(self, carga):
        """ Informa al usuario que se está realizando la búsqueda """
        self.caja_de_imagenes()  # Limpiar
        tamaniox = 200 / 6 * (carga + 1)  # progreso de la barrita
        # Rectangulos:
        self.fondo_barrita = pygame.draw.rect(self.pantalla, self.GRIS, (
            self.caja_imagenes.centerx - 101, self.caja_imagenes.centery + 34, 202, 22))
        self.contorno_barrita = pygame.draw.rect(self.pantalla, self.VERDE, (
            self.caja_imagenes.centerx - 101, self.caja_imagenes.centery + 34, 202, 22), 1)
        self.barrita = pygame.draw.rect(self.pantalla, self.VERDE_FUERTE, (
            self.caja_imagenes.centerx - 100, self.caja_imagenes.centery + 35, tamaniox, 20))
        # Texto:
        self.tools.sombrear('Estamos buscando las imágenes, por favor espere . . .',
                            self.NEGRO, self.BLANCO_LINDO,
                            self.font_30, self.caja_imagenes)
        elemento = self.font_20.render(
            str(tamaniox * 100 // 200) + '%', True, self.NEGRO)
        pos = self.tools.centrar(self.contorno_barrita, elemento)
        self.pantalla.blit(elemento, pos)
        # Refresco:
        pygame.display.update()

    def buscar_enter(self):
        """Al presionar enter busca en Flickr"""
        try:
            self.buscar_Flickr(self.texto)
            self.actualizar_grilla('busqueda')
        except:
            self.caja_de_imagenes()
            self.tools.sombrear('Se ha producido un error con su busqueda, lo sentimos...',
                                self.NEGRO, self.BLANCO_LINDO,
                                self.font_30, self.caja_imagenes)

    def buscar_Flickr(self, texto):
        """ Busca en Flickr 6 imagenes y las guarda """
        engine = Flickr(license=None, throttle=0.5, language='es')
        i = 0
        for result in engine.search(texto, count=6, cached=True, copyright=False):
            self.espera(i)

            directorio = os.path.join(
                'imagenes', 'busqueda', str(i) + extension(result.url))
            f = open(directorio, 'wb')
            f.write(result.download(timeout=10))
            f.close()
            i += 1

# Procesado del texto

    def comenzar_buscar(self):
        """ Limpia la caja buscar e inicializa el texto a capturar """
        self.texto = ''
        self.renderizar_texto_buscar()

    def buscar_borrar(self):
        self.texto = self.texto[:-1]

    def dentro_limite(self, texto):
        """ Verifica si el texto no superó el limite
            de la caja que lo contiene """
        return self.tools.centrar(self.buscar, self.font_30.render(texto, True, self.BLANCO))[0] - 20 > self.buscar.left

    def actualizar_texto(self, caracter):
        self.texto += caracter

    def renderizar_texto_buscar(self):
        """
        Muestra el texto en la pantalla.
        Retorna si el límite fue o no superado.
        """
        if (self.dentro_limite(self.texto)):
            # Limpio pantalla
            self.caja_buscar()
            pygame.draw.line(self.pantalla, self.NEGRO,
                             (self.buscar.bottomleft[
                              0] + 20, self.buscar.bottomleft[1] - 10),
                             (self.buscar.bottomright[
                              0] - 20, self.buscar.bottomright[1] - 10),
                             3)
            # Renderiza el texto
            self.tools.sombrear(self.texto, self.BLANCO, self.OXFORD_BLUE,
                                self.font_30, self.buscar)
            return False
        else:
            return True
