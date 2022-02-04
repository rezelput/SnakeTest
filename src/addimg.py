import pygame
import sys
import os
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,500))


bg = pygame.image.load(os.path.join("images", "cloud.jpg"))


pygame.mouse.set_visible(0)

ship = pygame.image.load(os.path.join("images", "ship.jpg"))
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2
screen.blit(ship, (ship_left,ship_top))

shot = pygame.image.load(os.path.join("images", "space.png"))
shoot_y = 0


pygame.display.set_caption('galaxy invaders')