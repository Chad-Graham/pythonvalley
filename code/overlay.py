import pygame
from settings import *
from os import walk, path

class Overlay:
	def __init__(self, player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports 
		for root, dir, files in walk('.\graphics\overlay', topdown=True):

			surface_list_1 = {}
			surface_list_2 = {}
			
			for file in files:

				full_path = root + '\\' + file
				image_surf = pygame.image.load(full_path).convert_alpha()

				if file == 'axe.png' or file == 'hoe.png' or file == 'water.png':
					surface_list_1[path.splitext(file)[0]] = image_surf
					self.tools_surf = surface_list_1
				
				elif file == 'corn.png' or file == 'tomato.png':
					surface_list_2[path.splitext(file)[0]] = image_surf	
					self.seeds_surf = surface_list_2

	def display(self):

		# tool
		tool_surf = self.tools_surf[self.player.selected_tool]
		tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
		self.display_surface.blit(tool_surf,tool_rect)

		# seeds
		seed_surf = self.seeds_surf[self.player.selected_seed]
		seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
		self.display_surface.blit(seed_surf,seed_rect)