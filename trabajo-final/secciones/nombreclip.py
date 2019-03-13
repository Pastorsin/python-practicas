import pygame
import time
import os
from herramientas.Utilidades import Tools


class NombreClip:
    """ Se encarga de procesar el nombre del clip"""

    def __init__(self, pantalla, ancho, alto, usuario):
        # Valores por defecto
        self.usuario = usuario
        self.nombre_clip = ''
        self.ALTO = alto
        self.ANCHO = ancho
        self.pantalla = pantalla
        self.tools = Tools(self.pantalla)
        # Colores
        self.COLOR_FONDO_MENU = (179, 0, 0)
        self.ROJO = (244, 36, 40)
        self.BLANCO = (255, 230, 230)
        self.GRIS = (194, 214, 214)
        self.NEGRO = (0, 0, 0)
        self.OXFORD_BLUE = (3, 15, 69)
        self.KENYAN_COPPER = (117, 19, 4)
        self.BLUE_YONDER = (77, 126, 168)
        self.VANILLA = (242, 243, 174)
        self.ROJO_CLARITO = (255, 153, 153)
        self.COLOR_TITULO = (102, 0, 51)
        # Fuentes
        self.font_72 = pygame.font.SysFont('monaco', 65)
        self.font_45 = pygame.font.SysFont('Bank Gothic', 45)
        self.font_30 = pygame.font.SysFont('Bank Gothic', 30)
        self.interfaz(self.pantalla.get_rect())

    def interfaz(self, pantalla):
        """ Pone la interfaz del nombre del clip """
        pos_titulo = (pantalla.center[0] - 300, pantalla.center[1] - 200)
        self.titulo = pygame.draw.rect(self.pantalla, self.COLOR_TITULO,
                                       (0, pantalla.center[1] - 200) + (pantalla.width, 150))
        self.tools.sombrear('Ingrese el nombre del clip', self.ROJO_CLARITO, (0, 0, 0),
                            self.font_72, self.titulo)
        self.limpiar_campo()
        self.cancelar = pygame.image.load(os.path.join('imagenes', 'cancelar.png'))
        self.pantalla.blit(self.cancelar, (pantalla.width / 2 - 311/2, pantalla.bottom - 100))
        self.cancelar = self.cancelar.get_rect().move(pantalla.width / 2 - 311/2, pantalla.bottom - 100)

    def limpiar_campo(self):
        pos_campo = (self.pantalla.get_width() / 2 - 400, self.titulo.bottom)
        self.campo = pygame.draw.rect(self.pantalla, self.ROJO_CLARITO,
                                      pos_campo + (800, 100))

    def enter(self):
        """ Guarda el clip """
        if not self.nombre_clip:
            self.nombre_clip = 'sin nombre'
        directorios = os.listdir(os.path.join('archivos', self.usuario))
        if self.nombre_clip in directorios:
            self.nombre_clip = ''
            self.existe = True
        else:
            self.existe = False

    def avisar_existe(self):
        """ Indicador de que el clip existe  """
        img = pygame.image.load(os.path.join('imagenes', 'errorclip.png'))
        self.pantalla.blit(img, (self.campo.left + 50, self.campo.bottom + 20))
        self.interfaz(self.pantalla.get_rect())

    def avisar_correcto(self):
        """ Indicador de que el clip no existe """
        self.interfaz(self.pantalla.get_rect())
        img = pygame.image.load(os.path.join('imagenes', 'checkclip.png'))
        self.pantalla.blit(img, (self.campo.left + 50, self.campo.bottom + 20))
        pygame.display.update()
        time.sleep(1.5)

    def borrar(self):
        self.nombre_clip = self.nombre_clip[:-1]

    def actualizar_texto(self, caracter):
        self.nombre_clip += caracter

    def dentro_limite(self, texto):
        """ Verifica si el texto no superó el limite
            de la caja que lo contiene """
        return self.tools.centrar(self.campo, self.font_72.render(texto, True, self.GRIS))[0] - 20 > self.campo.left

    def renderizar_texto_buscar(self):
        """
        Muestra el texto en la pantalla.
        Retorna si el límite fue o no superado.
        """
        if (self.dentro_limite(self.nombre_clip)):
            # Limpio pantalla
            self.limpiar_campo()
            pygame.draw.line(self.pantalla, self.NEGRO,
                             (self.campo.bottomleft[0] + 20,
                              self.campo.bottomleft[1] - 10),
                             (self.campo.bottomright[0] - 20,
                              self.campo.bottomright[1] - 10),
                             3)
            # Renderiza el texto
            self.tools.sombrear(self.nombre_clip, self.NEGRO, self.ROJO,
                                self.font_72, self.campo)
            return False
        else:
            return True
