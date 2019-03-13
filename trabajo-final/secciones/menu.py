# -*- coding: utf-8 -*-

import pygame
import shutil
import os
import json
from herramientas.Utilidades import Tools


class Menu():
    """Menu principal de la aplicación"""

    def __init__(self, pantalla, ancho, alto, usuario):
        """Valores por defecto propios del menú"""
        # Colores
        self.COLOR_FONDO_MENU = (179, 0, 0)
        self.ROJO = (244, 36, 40)
        self.BLANCO = (255, 230, 230)
        self.GRIS = (194, 214, 214)
        self.NEGRO = (0, 0, 0)
        self.OXFORD_BLUE = (3, 15, 69)
        self.NEGRO = (0, 0, 0)
        # Pantalla
        self.ANCHO = ancho
        self.ALTO = alto
        self.pantalla = pantalla
        # Fuentes
        self.font_72 = pygame.font.SysFont('monaco', 65)
        self.font_30 = pygame.font.SysFont('Bank Gothic', 30)
        # Inicializaciones
        self.tools = Tools(self.pantalla)
        self.clicks = {}
        self.usuario = usuario
        self.interfaz(self.pantalla)

    def interfaz(self, pantalla):
        if self.usuario == '':
            self.sesion(pantalla.get_rect())
        else:
            self.botones(pantalla.get_rect())

    def sesion(self, pantalla):
        """ Pone la interfaz del inicio de sesion del usuario """
        pos_titulo = (pantalla.center[0] - 250, pantalla.center[1] - 200)
        self.titulo = pygame.draw.rect(self.pantalla, self.ROJO,
                                       pos_titulo + (500, 100))
        self.tools.sombrear('Ingrese su nombre', self.GRIS, (0, 0, 0),
                            self.font_72, self.titulo)
        self.limpiar_campo()
        self.clicks['campo'] = (self.campo, self.font_30)

    def limpiar_campo(self):
        """ Limpia el campo del input """
        pos_campo = (self.titulo.bottomleft[0] - 100,
                     self.titulo.bottomleft[1] + 20)
        self.campo = pygame.draw.rect(self.pantalla, self.BLANCO,
                                      pos_campo + (700, 100))

    def comenzar_escribir(self):
        """ Limpia la caja campo e inicializa el texto a capturar """
        self.texto = ''
        self.renderizar_texto_escrito()

    def renderizar_texto_escrito(self):
        """
        Muestra el texto en la pantalla.
        Retorna si el límite fue o no superado.
        """
        if (self.dentro_limite(self.texto)):
            # Limpio pantalla
            self.limpiar_campo()
            pygame.draw.line(self.pantalla, self.NEGRO,
                             (self.campo.bottomleft[0] + 20,
                              self.campo.bottomleft[1] - 10),
                             (self.campo.bottomright[0] - 20,
                              self.campo.bottomright[1] - 10),
                             3)
            # Renderiza el texto
            self.tools.sombrear(self.texto, self.OXFORD_BLUE, self.BLANCO,
                                self.font_72, self.campo)
            return False
        else:
            return True

    def borrar(self):
        self.texto = self.texto[:-1]

    def actualizar_texto(self, caracter):
        self.texto += caracter

    def dentro_limite(self, texto):
        """ Verifica si el texto no superó el limite
            de la caja que lo contiene """
        pos = self.tools.centrar(self.campo,
                                 self.font_72.render(texto, True, self.BLANCO))
        return pos[0] - 20 > self.campo.left

    def enter(self):
        """Al presionar enter guarda o carga el usuario"""
        if self.texto == '':
            self.texto = 'anónimo'
        try:
            self.usuario = self.texto
            # Crea la carpeta del usuario en caso de no existir
            directorios = list(
                filter(lambda x: os.path.isdir(os.path.join(os.getcwd(),
                                                            'archivos', x)),
                       os.listdir('archivos')))
            if self.usuario not in directorios:
                os.mkdir(os.path.join('archivos', self.usuario))
            else:
                self.aprobado()
            # Crea la carpeta temporal
            clip_temp = os.path.join('archivos', self.usuario, 'temp')
            if os.path.exists(clip_temp):  # Si existe la carpeta, la elimina
                shutil.rmtree(clip_temp)
            os.mkdir(clip_temp)
        except FloatingPointError:
            pass

    def aprobado(self):
        """ Muestra el icono indicador de que el usuario existe """
        icono = pygame.image.load(os.path.join('imagenes', 'check_ok.png'))
        icono = pygame.transform.scale(icono, (100, 100))
        self.pantalla.blit(icono, self.campo.topright)
        pygame.display.update()

    def botones(self, pantalla):
        """ Renderizado de los botones de la secciones """

        mis_clips = pygame.draw.rect(self.pantalla, self.COLOR_FONDO_MENU,
                                     (pantalla.centerx - 200,
                                      pantalla.centery - 150,
                                      400, 100))
        jugar = pygame.draw.rect(self.pantalla, self.COLOR_FONDO_MENU,
                                 (pantalla.centerx - 200,
                                  pantalla.centery + 50,
                                  400, 100))

        texto_clips = self.font_72.render('CLIPS', True, self.BLANCO)
        texto_jugar = self.font_72.render('JUGAR JUEGO', True, self.BLANCO)

        self.pantalla.blit(texto_clips,
                           self.tools.centrar(mis_clips, texto_clips))
        self.pantalla.blit(texto_jugar, self.tools.centrar(jugar, texto_jugar))

        texto_boton = ['ARMAR CLIP', 'CARGAR CLIP', 'JUGAR JUEGO']

        self.clicks['clips'] = (mis_clips, self.font_72)
        self.clicks['jugar juego'] = (jugar, self.font_72)

    def chequear_botones(self, pos_mouse):
        return self.tools.consulta_botones(pos_mouse, self.clicks)
