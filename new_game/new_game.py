#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame,sys,os,math
from colors import *
from player import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
ancho,alto = 800,600
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("muevete")

reloj = pygame.time.Clock()

posX,posY = ancho/2, alto/2
x,y = 0,0

seno = 0
coseno = 0

menu = True
pos = 80

while menu:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and pos == 80:
			menu = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
			pos = 80
		if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
			pos = 300
	ventana.fill(lverde)
	pygame.draw.line(ventana,gris,(70,int(pos+math.degrees(math.sin(seno))/5)),(100,int(pos+math.degrees(math.sin(seno))/5)),5)

	seno += 0.1
	pygame.display.update()

seno = 0
l = 80

jugador = Jugador()
while True:
	# procesos
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		jugador.mover(-5,0)
	if key[pygame.K_RIGHT]:
		jugador.mover(5,0)
	if key[pygame.K_UP]:
		jugador.mover(0,-5)
	if key[pygame.K_DOWN]:
		jugador.mover(0,5)


	if posX < 780 or posX > 20:
		posX += x
	if posY < 580 or posY > 20:
		posY += y
	
	#actualizar
	seno += 0.1
	coseno += 0.1
	l += 1
	reloj.tick(60)

	# dibujo
	ventana.fill((255,255,255))
	jugador.dibujar(ventana)
	pygame.draw.circle(ventana ,negro , (posX,posY), 10)
	pygame.draw.circle(ventana,lrojo, (int(l+math.degrees(math.cos(coseno))),int(80+math.degrees(math.sin(seno)))),10)

	pygame.display.update()
	# frames per second
	
