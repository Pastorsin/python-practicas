# -*- coding: utf-8 -*-

import pygame
import sys
import os
import json
import shutil
from datetime import datetime
from secciones.menu import *
from secciones.armarclip import *
from secciones.cargarclip import *
from secciones.jugarjuego import *
from secciones.editor import *
from secciones.nombreclip import *
from secciones.reproductor import *
from secciones.editorclip import *


class Aplicacion():
    """ Representa a la aplicación, se encarga de dirigir los eventos y
    controlar el loop del juego """

    def __init__(self):
        """Valores por defecto del juego"""
        # Configuración de pantalla
        self.TITULO = "PochoClips"
        self.ANCHO = 1024
        self.ALTO = 720
        self.RESOLUCION = (self.ANCHO, self.ALTO)

        # Corte del programa
        self.run = True

        # Diccionario que por clave nos indica en que sección del juego estamos
        self.estamos_en = {
            'menu': True,
            'armar clip': False,
            'cargar clip': False,
            'jugar juego': False,
            'editor': False,
            'nombre clip': False,
            'reproductor': False,
            'editor clip': False
        }
        self.seccion = {
            'menu': Menu,
            'armar clip': ArmarClip,
            'cargar clip': CargarClip,
            'jugar juego': JugarJuego,
            'editor': Editor,
            'nombre clip': NombreClip,
            'reproductor': Reproductor,
            'editor clip': EditorClip
        }

        self.entrada_de_texto = False

        # Para guardar imagenes
        self.directorio = ''
        self.ultimo_boton = ''
        self.ultima_seccion = ''
        self.posicion_clip = 0

        # Para cargar el clip
        self.clip_elegido = 0
        self.secuencia = False

        # Datos del usuario
        self.usuario = ''
        self.datos_usuario = {
            'clip': 'desconocido',
            'imagenes': [],
            'musica': {'ruta': '',
                       'loop': False},
            'fecha': ''
        }

    def fondo(self):
        """Implementación del fondo"""
        self.pantalla = pygame.display.set_mode(self.RESOLUCION)
        fondo = pygame.image.load(os.path.join('imagenes', 'fondo.jpg'))
        fondo = pygame.transform.scale(fondo, self.RESOLUCION)
        self.pantalla.blit(fondo, (0, 0))

    def inicializaciones(self):
        """Inicializaciones propias para el funcionamiento"""
        pygame.init()
        self.fondo()
        pygame.display.set_caption(self.TITULO)
        self.escena_actual = Menu(
            self.pantalla, self.ANCHO, self.ALTO, self.usuario)
        # inicio de sesion
        self.escena_actual.comenzar_escribir()
        self.entrada_de_texto = True
        self.limite = False

# Manejadores de eventos

# Menu
    def manejador_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            # Mostrar la sección
            if boton == 'clips':
                self.fondo()
                self.escena_actual = self.seccion['cargar clip'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario)
                self.estamos_en['menu'] = False
                self.entrada_de_texto = False
                self.estamos_en['cargar clip'] = True
            elif boton == 'jugar juego':
                self.escena_actual = self.seccion['jugar juego'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario)
                self.estamos_en['menu'] = False
                self.estamos_en['jugar juego'] = True
        if event.type == pygame.KEYDOWN:
            if self.entrada_de_texto:
                self.manejador_sesion(event)

    def manejador_sesion(self, event):
        """Se encarga del inicio de sesión"""
        if event.key == pygame.K_RETURN:  # Si apreta enter
            self.escena_actual.enter()
            self.usuario = self.escena_actual.usuario
            time.sleep(0.5)  # Para mostrar el okey
            self.entrada_de_texto = False
        elif event.key == pygame.K_BACKSPACE:  # Si borra
            self.escena_actual.borrar()
        elif not self.limite:  # Si ingresa cualquier tecla y no superó la caja
            self.escena_actual.actualizar_texto(event.unicode)
        if self.entrada_de_texto:
            self.limite = self.escena_actual.renderizar_texto_escrito()
        else:   # cuando deja de enfocar el campo
            # Saco la sesion y pongo los botones
            self.fondo()
            self.escena_actual.botones(self.pantalla.get_rect())

# Cargar clip

    def manejador_cargarclip(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            if boton == 'armar clip':
                if self.ultimo_boton == 'finalizar':
                    # Crea la carpeta donde se va a guardar el posible clip
                    clip_temp = os.path.join('archivos', self.usuario, 'temp')
                    if os.path.exists(clip_temp):
                        shutil.rmtree(clip_temp)
                    os.mkdir(clip_temp)
                    # Reinicia los datos del usuario
                    self.datos_usuario = {
                        'clip': 'desconocido',
                        'imagenes': [],
                        'musica': {'ruta': '',
                                   'loop': False},
                        'fecha': ''
                    }
                self.fondo()
                self.escena_actual = self.seccion[boton](self.pantalla,
                                                         self.ANCHO,
                                                         self.ALTO,
                                                         self.usuario)
                self.estamos_en['cargar clip'] = False
                self.estamos_en[boton] = True
            # Para que no se pierda el clip actual si el usuario va para atras
            elif boton == 'atras':
                # Limpio
                self.fondo()
                # Vuelve al menú
                self.escena_actual = self.seccion['menu'](self.pantalla,
                                                          self.ANCHO,
                                                          self.ALTO,
                                                          self.usuario)
                self.estamos_en['cargar clip'] = False
                self.estamos_en['menu'] = True
            # Si hay que reproducir
            elif boton and 'r' in boton:
                # Si elige un clip, va al reproductor y se guarda la posición
                # para luego cargarlo
                self.clip_elegido = int(boton[1])
                self.fondo()
                self.escena_actual = self.seccion['reproductor'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario,
                                                                 self.clip_elegido)
                self.estamos_en['cargar clip'] = False
                self.estamos_en['reproductor'] = True
            # Si hay que editar
            elif boton and 'e' in boton:
                # Si queres acceder a la posición del clip que se eligió
                # usa la posición 1 del string, porque las claves se guardan como:
                # r0, e0, r1, e1, etc.. Fijate el ejemplo de arriba
                self.clip_elegido = int(boton[1])
                self.fondo()
                self.escena_actual = self.seccion['editor clip'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario,
                                                                 self.clip_elegido)
                self.estamos_en['cargar clip'] = False
                self.estamos_en['editor clip'] = True

# Reproductor

    def manejador_reproductor(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            # Si aprieta play y no terminó el clip, ni se está reproduciendo la
            # secuencia
            if boton == 'play' and not self.secuencia and not self.escena_actual.fin:
                self.escena_actual.play()
                self.escena_actual.comenzar_musica()
                self.secuencia = True
            # Si aprieta pausa y se está reproduciendo la secuencia
            elif boton == 'pausa' and self.secuencia:
                self.escena_actual.pausa()
                pygame.mixer.music.pause()
                self.secuencia = False
            elif boton == 'stop':
                self.escena_actual.fin_clip('Tu clip ha finalizado')
                self.secuencia = False
            elif boton == 'loop':
                self.escena_actual.actualizar_loop()
            elif boton == 'atras':
                pygame.mixer.music.stop()
                self.secuencia = False
                self.fondo()
                self.escena_actual = self.seccion['cargar clip'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario)
                self.estamos_en['reproductor'] = False
                self.estamos_en['cargar clip'] = True

# Armar clip

    def manejador_armarclip(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Chequea qué botón fue presionado
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            if boton == 'Atras':
                boton = 'cargar clip'
                self.fondo()
                self.escena_actual = self.seccion[boton](self.pantalla,
                                                         self.ANCHO,
                                                         self.ALTO,
                                                         self.usuario)
                self.estamos_en['armar clip'] = False
                self.estamos_en[boton] = True
                self.entrada_de_texto = False
            elif boton == 'Predefinidas':
                # Mantiene el ultimo botón de IMAGENES que fue pulsado
                self.ultimo_boton = 'predefinidas'
                self.escena_actual.actualizar_grilla('predefinidas')
            elif boton == 'Camara':
                # Mantiene el ultimo botón de IMAGENES que fue pulsado
                self.ultimo_boton = 'camara'
                self.escena_actual.actualizar_camara()
            elif boton == 'Buscar' and not self.entrada_de_texto:
                # Mantiene el ultimo botón de IMAGENES que fue pulsado
                self.ultimo_boton = 'busqueda'
                self.escena_actual.comenzar_buscar()
                self.entrada_de_texto = True
                self.limite = False
            elif boton == 'Elegir Musica':
                self.ultimo_boton = 'cancion'
                self.escena_actual.interfaz_cancion()
                self.escena_actual.boton_loop()
            elif boton == 'Loop':
                self.escena_actual.switch_loop()
                self.datos_usuario['musica']['loop'] = self.escena_actual.cancion_loop

            elif boton == 'Finalizar':
                self.posicion_clip = 0
                self.ultimo_boton = 'finalizar'
                # Pide el nombre del clip
                self.fondo()
                self.escena_actual = self.seccion['nombre clip'](self.pantalla,
                                                                 self.ANCHO,
                                                                 self.ALTO,
                                                                 self.usuario)
                self.estamos_en['armar clip'] = False
                self.estamos_en['nombre clip'] = True
                self.entrada_de_texto = True
            elif boton and boton in "0123456789" and self.ultimo_boton:  # Si toca alguna imagen o cancion
                if self.ultimo_boton == 'camara':
                    boton = '0'
                # si no tocan una cancion al editor
                if self.ultimo_boton not in ('cancion', 'finalizar', 'cancelar', 'loop'):
                    # Seteo la ultima sección para el editor
                    self.ultima_seccion = 'armar clip'
                    # Lanzo el editor
                    self.fondo()
                    self.escena_actual = self.seccion['editor'](self.pantalla,
                                                                self.ANCHO,
                                                                self.ALTO,
                                                                self.usuario)
                    self.escena_actual.iniciar_editor(os.path.join(
                        'imagenes', self.ultimo_boton, boton + '.jpg'),
                      )
                    self.estamos_en['armar clip'] = False
                    self.estamos_en['editor'] = True
                elif self.ultimo_boton == 'cancion':  # sino le pone play a la pos indicada
                    cancion = os.listdir(os.path.join('audio', 'canciones'))
                    cancion = list(sorted(cancion))
                    ruta = os.path.join(
                        'audio', 'canciones', cancion[int(boton)])
                    self.escena_actual.seleccionar_cancion(ruta, boton)
                    # poner la cancion en el diccionario que se subira al json
                    self.datos_usuario['musica']['ruta'] = ruta

            if boton and pygame.mixer.music.get_busy() and boton not in "0123456789":
                pygame.mixer.music.fadeout(500)

        if event.type == pygame.KEYDOWN:
            if self.entrada_de_texto:
                self.manejador_buscar(event)

    def manejador_buscar(self, event):
        if event.key == pygame.K_RETURN:  # Si apreta enter
            self.escena_actual.buscar_enter()
            self.entrada_de_texto = False
        elif event.key == pygame.K_BACKSPACE:  # Si borra
            self.escena_actual.buscar_borrar()
        elif not self.limite:  # Si ingresa cualquier tecla y no superó la caja
            self.escena_actual.actualizar_texto(event.unicode)
        self.limite = self.escena_actual.renderizar_texto_buscar()

# Editor

    def ultima_modificacion(self, dicc_img):
        """Actualiza los cambios y la fecha en la cual se los hizo"""
        # Abro para extraer el json
        with open(os.path.join('archivos', 'usuarios.json'), 'r') as arch:
            dicc = json.load(arch)
            # Modifico y le agrego la fecha actual
            dicc[self.usuario][self.clip_elegido]['fecha'] = datetime.now().strftime(
                '%d-%m-%y %H:%M')
            # Agrego sonido y duración
            dicc[self.usuario][self.clip_elegido]['imagenes'][int(self.nombre_imagen)-1] = dicc_img
        with open(os.path.join('archivos', 'usuarios.json'), 'w') as arch:
            json.dump(dicc, arch, ensure_ascii=False, indent=4)

    def manejador_editor(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            # Si elige la opción "agregar sonido" se deshabilitan los demás
            # botones
            self.entrada_de_texto = False  # para desactivar el input si hace click
            if self.ultimo_boton != 'sonido':
                if boton == 'agregar':
                    # Si pulsa agregar, se actualiza el archivo en la key
                    # imagenes
                    dicc_img = {
                        'directorio': '',
                        'duracion': self.escena_actual.duracion,
                        'sonido': self.escena_actual.sonido
                    }
                    # Si llama al editor en el Armar clip
                    if self.ultima_seccion == 'armar clip':
                        self.posicion_clip += 1
                        dicc_img['directorio'] = os.path.join(
                            'archivos', self.usuario, 'temp', str(self.posicion_clip) + '.jpg')
                        self.datos_usuario['imagenes'].append(dicc_img)
                    # Si llama al editor en el EDITOR del clip
                    elif self.ultima_seccion == 'editor clip':
                        dicc_img['directorio'] = self.directorio
                        self.ultima_modificacion(dicc_img)
                    self.escena_actual.agregar_clip(dicc_img['directorio'])
            # Duracion
                elif boton == 'incrementar':
                    self.escena_actual.incrementar_duracion()
                elif boton == 'decrementar':
                    self.escena_actual.decrementar_duracion()
            # Sonido
                elif boton == 'sonido':
                    self.ultimo_boton = 'sonido'
                    self.escena_actual.agregar_sonido()
            # Cuadrado
                elif boton == 'cuadrado_R':
                    self.escena_actual.crear_cuadrado()
                elif boton == 'cuadrado_V':
                    self.escena_actual.crear_cuadrado(True)
            # Linea
                elif boton == 'linea':
                    self.escena_actual.crear_linea()
            # Circulo
                elif boton == 'circulo_R':
                    self.escena_actual.crear_circulo()
                elif boton == 'circulo_V':
                    self.escena_actual.crear_circulo(True)
            # Opciones
                elif boton == 'color':
                    self.escena_actual.cambiar_color()
                elif boton == 'inc_grosor':
                    self.escena_actual.incrementar_grosor()
                elif boton == 'dec_grosor':
                    self.escena_actual.decrementar_grosor()
            # Texto
                elif boton == 'texto':
                    self.escena_actual.insertar_texto()
                    self.entrada_de_texto = True
                    self.limite = False
                elif boton == 'color_fondo':
                    self.escena_actual.cambiar_color_fondo()
                elif boton == 'tipografia':
                    self.escena_actual.cambiar_estilo()
                elif boton == 'inc_tamaño':
                    self.escena_actual.incrementar_tamaño()
                elif boton == 'dec_tamaño':
                    self.escena_actual.decrementar_tamaño()
            # Filtro
                elif boton == 'filtro':
                    self.escena_actual.cambiar_filtro()
            # Salida/Agregar
                if boton == 'salir' or boton == 'agregar':
                    # Vuelve a armar clip o al editor del clip
                    self.fondo()
                    if self.ultima_seccion == 'editor clip':
                        self.escena_actual = self.seccion[self.ultima_seccion](self.pantalla,
                                                                               self.ANCHO,
                                                                               self.ALTO,
                                                                               self.usuario,
                                                                               self.clip_elegido)
                    else:
                        self.escena_actual = self.seccion[self.ultima_seccion](self.pantalla,
                                                                               self.ANCHO,
                                                                               self.ALTO,
                                                                               self.usuario)
                    self.estamos_en[self.ultima_seccion] = True
                    self.estamos_en['editor'] = False
            elif boton:
                if boton in '0123456':  # Si elige algún sonido
                    self.escena_actual.sonido_elegido(int(boton))
                # Vuelve al editor con la imagen de respaldo
                self.ultimo_boton = ''
                respaldo = os.path.join('imagenes', 'respaldo', '0.jpg')
                self.escena_actual.iniciar_editor(respaldo)
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_mods() & pygame.KMOD_LCTRL:
                if event.key == pygame.K_z:
                    respaldo = os.path.join('imagenes', 'respaldo', '0.jpg')
                    self.escena_actual.iniciar_editor(respaldo)
            if self.entrada_de_texto:
                self.manejador_escribir_editor(event)

    def manejador_escribir_editor(self, event):
        if event.key == pygame.K_RETURN:  # Si apreta enter
            self.entrada_de_texto = False
        elif event.key == pygame.K_BACKSPACE:  # Si borra
            self.escena_actual.borrar()
        elif not self.limite:  # Si ingresa cualquier tecla y no superó la caja
            self.escena_actual.actualizar_texto(event.unicode)
        self.limite = self.escena_actual.renderizar_texto_escribir()

# Nombre clip

    def manejador_nombreclip(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Si apreta enter
                self.escena_actual.enter()
                if self.escena_actual.existe:
                    self.escena_actual.avisar_existe()
                else:
                    # Aviso
                    self.fondo()
                    self.escena_actual.avisar_correcto()
                    # Escribe el nombre del clip
                    self.nombre_clip = self.escena_actual.nombre_clip
                    self.escribir_clips()
                    # Vuelve al menú
                    self.fondo()
                    self.escena_actual = self.seccion['menu'](self.pantalla,
                                                              self.ANCHO,
                                                              self.ALTO,
                                                              self.usuario)
                    self.estamos_en['nombre clip'] = False
                    self.estamos_en['menu'] = True
                    self.entrada_de_texto = False
            elif event.key == pygame.K_BACKSPACE:  # Si borra
                self.escena_actual.borrar()
            elif not self.limite:  # Si ingresa cualquier tecla y no superó la caja
                self.escena_actual.actualizar_texto(event.unicode)
            if self.entrada_de_texto:
                self.limite = self.escena_actual.renderizar_texto_buscar()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si presiona cancelar
            if self.escena_actual.cancelar.collidepoint(pygame.mouse.get_pos()):
                self.ultimo_boton = 'cancelar'
                # Vuelve a armar clip
                self.fondo()
                self.escena_actual = self.seccion['armar clip'](self.pantalla,
                                                                self.ANCHO,
                                                                self.ALTO,
                                                                self.usuario)
                self.estamos_en['nombre clip'] = False
                self.estamos_en['armar clip'] = True
                self.entrada_de_texto = False

    def escribir_clips(self):
        """Escribe la secuencia de clips en el disco"""
        with open(os.path.join('archivos', 'usuarios.json'), 'r') as arch:
            dicc = json.load(arch)
            # Logica
            self.renombrar_datos()
            if self.usuario not in dicc.keys():
                dicc[self.usuario] = list()
            # Le agrego la fecha actual
            self.datos_usuario['fecha'] = datetime.now(
            ).strftime('%d-%m-%y %H:%M')
            dicc[self.usuario].append(self.datos_usuario)
        with open(os.path.join('archivos', 'usuarios.json'), 'w') as arch:
            json.dump(dicc, arch, ensure_ascii=False, indent=4)

    def renombrar_datos(self):
        """Renombra a temp por el nombre del clip"""
        os.rename(os.path.join('archivos', self.usuario, 'temp'),
                  os.path.join('archivos', self.usuario, self.nombre_clip))
        self.datos_usuario['clip'] = self.nombre_clip
        # Cambia la ruta de temp por la del nombre del clip de cada imagen
        # elegida
        for dicc in self.datos_usuario['imagenes']:
            dicc['directorio'] = dicc['directorio'].replace(
                'temp', self.nombre_clip)

# Editor Clip

    def manejador_editorclip(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            boton = self.escena_actual.chequear_botones(pygame.mouse.get_pos())
            if boton == 'der':
                self.escena_actual.aumentar_imagenes()
            elif boton == 'izq':
                self.escena_actual.decrementar_imagenes()
            elif boton and boton in "012":
                # Calculo el directorio de la imagen
                self.nombre_imagen = str(
                    (self.escena_actual.pos_img - (3 - int(boton))) + 1)
                self.directorio = os.path.join('archivos', self.usuario,
                                               self.escena_actual.clip['clip'], self.nombre_imagen + '.jpg')
                # Lanzo el editor si la imágen existe (puede hacer click en
                # algún rectangulo vacío)
                if os.path.exists(self.directorio):
                    # Seteo la ultima seccion para el editor
                    self.ultima_seccion = 'editor clip'
                    self.fondo()
                    self.escena_actual = self.seccion['editor'](self.pantalla,
                                                                self.ANCHO,
                                                                self.ALTO,
                                                                self.usuario)
                    self.escena_actual.iniciar_editor(
                        self.directorio)
                    self.estamos_en['editor clip'] = False
                    self.estamos_en['editor'] = True

            elif boton == 'finalizar':
                boton = 'cargar clip'
                self.fondo()
                self.escena_actual = self.seccion[boton](self.pantalla,
                                                         self.ANCHO,
                                                         self.ALTO,
                                                         self.usuario)
                self.estamos_en['editor clip'] = False
                self.estamos_en[boton] = True

# Eventos

    def eventos(self):
        """Captura de eventos"""
        for event in pygame.event.get():
            # receptor de secciones
            if self.estamos_en['menu']:
                self.manejador_menu(event)
            elif self.estamos_en['armar clip']:
                self.manejador_armarclip(event)
            elif self.estamos_en['cargar clip']:
                self.manejador_cargarclip(event)
            elif self.estamos_en['editor']:
                self.manejador_editor(event)
            elif self.estamos_en['jugar juego']:
                self.escena_actual.chequear_eventos(event)
            elif self.estamos_en['nombre clip']:
                self.manejador_nombreclip(event)
            elif self.estamos_en['reproductor']:
                self.manejador_reproductor(event)
            elif self.estamos_en['editor clip']:
                self.manejador_editorclip(event)
            # receptor de teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False

            if event.type == pygame.QUIT:
                self.run = False

# Loop

    def loop(self):
        """Bucle en donde ocurre la lógica del juego"""
        while self.run:
            self.eventos()
            if self.estamos_en['jugar juego']:
                # Si perdió, entonces vuelve al menú
                if self.escena_actual.actualizar():
                    self.estamos_en['jugar juego'] = False
                    self.estamos_en['menu'] = True
                    self.fondo()
                    self.escena_actual = self.seccion['menu'](self.pantalla,
                                                              self.ANCHO,
                                                              self.ALTO,
                                                              self.usuario)
                    time.sleep(6)
            elif self.estamos_en['reproductor']:
                # Si está en la secuencia
                if self.secuencia:
                    # Actualiza la imagen
                    self.escena_actual.avanzar_imagen()
                    # Si llegó al fin
                    if self.escena_actual.fin:
                        self.escena_actual.fin_clip('Tu clip ha finalizado')
                        self.secuencia = False
            pygame.display.update()
            pygame.time.Clock().tick(20)

    def finalizacion(self):
        """Actos qué hacer antes de terminar con la ejecución"""
        pygame.quit()
        sys.exit()

    def ejecutar(self):
        """Ejecución del juego"""
        self.inicializaciones()
        self.loop()
        self.finalizacion()


if __name__ == '__main__':
    Aplicacion().ejecutar()
