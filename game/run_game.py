#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame, sys, os, math
from modulos.colors import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
medidas_pantalla = (1024,700)

ventana = pygame.display.set_mode(medidas_pantalla)
pygame.display.set_caption("game")
reloj = pygame.time.Clock()

cond_menu = True
cond_jugar = True
#flecha menu
posX, posY = 200,450
flecha_imagen = pygame.image.load("imagenes/sprite.png")
seno = 0
background_menu = pygame.image.load("imagenes/background_menu.png")

# menu loop ----------------------------------------------------------
while cond_menu:
	#procesar eventos
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
			if posY == 450:
				cond_menu = False
			else:
				pygame.quit()
				sys.exit()
		
	key = pygame.key.get_pressed()
	if key[pygame.K_UP]:
		posY = 450
	if key[pygame.K_DOWN]:
		posY = 550
			
	#actualizar
	reloj.tick(60)
	seno += 0.1
	#dibujar
	ventana.blit(background_menu,(0,0))
	ventana.blit(flecha_imagen,(posX,int(posY+math.degrees(math.sin(seno)) / 2 )) )
	pygame.display.update()

# juego loop -----------------------------------------------------------
while cond_jugar:
	#procesar eventos
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			cond_jugar = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			cond_jugar = False
	#actualizar
	reloj.tick(60)
	#dibujar
	ventana.fill(rojo)
	pygame.display.update()
