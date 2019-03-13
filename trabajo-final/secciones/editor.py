import pygame
import os
import time
import math
from herramientas.Utilidades import Tools


class Editor():
    """Editor de imagenes"""

    def __init__(self, pantalla, ancho, alto, usuario):
        """ Inicializa los valores predeterminados de la clase"""

    # Pantalla
        self.pantalla = pantalla
        self.ANCHO = ancho
        self.ALTO = alto
    # Usuario
        self.usuario = usuario
        self.duracion = 1
        self.cont_grosor = 1
        self.cont_tamaño = 1
        self.cont_color = 0
        self.cont_estilo = 0
        self.cont_color_fondo = 0
        self.cont_filtro = 0
        self.color_actual = (51, 0, 26)
        self.color_fondo_actual = (45, 23, 56)
        self.sonido = ''
        self.dir_img = ''
    # Colores
        self.VERDE = (79, 170, 90)
        self.BORDO = (102, 0, 51)
        self.VIOLETA = (51, 0, 26)
        self.BLANCO = (255, 255, 255)
        self.ROJO = (244, 36, 40)
        self.NEGRO = (0, 0, 0)
        self.ROJO_CLARITO = (255, 153, 153)
        self.DARK_PURPLE = (45, 23, 56)
        self.OXFORD_BLUE = (3, 15, 69)
        self.DEEP_CARMINE = (170, 40, 57)
        self.CELESTE_LINDO = (40, 152, 178)
        self.TIGERS_EYE = (224, 159, 62)
        self.GRIS = (194, 214, 214)
    # herramientas
        self.tools = Tools(self.pantalla)
    # Fuentes
        Josefin_Sans = os.path.join('fuentes', 'Josefin_Sans',
                                    'JosefinSans-Regular.ttf')
        Open_Sans = os.path.join('fuentes', 'Open_Sans',
                                 'OpenSans-Regular.ttf')
        Shrikhand = os.path.join('fuentes', 'Shrikhand',
                                 'Shrikhand-Regular.ttf')
        Wendy_One = os.path.join('fuentes', 'Wendy_One',
                                 'WendyOne-Regular.ttf')
        self.estilos = [Josefin_Sans, Open_Sans, Shrikhand, Wendy_One]
        self.tamaños = [15, 20, 30, 45, 60]
        self.estilo_actual = self.estilos[1]

        self.font_60 = pygame.font.Font(self.estilos[1], self.tamaños[4])
        self.font_45 = pygame.font.Font(self.estilos[1], self.tamaños[3])
        self.font_30 = pygame.font.Font(self.estilos[1], self.tamaños[2])
        self.font_20 = pygame.font.Font(self.estilos[1], self.tamaños[1])
        self.font_15 = pygame.font.Font(self.estilos[1], self.tamaños[0])

    def iniciar_editor(self, directorio):
        self.imagen = pygame.image.load(directorio)
        self.interfaz()

    def interfaz(self):
        """ Se encarga de cargar los elementos y botones en la pantalla"""
    # Cajas
        self.caja_principal = pygame.draw.rect(self.pantalla, self.BORDO,
                                               (self.ANCHO / 2 - 750 / 2,
                                                0, 750, 720))
        self.caja_lateral_izq = pygame.draw.rect(self.pantalla, self.VIOLETA,
                                                 (0, 0,
                                                  (1024 - 750) / 2, 720))
        self.caja_lateral_der = pygame.draw.rect(self.pantalla, self.VIOLETA,
                                                 (self.caja_principal.right, 0,
                                                  (1024 - 750) / 2, 720))
        self.caja_duracion_total = pygame.draw.rect(
            self.pantalla, self.VIOLETA, (self.pantalla.get_width() / 2 - 200,
                                          self.pantalla.get_height() - 40,
                                          400, 40))

    # Imagenes
        self.imagen = pygame.transform.scale(self.imagen, (724, 620))
        self.salir = pygame.image.load(os.path.join('imagenes', 'close.png'))
        self.agregar = pygame.image.load(os.path.join('imagenes', 'clip.png'))

    # Botones
        self.actualizar_caja_duracion()
        self.inc_duracion = pygame.draw.rect(
            self.pantalla, self.VERDE, (self.pantalla.get_width() / 2,
                                        self.pantalla.get_rect().bottom - 35,
                                        10, 15))
        self.dec_duracion = pygame.draw.rect(
            self.pantalla, self.ROJO, (self.pantalla.get_width() / 2,
                                       self.pantalla.get_rect().bottom - 20,
                                       10, 15))
        self.caja_sonido = pygame.draw.rect(
            self.pantalla, self.VIOLETA, (self.pantalla.get_width() / 2 - 200, 0,
                                          400, 40))
        self.caja_formas = pygame.draw.rect(
            self.pantalla, self.DARK_PURPLE,
            ((self.caja_lateral_der.topright[0] - 110,
              self.caja_lateral_der.topright[1] + 50) +
             (110, 500)))

    # Formas
        self.cuadrado_relleno = pygame.draw.rect(
            self.pantalla, self.NEGRO,
            (self.caja_formas.topleft[0] + 30,
             self.caja_formas.topleft[1] + 20) +
            (50, 50))
        self.cuadrado_vacio = pygame.draw.rect(
            self.pantalla, self.NEGRO,
            (self.cuadrado_relleno.bottomleft[0],
             self.cuadrado_relleno.bottomleft[1] + 20) +
            (50, 50), 3)
        self.linea = pygame.draw.line(
            self.pantalla, self.NEGRO,
            (self.cuadrado_vacio.bottomleft[0],
             self.cuadrado_vacio.bottomleft[1] + 60),
            (self.cuadrado_vacio.bottomright[0],
             self.cuadrado_vacio.bottomright[1] + 30),
            4)
        self.circulo_relleno = pygame.draw.circle(
            self.pantalla, self.NEGRO,
            (self.linea.bottomleft[0] + 25,
             self.linea.bottomleft[1] + 50),
            30)
        self.circulo_vacio = pygame.draw.circle(
            self.pantalla, self.NEGRO,
            (self.circulo_relleno.bottomleft[0] + 30,
             self.circulo_relleno.bottomleft[1] + 40),
            30, 4)

    # Opciones
        self.color = pygame.draw.rect(self.pantalla, self.color_actual,
                                      (self.caja_formas.bottomleft[0] + 10,
                                       self.caja_formas.bottomleft[1] - 100) +
                                      (90, 30))
        self.grosor = pygame.draw.rect(self.pantalla, self.VIOLETA,
                                       (self.caja_formas.bottomleft[0] + 10,
                                        self.caja_formas.bottomleft[1] - 60) +
                                       (90, 30))
        self.inc_grosor = pygame.draw.rect(
            self.pantalla, self.VERDE, ((self.grosor.topright[0] - 10,
                                         self.grosor.topright[1]) + (10, 15)))
        self.dec_grosor = pygame.draw.rect(
            self.pantalla, self.ROJO, ((self.grosor.topright[0] - 10,
                                        self.grosor.topright[1] + 15) +
                                       (10, 15)))
        self.actualizar_caja_grosor()

    # Escritura
        self.boton_texto = pygame.draw.rect(
            self.pantalla, self.NEGRO, (self.caja_lateral_izq.topleft[0] + 30,
                                        self.caja_lateral_izq.topleft[1] + 125,
                                        80, 100))
        self.color_fondo = pygame.draw.rect(
            self.pantalla, self.color_fondo_actual,
            (self.boton_texto.bottomleft[0] - 10,
             self.boton_texto.bottomleft[1] + 30,
             100, 30))
        self.tipografia = pygame.draw.rect(
            self.pantalla, self.DARK_PURPLE, (self.color_fondo.bottomleft[0],
                                              self.color_fondo.bottomleft[
                                                  1] + 10,
                                              100, 30))
        self.tamaño = pygame.draw.rect(self.pantalla, self.DARK_PURPLE,
                                       (self.tipografia.bottomleft[0],
                                        self.tipografia.bottomleft[1] + 10) +
                                       (70, 30))
        self.inc_tamaño = pygame.draw.rect(
            self.pantalla, self.VERDE, ((self.tipografia.bottomright[0] - 10,
                                         self.tipografia.bottomright[1] + 10) +
                                        (10, 15)))
        self.dec_tamaño = pygame.draw.rect(
            self.pantalla, self.ROJO, ((self.tipografia.bottomright[0] - 10,
                                        self.tipografia.bottomright[1] + 25) +
                                       (10, 15)))
        self.actualizar_caja_tamaño()
        self.filtro = pygame.draw.circle(
            self.pantalla, self.NEGRO, (self.tipografia.bottomleft[0] + 50,
                                        self.tipografia.bottomleft[1] + 200), 50)

    # Texto
        self.texto_duracion = self.font_20.render(
            'DURACIÓN:', True, self.BLANCO)
        self.texto_sonido = self.font_30.render(
            'AGREGAR SONIDO', True, self.BLANCO)
        self.texto_segundos = self.font_15.render(
            'Segundos', True, self.BLANCO)
        self.texto_color = self.font_15.render(
            'Color', True, self.GRIS)
        self.texto_grosor = self.font_15.render(
            'Grosor', True, self.BLANCO)
        self.flecha_arriba = self.font_15.render(
            '+', True, self.NEGRO)
        self.flecha_abajo = self.font_15.render(
            '-', True, self.NEGRO)
        self.texto_escritura = self.font_20.render(
            'TEXTO', True, self.BORDO)
        self.texto_fondo = self.font_15.render(
            'Color Fondo', True, self.BLANCO)
        self.texto_tipografia = pygame.font.Font(self.estilo_actual,
                                                 self.tamaños[0]).render(
            'Tipografía', True, self.BLANCO)
        self.texto_tamaño = self.font_15.render(
            'Tamaño', True, self.BLANCO)
        self.texto_filtro = self.font_20.render(
            'FILTRO', True, self.BORDO)

    # Renders
        self.inferior = (self.pantalla.get_width() - self.agregar.get_width(),
                         self.caja_principal.height - self.agregar.get_height()
                         )
        # botones imagen, agregar y cancelar
        self.pantalla.blit(
            self.imagen, self.tools.centrar(self.caja_principal, self.imagen))
        self.pantalla.blit(self.agregar, self.inferior)
        self.pantalla.blit(self.salir, (2, 2))
        # duracion
        self.pantalla.blit(
            self.texto_duracion, (self.inc_duracion.left - 160,
                                  self.pantalla.get_height() - 30))
        self.pantalla.blit(
            self.texto_segundos, (self.inc_duracion.left + 20,
                                  self.pantalla.get_height() - 28))
        self.pantalla.blit(
            self.flecha_arriba, self.tools.centrar(self.inc_duracion,
                                                   self.flecha_arriba))
        self.pantalla.blit(
            self.flecha_abajo, self.tools.centrar(self.dec_duracion,
                                                  self.flecha_abajo))
        # sonido
        self.pantalla.blit(
            self.texto_sonido, (self.pantalla.get_width() / 2 -
                                self.texto_sonido.get_width() / 2, 5))
        # formas
        self.pantalla.blit(
            self.texto_color, self.tools.centrar(self.color,
                                                 self.texto_color))
        self.pantalla.blit(
            self.texto_grosor, (self.grosor.topleft[0] + 7,
                                self.grosor.topleft[1] + 7))
        self.pantalla.blit(
            self.flecha_arriba, self.tools.centrar(self.inc_grosor,
                                                   self.flecha_arriba))
        self.pantalla.blit(
            self.flecha_abajo, self.tools.centrar(self.dec_grosor,
                                                  self.flecha_abajo))
        # escritura
        self.pantalla.blit(
            self.texto_escritura, self.tools.centrar(self.boton_texto,
                                                     self.texto_escritura))
        self.pantalla.blit(
            self.texto_fondo, self.tools.centrar(self.color_fondo,
                                                 self.texto_fondo))
        self.pantalla.blit(
            self.texto_tipografia, self.tools.centrar(self.tipografia,
                                                      self.texto_tipografia))
        self.pantalla.blit(
            self.texto_tamaño, self.tools.centrar(self.tamaño,
                                                  self.texto_tamaño))
        self.pantalla.blit(
            self.flecha_arriba, self.tools.centrar(self.inc_tamaño,
                                                   self.flecha_arriba))
        self.pantalla.blit(
            self.flecha_abajo, self.tools.centrar(self.dec_tamaño,
                                                  self.flecha_abajo))
        self.pantalla.blit(
            self.texto_filtro, self.tools.centrar(self.filtro,
                                                  self.texto_filtro))

    # Respaldo para el deshacer y los filtros
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '1.jpg')

    # Clicks
        self.clicks = {
            'salir': (self.salir.get_rect().move(2, 2), 0),
            'agregar': (self.agregar.get_rect().move(self.inferior), 0),
            'incrementar': (self.inc_duracion, 0),
            'decrementar': (self.dec_duracion, 0),
            'sonido': (self.caja_sonido, 0),

            'cuadrado_R': (self.cuadrado_relleno, 0),
            'cuadrado_V': (self.cuadrado_vacio, 0),
            'linea': (self.linea, 0),
            'circulo_R': (self.circulo_relleno, 0),
            'circulo_V': (self.circulo_vacio, 0),
            'color': (self.color, 0),
            'inc_grosor': (self.inc_grosor, 0),
            'dec_grosor': (self.dec_grosor, 0),

            'texto': (self.boton_texto, 0),
            'color_fondo': (self.color_fondo, 0),
            'tipografia': (self.tipografia, 0),
            'tamaño': (self.tamaño, 0),
            'inc_tamaño': (self.inc_tamaño, 0),
            'dec_tamaño': (self.dec_tamaño, 0),
            'filtro': (self.filtro, 0)
        }

# Cuadrados
    def crear_cuadrado(self, relleno=False):
        """ Dibuja un cuadrado en pantalla """
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        cuadrado = self.tools.obtener_pos_tam(pygame.Rect(150, 50, 724, 625))
        if relleno:
            grosor = self.cont_grosor
        else:
            grosor = 0
        pygame.draw.rect(
            self.pantalla, self.color_actual, cuadrado, grosor)
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '1.jpg')

# Lineas
    def crear_linea(self):
        """ Dibuja una linea en pantalla """
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        pos1 = self.tools.obtener_posicion_click(pygame.Rect(150, 50, 724, 625))
        pos2 = self.tools.obtener_posicion_click(pygame.Rect(150, 50, 724, 625))
        pygame.draw.line(
            self.pantalla, self.color_actual, pos1, pos2, self.cont_grosor)
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '1.jpg')

# Circulos
    def crear_circulo(self, relleno=False):
        """ Dibuja un circulo en pantalla """
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        pos1 = self.tools.obtener_posicion_click(pygame.Rect(150, 50, 724, 625))
        pos2 = self.tools.obtener_posicion_click(pygame.Rect(150, 50, 724, 625))
        radio = int(
            (math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)) // 2)
        medio = (pos2[0] - (pos2[0] - pos1[0]) // 2,
                 pos2[1] - (pos2[1] - pos1[1]) // 2)
        if relleno:
            grosor = self.cont_grosor
        else:
            grosor = 0
        pygame.draw.circle(
            self.pantalla, self.color_actual, medio, radio, grosor)
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '1.jpg')

# Color
    def cambiar_color(self):
        """ Cambia el color de las formas y el texto """
        lista_colores = [self.VERDE, self.BORDO, self.ROJO, self.NEGRO,
                         self.BLANCO, self.ROJO_CLARITO, self.OXFORD_BLUE,
                         self.DEEP_CARMINE, self.CELESTE_LINDO,
                         self.TIGERS_EYE, self.VIOLETA]
        self.color_actual = lista_colores[self.cont_color]
        self.cont_color += 1
        if self.cont_color == 11:
            self.cont_color = 0
        # cambio al color indicado al boton de color
        self.color = pygame.draw.rect(self.pantalla, self.color_actual,
                                      (self.caja_formas.bottomleft[0] + 10,
                                       self.caja_formas.bottomleft[1] - 100) +
                                      (90, 30))
        self.pantalla.blit(
            self.texto_color, self.tools.centrar(self.color, self.texto_color))

# Texto
    def insertar_texto(self):
        """ Maneja la insercion del texto en la imagen """
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        self.pos = self.tools.obtener_posicion_click(pygame.Rect(150, 50, 724, 625))
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        self.texto = ''
        self.renderizar_texto_escribir()

    def borrar(self):
        self.texto = self.texto[:-1]

    def dentro_limite(self, texto):
        """ Verifica si el texto no superó el limite
            de la caja que lo contiene """
        rect_imagen = self.imagen.get_rect()
        F = pygame.font.Font(self.estilo_actual,
                             self.tamaños[self.cont_tamaño])
        rect_texto = F.render(texto, True, self.BLANCO)
        return rect_texto.get_width() < (875 - self.pos[0])

    def actualizar_texto(self, caracter):
        self.texto += caracter

    def renderizar_texto_escribir(self):
        """
        Muestra el texto en la pantalla.
        Retorna si el límite fue o no superado.
        """
        if (self.dentro_limite(self.texto)):
            # Limpio pantalla
            respaldo = os.path.join('imagenes', 'respaldo', '0.jpg')
            self.iniciar_editor(respaldo)
            # Renderiza el texto
            F = pygame.font.Font(self.estilo_actual,
                                 self.tamaños[self.cont_tamaño])
            if self.color_fondo_actual != self.DARK_PURPLE:  # Dark purple lo deja invisible
                render = F.render(self.texto, True, self.color_actual)
                render.fill(self.color_fondo_actual)
                self.pantalla.blit(render, self.pos)
            render = F.render(self.texto, True, self.color_actual)
            self.pantalla.blit(render, self.pos)
            self.tools.guardar_cambio(self.imagen, self.caja_principal, '1.jpg')
            return False
        else:
            return True

# Color Fondo
    def cambiar_color_fondo(self):
        """ Cambia el color de fondo del texto que se escribe """
        lista_colores = [self.VERDE, self.BORDO, self.ROJO, self.NEGRO,
                         self.BLANCO, self.ROJO_CLARITO, self.OXFORD_BLUE,
                         self.DEEP_CARMINE, self.VIOLETA, self.CELESTE_LINDO,
                         self.TIGERS_EYE, self.DARK_PURPLE]
        self.color_fondo_actual = lista_colores[self.cont_color_fondo]
        self.cont_color_fondo += 1
        if self.cont_color_fondo == 12:
            self.cont_color_fondo = 0
        # cambio al color indicado al boton de color de fondo
        self.color_fondo = pygame.draw.rect(
            self.pantalla, self.color_fondo_actual,
            (self.boton_texto.bottomleft[0] - 10,
             self.boton_texto.bottomleft[1] + 30,
             100, 30))
        self.pantalla.blit(
            self.texto_fondo, self.tools.centrar(self.color_fondo,
                                                 self.texto_fondo))

# Estilo

    def cambiar_estilo(self):
        """ Cambia el estilo de la fuente del texto """
        self.estilo_actual = self.estilos[self.cont_estilo]
        self.cont_estilo += 1
        if self.cont_estilo == 4:
            self.cont_estilo = 0
        # cambio el estilo indicado al boton de tipografia
        self.tipografia = pygame.draw.rect(
            self.pantalla, self.DARK_PURPLE, (self.color_fondo.bottomleft[0],
                                              self.color_fondo.bottomleft[
                                                  1] + 10,
                                              100, 30))
        F = pygame.font.Font(self.estilo_actual, self.tamaños[0])
        texto = F.render('Tipografía', True, self.BLANCO)
        self.pantalla.blit(texto, self.tools.centrar(self.tipografia, texto))

# Filtro

    def cambiar_filtro(self):
        """ Le aplica un filtro a la imagen """
        lista_colores = [self.VERDE, self.BORDO, self.ROJO, self.NEGRO,
                         self.ROJO_CLARITO, self.OXFORD_BLUE,
                         self.DEEP_CARMINE, self.CELESTE_LINDO,
                         self.TIGERS_EYE, self.VIOLETA, self.DARK_PURPLE]
        color_actual_filtro = (lista_colores[self.cont_filtro][0],
                               lista_colores[self.cont_filtro][1],
                               lista_colores[self.cont_filtro][2], 100)
        self.cont_filtro += 1
        if self.cont_filtro == 11:
            self.cont_filtro = 0
        # Limpio
        respaldo = os.path.join('imagenes', 'respaldo', '1.jpg')
        self.iniciar_editor(respaldo)
        # Pongo el filtro
        superficie = self.imagen.convert_alpha()
        superficie.fill(color_actual_filtro)
        self.pantalla.blit(superficie, self.tools.centrar(self.caja_principal,
                                                          superficie))

# Contador grosor

    def actualizar_caja_grosor(self):
        """ Indicador grafico del grosor aplicado a las formas """
        caja_grosor = pygame.draw.rect(
            self.pantalla, self.BLANCO, (self.inc_grosor.topleft[0] - 20,
                                         self.inc_grosor.topleft[1],
                                         20, 30))
        numero = self.font_20.render(str(self.cont_grosor), True, self.NEGRO)
        self.pantalla.blit(numero, self.tools.centrar(caja_grosor,
                                                      numero))

    def incrementar_grosor(self):
        if self.cont_grosor < 10:
            self.cont_grosor += 1
        self.actualizar_caja_grosor()

    def decrementar_grosor(self):
        if self.cont_grosor != 1:
            self.cont_grosor -= 1
        self.actualizar_caja_grosor()

# Contador duracion

    def actualizar_caja_duracion(self):
        """ Indicador grafico de la duracion que se le aplicara a la imagen """
        self.caja_duracion = pygame.draw.rect(
            self.pantalla, self.BLANCO, (self.pantalla.get_width() / 2 - 30,
                                         self.pantalla.get_rect().bottom - 35,
                                         30, 30))
        numero = self.font_20.render(str(self.duracion), True, self.NEGRO)
        self.pantalla.blit(numero, self.tools.centrar(self.caja_duracion,
                                                      numero))

    def incrementar_duracion(self):
        if self.duracion < 99:
            self.duracion += 1
        self.actualizar_caja_duracion()

    def decrementar_duracion(self):
        if self.duracion != 1:
            self.duracion -= 1
        self.actualizar_caja_duracion()

# Contador tamaño

    def actualizar_caja_tamaño(self):
        """ Indicador grafico del tamaño que se le aplicará a la fuente """
        caja_tamaño = pygame.draw.rect(
            self.pantalla, self.BLANCO, (self.inc_tamaño.topleft[0] - 20,
                                         self.inc_tamaño.topleft[1],
                                         20, 30))
        numero = self.font_20.render(str(self.cont_tamaño), True, self.NEGRO)
        self.pantalla.blit(numero, self.tools.centrar(caja_tamaño, numero))

    def incrementar_tamaño(self):
        if self.cont_tamaño < 4:
            self.cont_tamaño += 1
        self.actualizar_caja_tamaño()

    def decrementar_tamaño(self):
        if self.cont_tamaño != 1:
            self.cont_tamaño -= 1
        self.actualizar_caja_tamaño()

# Extras

    def chequear_botones(self, mouse):
        return self.tools.consulta_botones(mouse, self.clicks)

    def agregar_clip(self, directorio_clip):
        """ Guarda la imagen editada """
        self.imagen_editada = self.pantalla.subsurface(
            self.imagen.get_rect().move(self.tools.centrar(self.caja_principal,
                                                           self.imagen)))
        pygame.image.save(self.imagen_editada, directorio_clip)

    def agregar_sonido(self):
        self.tools.guardar_cambio(self.imagen, self.caja_principal, '0.jpg')
        # Hago la grilla
        self.grilla_sonidos()

    def grilla_sonidos(self):
        """ Despliega la grilla de sonidos elegibles para la imagen """
        color = ((204, 0, 102), (128, 0, 0))
        sonidos = os.listdir(os.path.join('audio', 'sonidos'))
        x = self.tools.centrar(self.caja_principal, self.imagen)[0]
        y = self.tools.centrar(self.caja_principal, self.imagen)[1]
        alto = 625 // 6
        for i in range(6):
            coord = (x, y + i * alto, 724, alto)
            rectangulo = pygame.draw.rect(self.pantalla, color[i % 2], coord)
            # Agrego a los rectángulos a los clicks
            self.clicks[str(i)] = (rectangulo, 0)
            texto = self.font_45.render(
                os.path.splitext(sonidos[i])[0], True, self.BLANCO)
            self.pantalla.blit(texto, self.tools.centrar(rectangulo, texto))

    def sonido_elegido(self, pos):
        # Guarda el directorio del sonido
        directorio = os.path.join('audio', 'sonidos')
        sonidos = os.listdir(directorio)
        self.sonido = os.path.join(directorio, sonidos[pos])
        # Muestra al usuario el sonido elegido
        s = pygame.mixer.Sound(self.sonido)
        s.play()
        time.sleep(1)
