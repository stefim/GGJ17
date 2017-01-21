#!/usr/bin/python

import pygame

def cargar_imagen(ruta):
	imagen = pygame.image.load(ruta).convert_alpha()
	return imagen
	
class Bombero(pygame.sprite.Sprite):
	def __init__(self,inicioX,inicioY):
		pygame.sprite.Sprite.__init__(self)
		self.x, self.y = inicioX, inicioY
		self.dt_animacion = 15
		self.imagenes = []
		self.imagenes.append(cargar_imagen("imagenes/bombero.png"))
		self.index = 0
		self.imagen = self.imagenes[self.index]
		
	def dibujar(self,ventana):
		ventana.blit(self.imagen,(self.x,self.y))
		
	def actualizar(self):
		self.dt_animacion -= 1
		if (self.dt_animacion == 0):
			self.dt_animacion = 15
			self.index += 1
			if self.index >= len(self.imagenes):
				self.index = 0
			self.imagen = self.imagenes[self.index]
			
	def mover(self,dx,dy):
		self.x += dx
		self.y += dy

	def get_pos(self):
		return (self.x,self.y)
