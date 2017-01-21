#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame,sys,os

def cargar_imagen(nombre):
	imagen = pygame.image.load(nombre)
	return imagen

class Jugador(pygame.sprite.Sprite):
	def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.x = 50
			self.y = 50
			self.tiempo = 10
			self.imagenes = []
			self.imagenes.append(cargar_imagen("sprite.png"))
			self.imagenes.append(cargar_imagen("sprite2.png"))
			self.imagenes.append(cargar_imagen("sprite3.png"))
			self.index = 0
			self.imagen = self.imagenes[self.index]
	def dibujar(self,ventana):
	
		ventana.blit(self.imagen,(self.x,self.y))
	def mover(self,dx,dy):
		self.tiempo -= 1
		if self.tiempo == 0:
			self.tiempo = 10		
			self.index += 1
			if self.index >= len(self.imagenes):
				self.index = 0
			self.imagen = self.imagenes[self.index]
		self.x += dx
		self.y += dy
