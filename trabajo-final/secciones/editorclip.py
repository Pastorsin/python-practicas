import pygame
import json
import os
from herramientas.Utilidades import Tools


class EditorClip():
    """Permite modificar un clip ya realizado"""

    def __init__(self, pantalla, ancho, alto, usuario, clip_elegido):
        # ..
        self.pantalla = pantalla
        self.ANCHO = ancho
        self.ALTO = alto
        self.usuario = usuario
        self.clip_elegido = clip_elegido
        # Control de las imagenes
        self.pos_img = 0
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
        self.font_100 = pygame.font.SysFont('Bank Gothic', 100)
        self.font_45 = pygame.font.SysFont('Bank Gothic', 45)
        self.font_30 = pygame.font.SysFont('Bank Gothic', 30)
        self.font_20 = pygame.font.SysFont('Bank Gothic', 20)
        # Herramientas
        self.tools = Tools(self.pantalla)
        self.cargar_datos_usuario()
        self.interfaz()

    def cargar_datos_usuario(self):
        """Carga la información del clip elegido por el usuario mediante el JSON"""
        arch = open(os.path.join(
            os.getcwd(), 'archivos', 'usuarios.json'), 'r')
        self.datos = json.load(arch)
        self.clip = self.datos[self.usuario][self.clip_elegido]
        arch.close()

    def grilla(self):
        """Tagea los rectángulos en el diccionario de clicks"""
        tamanio = (800 // 3, 280)
        y = self.caja_principal.top + 10
        for i in range(3):
            x = self.caja_principal.left + i * tamanio[0] + 5
            rectangulo = pygame.draw.rect(
                self.pantalla, self.DEEP_CARMINE, (x, y) + (tamanio[0] - 10, tamanio[1]))
            self.clicks[str(i)] = (rectangulo, 0)

    def actualizar_imagenes(self):
        tamanio = (800 // 3, 280)
        lista_img = self.clip['imagenes']
        y = self.caja_principal.top + 10
        # Muestro las imagenes en los 3 rect de la grilla
        for i in range(3):
            x = self.caja_principal.left + i * tamanio[0] + 5
            # Si está en el rango de las imagenes, la cargo y la muestro
            if (self.pos_img < len(lista_img)):
                img = pygame.image.load(lista_img[self.pos_img]['directorio'])
                img = pygame.transform.scale(
                    img, (tamanio[0] - 10, tamanio[1]))
                self.pantalla.blit(img, (x, y))
            else:
                # Muestra un rectángulo si no hay imágenes disponibles
                rectangulo = pygame.draw.rect(
                    self.pantalla, self.DEEP_CARMINE, (x, y) + (tamanio[0] - 10, tamanio[1]))
            self.pos_img += 1

    def interfaz(self):
        # Cajas
        titulo = pygame.draw.rect(self.pantalla, self.ROJO,
                                  (self.pantalla.get_rect().midtop[0] - 300,
                                   self.pantalla.get_rect().midtop[1] + 50,
                                   600, 80))
        finalizar = pygame.draw.rect(self.pantalla, self.VERDE,
                                     (self.ANCHO - 100, self.ALTO - 50) +
                                     (100, 50))
        self.caja_principal = pygame.draw.rect(
            self.pantalla, self.BLANCO,
            (self.pantalla.get_rect().centerx - 800 / 2,
             self.pantalla.get_rect().centery - 350 / 2, 800, 300))
        # Flechas
        self.f_izq = pygame.draw.rect(self.pantalla, self.ROJO_CLARITO, (
            self.caja_principal.left - 50, self.caja_principal.centery - 70 / 2, 50, 70))
        self.f_der = pygame.draw.rect(self.pantalla, self.ROJO_CLARITO, (
            self.caja_principal.right, self.caja_principal.centery - 70 / 2, 50, 70))
        # Texto
        self.tools.sombrear('«', self.BLANCO, self.NEGRO,
                            self.font_100, self.f_izq)
        self.tools.sombrear('»', self.BLANCO, self.NEGRO,
                            self.font_100, self.f_der)
        self.tools.sombrear('Editor de clip', self.BLANCO, self.NEGRO,
                            self.font_100, titulo)
        self.tools.sombrear('Finalizar', self.BLANCO, self.OXFORD_BLUE,
                            self.font_30, finalizar)
        # Clicks
        self.clicks = {
            'izq': (self.f_izq, 0),
            'der': (self.f_der, 0),
            'finalizar': (finalizar, 0)
        }
        # Grilla
        self.grilla()
        # Imagenes
        self.actualizar_imagenes()
# Funcionalidades

    def aumentar_imagenes(self):
        lista_img = self.clip['imagenes']
        if (self.pos_img < len(lista_img)):
            self.actualizar_imagenes()

    def decrementar_imagenes(self):
        lista_img = self.clip['imagenes']
        if (self.pos_img - 6 >= 0):
            self.pos_img -= 6
            self.actualizar_imagenes()

    def chequear_botones(self, mouse):
        return self.tools.consulta_botones(mouse, self.clicks)
