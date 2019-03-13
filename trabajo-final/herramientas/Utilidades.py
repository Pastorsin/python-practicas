# -*- coding: utf-8 -*-

import os
import json
import pygame


class Tools():
    """ Funciones utiles usadas en varios modulos """

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.cont = 1

    def centrar(self, contendor, elemento):
        """ retorna la posicion para que el elemento quede
            alineado en el centro del contenedor """

        return (contendor.centerx - elemento.get_width() / 2,
                contendor.centery - elemento.get_height() / 2)

    def consulta_botones(self, pos_mouse, clicks):
        for seccion, rect in clicks.items():
            if rect[0].collidepoint(pos_mouse):
                return seccion

    def sombrear(self, texto, C1, C2, fuente, contendor):
        """ sombrea el texto recibido por parametro y lo ubica dentro
            del contenedor """

        elemento = fuente.render(texto, True, C1)
        sombra = fuente.render(texto, True, C2)

        pos = self.centrar(contendor, elemento)

        self.pantalla.blit(sombra, (pos[0] - 2, pos[1] + 2))
        self.pantalla.blit(elemento, pos)

    def obtener_posicion_click(self, imagen):
        """ Devuelve la posicion donde se hizo click dentro de un rectangulo """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if imagen.collidepoint(pygame.mouse.get_pos()):
                        pygame.mouse.set_cursor(
                            *pygame.cursors.broken_x) if self.cont % 2 == 1 else pygame.mouse.set_cursor(*pygame.cursors.arrow)
                        self.cont += 1
                        return pygame.mouse.get_pos()

    def obtener_pos_tam(self, imagen):
        """ Devuelve la distancia entre dos clicks """
        pos1 = self.obtener_posicion_click(imagen)
        pos2 = self.obtener_posicion_click(imagen)
        return (pos1 + (pos2[0] - pos1[0], pos2[1] - pos1[1]))

    def guardar_cambio(self, imagen, caja_principal, nombre):
        """ Almacena en el directorio la imagen pasada por parametro """
        imagen_editada = self.pantalla.subsurface(
            imagen.get_rect().move(self.centrar(caja_principal, imagen)))
        pygame.image.save(imagen_editada, os.path.join(
            'imagenes', 'respaldo', nombre))
