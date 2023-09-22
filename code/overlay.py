import pygame
from settings import *
from os import walk, path

class Overlay:
	def __init__(self, player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports
		self.tools_surf = {} 
		self.seeds_surf = {}

		full_path = f'.\graphics\overlay\\axe.png'
		image_surf = pygame.image.load(full_path).convert_alpha()
		self.tools_surf['axe'] = image_surf

		full_path = f'.\graphics\overlay\hoe.png'
		image_surf = pygame.image.load(full_path).convert_alpha()
		self.tools_surf['hoe'] = image_surf

		full_path = f'.\graphics\overlay\water.png'
		image_surf = pygame.image.load(full_path).convert_alpha()
		self.tools_surf['water'] = image_surf
		
		full_path = f'.\graphics\overlay\corn.png'
		image_surf = pygame.image.load(full_path).convert_alpha()
		self.seeds_surf['corn'] = image_surf

		full_path = f'.\graphics\overlay\\tomato.png'
		image_surf = pygame.image.load(full_path).convert_alpha()
		self.seeds_surf['tomato'] = image_surf

	def display(self):

		# tool
		tool_surf = self.tools_surf[self.player.selected_tool]
		tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
		self.display_surface.blit(tool_surf,tool_rect)

		# seeds
		seed_surf = self.seeds_surf[self.player.selected_seed]
		seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
		self.display_surface.blit(seed_surf,seed_rect)