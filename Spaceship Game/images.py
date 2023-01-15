import os
import pygame
game_folder = os.path.dirname(__file__)  # renaming the file where the main is
img_folder = os.path.join(game_folder, "Images")  # takes game folder and adds img folder


ship = pygame.image.load(os.path.join(img_folder, "ship.png"))