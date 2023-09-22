from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for root, dir, img_files in walk(f'.\graphics\character\{path}', topdown=True):

		for image in img_files:
			path_name = root.split('/')[len(root.split('/'))-1:][0]
			full_path = f'{path_name}\{image}'
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list