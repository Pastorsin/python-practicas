import pygame
import os
import json
import time
from herramientas.Utilidades import Tools
from datetime import datetime


class Reproductor():
    """ Reproduce un clip ya realizado """

    def __init__(self, pantalla, ancho, alto, usuario, clip):
        # Valores por defecto
        self.pantalla = pantalla
        self.ANCHO = ancho
        self.ALTO = alto
        self.clip_elegido = clip
        # Usuario
        self.usuario = usuario
        # Secuencia de imagenes
        self.pos_img = 0
        self.loop = False
        self.fin = False
        self.duracion_img = -1
        self.auxiliar = 0
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
        # Fuentes
        self.font_45 = pygame.font.SysFont('Bank Gothic', 45)
        self.font_20 = pygame.font.SysFont('Bank Gothic', 20)
        # herramientas
        self.tools = Tools(self.pantalla)
        self.tamanio_img = (724, 620)
        self.cargar_datos_usuario()
        self.interfaz()

    def limpiar_pantalla(self):
        self.caja_pantalla = pygame.draw.rect(
            self.pantalla, self.BLANCO, (self.pantalla.get_rect().centerx - 724 / 2, 0, 724, 620))

    def cargar_datos_usuario(self):
        """ Carga los datos almacenados en el json del usuario """
        arch = open(os.path.join(
            os.getcwd(), 'archivos', 'usuarios.json'), 'r')
        self.datos = json.load(arch)
        self.clip = self.datos[self.usuario][self.clip_elegido]
        arch.close()

    def comenzar_musica(self):
        """ inicializa la musica en el clip """
        if self.clip['musica']['ruta'] and not self.fin:
            if pygame.mixer.music.get_busy():  # Si ya hay música, renaudo
                pygame.mixer.music.unpause()
            else:  # Si no hay música, reproduzco desde 0
                pygame.mixer.music.load(self.clip['musica']['ruta'])
                pygame.mixer.music.play(
                    loops=-1 if self.clip['musica']['loop'] else 0)

    def play(self):
        """ Inicia el reloj y comienza a reproducir las imágenes """
        self.inicio = time.time()
        time.clock()
        self.avanzar_imagen()

    def pausa(self):
        """ Setea la duración de la imagen para la próxima vez que aprieten play.
        Así completa lo que le falta. """
        # print('PAUSA',self.auxiliar)
        self.duracion_img = self.auxiliar

    def cambiar_imagen(self, duracion):
        """ Retorna si hay que cambiar o no de imagen """
        if self.clip['imagenes']:
            segundos = int(time.time() - self.inicio)
            self.auxiliar = duracion - segundos
            # print(duracion, '-', segundos, '=', duracion - segundos)
            return duracion - segundos < 0 and not self.fin
        else:
            return False

    def avanzar_imagen(self):
        """ Reproduce las imagenes """
        # Si hay que cambiar la imagen
        if self.cambiar_imagen(self.duracion_img):
            # Si no terminó el clip
            if (self.pos_img < len(self.clip['imagenes'])):
                # Inicia el RELOJ
                self.inicio = time.time()
                time.clock()
                imagen_actual = self.clip['imagenes'][self.pos_img]
                # Carga la imagen
                self.img = pygame.image.load(imagen_actual['directorio'])
                # Muestra la imagen
                self.pantalla.blit(self.img, self.caja_pantalla.topleft)
                # Reproduce el sonido
                if imagen_actual['sonido']:
                    pygame.mixer.Sound(imagen_actual['sonido']).play()
                self.duracion_img = int(self.clip['imagenes'][
                                        self.pos_img]['duracion'])
                self.pos_img += 1
            elif self.loop:
                self.pos_img = 0
            else:
                self.fin = True

    def fin_clip(self, texto):
        """ Indicador de fin del clip """
        self.fin = True
        self.pos_img = 0
        # Avisa que terminó
        self.limpiar_pantalla()
        self.tools.sombrear(texto, self.NEGRO, self.VERDE,
                            self.font_45, self.caja_pantalla)
        # Para la música
        pygame.mixer.music.fadeout(500)
        # Actualiza la pantalla para no perder el tiempo congelado
        pygame.display.update()
        time.sleep(2)

    def interfaz(self):
        """ Interfaz del reproductor """
        # Opacidad
        opacidad = pygame.Surface((self.ANCHO, self.ALTO), pygame.SRCALPHA)
        opacidad.fill((26, 26, 26, 180))
        self.pantalla.blit(opacidad, (0, 0))
        # Cajas
        self.limpiar_pantalla()
        self.caja_botones = pygame.draw.rect(
            self.pantalla, (26, 26, 26), (0, self.ALTO - 100, self.ANCHO, 100))
        # Botones para reproducir
        self.img_play = pygame.image.load(
            os.path.join('imagenes', 'play.png'))
        self.img_pausa = pygame.image.load(
            os.path.join('imagenes', 'pausa.png'))
        self.img_stop = pygame.image.load(
            os.path.join('imagenes', 'stop.png'))
        self.img_loop = pygame.image.load(
            os.path.join('imagenes', 'loop_off.png'))
        # Rectángulos de los botones
        self.atras = pygame.draw.rect(self.pantalla, self.DEEP_CARMINE,
                                      (self.pantalla.get_rect().width - 80, 0, 80, 30))
        self.tools.sombrear('Atrás', self.BLANCO,
                            self.OXFORD_BLUE, self.font_20, self.atras)
        self.rect_play = self.img_play.get_rect().move(
            20, self.caja_botones.centery - self.img_play.get_height() / 2)
        self.rect_pausa = self.img_pausa.get_rect().move(
            100, self.caja_botones.centery - self.img_play.get_height() / 2)
        self.rect_stop = self.img_stop.get_rect().move(
            180, self.caja_botones.centery - self.img_play.get_height() / 2)
        self.rect_loop = self.img_loop.get_rect().move(
            self.tools.centrar(self.caja_botones, self.img_stop))
        # Renderizado
        self.pantalla.blit(
            self.img_play, (20, self.caja_botones.centery - self.img_play.get_height() / 2))
        self.pantalla.blit(
            self.img_pausa, (100, self.caja_botones.centery - self.img_play.get_height() / 2))
        self.pantalla.blit(
            self.img_stop, (180, self.caja_botones.centery - self.img_play.get_height() / 2))
        self.pantalla.blit(
            self.img_loop, (self.tools.centrar(self.caja_botones, self.img_stop)))
        # Clicks
        self.clicks = {
            'play': (self.rect_play, 0),
            'loop': (self.rect_loop, 0),
            'pausa': (self.rect_pausa, 0),
            'stop': (self.rect_stop, 0),
            'atras': (self.atras, 0)
        }

    def actualizar_loop(self):
        """ Le da comportamiento al boton de loop """
        # Limpio el sector
        rect = pygame.draw.rect(
            self.pantalla, (26, 26, 26), self.rect_loop.topleft + self.rect_loop.size)
        # Informo al usuario si el loop está activado
        img = 'loop_off.png' if self.loop else 'loop_on.png'
        self.img_loop = pygame.image.load(os.path.join('imagenes', img))
        self.pantalla.blit(
            self.img_loop, (self.tools.centrar(self.caja_botones, self.img_stop)))
        # Actualizo estado del loop
        self.loop = not self.loop

    def chequear_botones(self, mouse):
        return self.tools.consulta_botones(mouse, self.clicks)
