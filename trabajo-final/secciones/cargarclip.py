import pygame
import os
import json
from datetime import datetime
from herramientas.Utilidades import Tools


class CargarClip():
    """Sección que se encarga de abrir los clips almacenados del usuario"""

    def __init__(self, pantalla, ancho, alto, usuario):
        # Valores por defecto
        self.pantalla = pantalla
        self.ALTO = alto
        self.ANCHO = ancho
        # Usuario
        self.usuario = usuario
        self.pos_clip = 0
        self.clips = []
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
        self.ROJO_CLARITO = (255, 153, 153)
        # Fuentes
        self.font_72 = pygame.font.SysFont('Bank Gothic', 72)
        self.font_50 = pygame.font.SysFont('Bank Gothic', 50)
        self.font_30 = pygame.font.SysFont('Bank Gothic', 30)
        self.font_20 = pygame.font.SysFont('Rachana', 15)
        self.font_10 = pygame.font.SysFont('Bank Gothic', 10)

        # herramientas
        self.tools = Tools(self.pantalla)
        self.clicks = {}
        self.iniciar_carga()

    def iniciar_carga(self):
        self.interfaz()
        self.cargar_clips_usuario()
        self.grilla()

    def grilla(self):
        """Grilla en donde aparecen todos los clips disponibles.
        Arma los clicks con clave: rx o ex, siendo x el numero de posición del clip en la grilla"""
        alto = 625 // 10
        color = ((204, 0, 102), (128, 0, 0))
        x = self.caja_principal.left
        y = self.caja_principal.top
        y2 = self.caja_principal.top + alto / 2 + 4 / 2
        y3 = self.caja_principal.top + 4 / 2
        for i in range(len(self.clips[:10])):
            coord = (x, y + i * alto, 724, alto)
            # Rectangulos
            rectangulo = pygame.draw.rect(self.pantalla, color[i % 2], coord)
            rect_r = pygame.draw.rect(
                self.pantalla, self.GRIS, (x + 4, y3 + i * alto, 80, alto / 2 - 4))
            rect_e = pygame.draw.rect(
                self.pantalla, (26, 26, 26), (x + 4, y2 + i * alto, 80, alto / 2 - 4))

            # Agrego a los rectángulos a los clicks
            self.clicks['r' + str(i)] = (rect_r, 0)
            self.clicks['e' + str(i)] = (rect_e, 0)
            # Hora de ultima modificación
            texto_fecha = self.font_20.render(
                'Última modificación: ' + self.clips[i]['fecha'], True, self.ROJO_CLARITO)
            # Nombre del clip
            texto = self.font_50.render(
                self.clips[i]['clip'], True, self.BLANCO)
            # Textos
            self.tools.sombrear('EDITAR', self.GRIS,
                                self.OXFORD_BLUE, self.font_20, rect_e)
            self.tools.sombrear('REPRODUCIR', (26, 26, 26),
                                self.GRIS, self.font_20, rect_r)
            # Render
            self.pantalla.blit(texto, self.tools.centrar(rectangulo, texto))
            self.pantalla.blit(texto_fecha,
                               (rectangulo.right - texto_fecha.get_rect().width - 3, rectangulo.bottom - texto_fecha.get_rect().height))

    def interfaz(self):
        """ Vista del cargar clip """
        # Cajas
        self.caja_principal = pygame.draw.rect(
            self.pantalla, self.BLANCO, (self.ANCHO / 2 - 724 / 2, self.ALTO / 2 - 580 / 2, 724, 620))
        self.caja_misclips = pygame.draw.rect(
            self.pantalla, self.ROJO, (self.ANCHO / 2 - 500 / 2, 0, 500, 50))
        img_agregar = pygame.image.load(os.path.join('imagenes',
                                                     'agregar.png'))
        # Botones
        aux = self.pantalla.get_rect()
        self.rect_agregar = img_agregar.get_rect().move(
            aux.bottomright[0] - 70,
            aux.bottomright[1] - 70)
        self.pantalla.blit(img_agregar, (aux.bottomright[0] - 70,
                                         aux.bottomright[1] - 70))
        self.atras = pygame.draw.rect(self.pantalla, self.DEEP_CARMINE,
                                      (0, self.pantalla.get_rect().height - 30, 80, 30))
        # Texto
        self.tools.sombrear('Atrás', self.BLANCO,
                            self.OXFORD_BLUE, self.font_30, self.atras)
        self.tools.sombrear('MIS CLIPS', self.BLANCO,
                            self.OXFORD_BLUE, self.font_72, self.caja_misclips)
        # Clicks
        self.clicks['armar clip'] = (self.rect_agregar, 0)
        self.clicks['atras'] = (self.atras, 0)

    def cargar_clips_usuario(self):
        """ obtiene los clips guardados del usuario """
        arch = open(os.path.join(
            os.getcwd(), 'archivos', 'usuarios.json'), 'r')
        datos = json.load(arch)
        if self.usuario in datos.keys():
            self.clips = datos[self.usuario]
        else:  # Si el usuario no posee clips guardados, lanza un cartel de error
            self.tools.sombrear('No hiciste ningún clip todavía. Hace uno!',
                                self.NEGRO, self.ROJO_CLARITO, self.font_50,
                                self.caja_principal)

    def chequear_botones(self, mouse):
        return self.tools.consulta_botones(mouse, self.clicks)
