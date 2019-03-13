# -*- coding: utf-8 -*-
import pygame
import sys
import time
import random
import json
import os
from datetime import datetime
from herramientas.Utilidades import Tools


class JugarJuego():
    """Adaptación del juego Snake realizado por el usuario apaar97"""

    def __init__(self, pantalla, ancho, alto, usuario):
        # Colores
        self.ROJO = pygame.Color(255, 0, 0)
        self.VERDE = pygame.Color(0, 255, 0)
        self.NEGRO = pygame.Color(0, 0, 0)
        self.BLANCO = pygame.Color(255, 255, 255)
        self.MARRON = pygame.Color(165, 42, 42)
        self.NEGRO_MATE = pygame.Color(26, 26, 26)

        # Pantalla
        self.pantalla = pantalla
        self.pantalla.fill(self.BLANCO)
        self.ALTO = alto
        self.ANCHO = ancho

        # Opciones del juego
        self.usuario = usuario
        self.delta = 10
        self.snakePos = [100, 50]
        self.snakeBody = [[100, 50], [90, 50], [80, 50]]
        self.foodPos = [400, 50]
        self.foodSpawn = True
        self.direction = 'RIGHT'
        self.changeto = ''
        self.score = 0

        # herramientas
        self.tools = Tools(self.pantalla)

    def mostrar_puntajes(self, a_json):
        """Muestra el mayor puntaje por usuario"""
        color = ((204, 0, 102), (128, 0, 0))
        fuente = pygame.font.SysFont('monaco', 32)
        # Tabla
        tabla = pygame.draw.rect(self.pantalla, self.MARRON,
                                 (self.ANCHO / 2 - 250, self.ALTO / 2 - 150) +
                                 (500, 500))
        # Encabezado
        rect_usuario = pygame.draw.rect(self.pantalla, color[
            0 % 2], (tabla.left, tabla.top, tabla.width / 3, tabla.height // 10))
        rect_score = pygame.draw.rect(self.pantalla, color[
                                      0 % 2 - 1], (tabla.left + tabla.width / 3, tabla.top, tabla.width / 3, tabla.height // 10))
        rect_tiempo = pygame.draw.rect(self.pantalla, color[
                                       0 % 2], (tabla.left + 2 * tabla.width / 3, tabla.top, tabla.width / 3, tabla.height // 10))
        self.tools.sombrear('USUARIO', self.NEGRO_MATE,
                            color[0 % 2], fuente, rect_usuario)
        self.tools.sombrear('SCORE', self.NEGRO_MATE,
                            color[0 % 2 - 1], fuente, rect_score)
        self.tools.sombrear('FECHA', self.NEGRO_MATE,
                            color[0 % 2], fuente, rect_tiempo)
        # Contenido
        i = 1
        for clave, valor in a_json.items():
            usuario = clave.upper()
            score = valor['score']
            tiempo = valor['tiempo']

            rect_usuario = pygame.draw.rect(self.pantalla, color[
                                            i % 2], (tabla.left, tabla.top + i * tabla.height // 10, tabla.width / 3, tabla.height // 10))
            rect_score = pygame.draw.rect(self.pantalla, color[
                                          i % 2 - 1], (tabla.left + tabla.width / 3, tabla.top + i * tabla.height // 10, tabla.width / 3, tabla.height // 10))
            rect_tiempo = pygame.draw.rect(self.pantalla, color[
                                           i % 2], (tabla.left + 2 * tabla.width / 3, tabla.top + i * tabla.height // 10, tabla.width / 3, tabla.height // 10))
            self.tools.sombrear(usuario, self.BLANCO,
                                color[i % 2 - 1], fuente, rect_usuario)
            self.tools.sombrear(str(score), self.BLANCO,
                                color[i % 2], fuente, rect_score)
            self.tools.sombrear(tiempo, self.BLANCO,
                                color[i % 2 - 1], fuente, rect_tiempo)
            i += 1

    def actualizar_score(self):
        # Leo la lista de scores
        datos_usuario = {
            'score': self.score,
            'tiempo': datetime.now().strftime('%d-%m-%y %H:%M')
        }
        with open(os.path.join('archivos', 'score_snake.json'), 'r') as f:
            archivo = json.load(f)
        # Confirmo que el usuario existe y actualizo
        if self.usuario in archivo.keys():
            if self.score > archivo[self.usuario]['score']:
                archivo[self.usuario] = datos_usuario
        else:
            archivo[self.usuario] = datos_usuario
        # Ordeno el archivo por puntaje
        archivo = dict(sorted(archivo.items(),
                              key=lambda items: items[1]['score'],
                              reverse=True))
        with open(os.path.join('archivos', 'score_snake.json'), 'w') as f:
            json.dump(archivo, f, indent=4, ensure_ascii=False, )
        # Armo la lista de puntajes en la pantalla
        self.mostrar_puntajes(archivo)

    def gameOver(self):
        '''Determina que hacer cuando el jugador perdió'''
        self.actualizar_score()
        self.perdi = True
        self.myFont = pygame.font.SysFont('monaco', 72)
        self.GOsurf = self.myFont.render("PERDISTE!", True, self.ROJO)
        self.GOrect = self.GOsurf.get_rect()
        self.GOrect.midtop = (self.ANCHO / 2, 80)
        self.pantalla.blit(self.GOsurf, self.GOrect)
        self.showScore(0)
        pygame.display.update()

    def showScore(self, choice=1):
        '''Muestra el puntaje del jugador en pantalla'''
        self.SFont = pygame.font.SysFont('monaco', 32)
        self.Ssurf = self.SFont.render("Score  :  {0}".format(self.score),
                                       True, self.NEGRO)
        self.Srect = self.Ssurf.get_rect()
        if choice == 1:
            self.Srect.midtop = (80, 10)
        else:
            self.Srect.midtop = (self.ANCHO / 2, 140)
        self.pantalla.blit(self.Ssurf, self.Srect)

    def chequear_eventos(self, event):
        '''Chequea los eventos para el movimiento de la viborita'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.changeto = 'DOWN'

    def actualizar(self):
        '''Actualiza la pantalla, en caso de perder, devuelve True'''
        self.perdi = False
        # Validate direction
        if self.changeto == 'RIGHT' and self.direction != 'LEFT':
            self.direction = self.changeto
        if self.changeto == 'LEFT' and self.direction != 'RIGHT':
            self.direction = self.changeto
        if self.changeto == 'UP' and self.direction != 'DOWN':
            self.direction = self.changeto
        if self.changeto == 'DOWN' and self.direction != 'UP':
            self.direction = self.changeto

        # Update snake position
        if self.direction == 'RIGHT':
            self.snakePos[0] += self.delta
        if self.direction == 'LEFT':
            self.snakePos[0] -= self.delta
        if self.direction == 'DOWN':
            self.snakePos[1] += self.delta
        if self.direction == 'UP':
            self.snakePos[1] -= self.delta

        # Snake body mechanism
        self.snakeBody.insert(0, list(self.snakePos))
        if self.snakePos == self.foodPos:
            self.foodSpawn = False
            self.score += 1
        else:
            self.snakeBody.pop()
        if not self.foodSpawn:
            self.foodPos = [random.randrange(1, self.ANCHO // 10) * self.delta,
                            random.randrange(1, self.ALTO // 10) * self.delta
                            ]
            self.foodSpawn = True

        self.pantalla.fill(self.BLANCO)
        for pos in self.snakeBody:
            pygame.draw.rect(self.pantalla, self.VERDE, pygame.Rect(pos[0],
                                                                    pos[1], self.delta, self.delta))
        pygame.draw.rect(self.pantalla, self.MARRON,
                         pygame.Rect(self.foodPos[0],
                                     self.foodPos[1],
                                     self.delta,
                                     self.delta))

        # Bounds
        if self.snakePos[0] >= self.ANCHO or self.snakePos[0] < 0:
            self.gameOver()
        if self.snakePos[1] >= self.ALTO or self.snakePos[1] < 0:
            self.gameOver()

        # Self hit
        for block in self.snakeBody[1:]:
            if self.snakePos == block:
                self.gameOver()

        self.showScore()

        return self.perdi
