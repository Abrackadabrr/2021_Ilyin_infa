import pygame
from pygame.draw import *

fps = 30
pygame.init()
clock = pygame.time.Clock()
clock.tick(fps)
screen = pygame.display.set_mode((300, 200))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
