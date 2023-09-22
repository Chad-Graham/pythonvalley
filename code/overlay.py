import pygame
from settings import *
from os import walk

class Overlay:
	def __init__(self, player):
		# print('starting overlay')
		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports 
		for root, dir, files in walk('.\graphics\overlay', topdown=True):
			# print('starting import')
			surface_list_1 = []
			surface_list_2 = []
			for file in files:
				print(file)
				full_path = root + '\\' + file
				image_surf = pygame.image.load(full_path).convert_alpha()

				if file == 'axe.png' or file == 'hoe.png' or file == 'water.png':
					surface_list_1.append(image_surf)
					self.tools_surf = surface_list_1
					# print(f'self.tools_surf: {self.tools_surf}')
				
				elif file == 'corn.png' or file == 'tomato.png':
					surface_list_2.append(image_surf) 			
					self.seeds_surf = surface_list_2
					# print(f'self.seeds_surf:{self.seeds_surf}') 

		# print(f'self.tools_surf: {self.tools_surf}')
		# print(f'self.seeds_surf:{self.seeds_surf}') 