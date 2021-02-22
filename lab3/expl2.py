import pygame
from pygame.draw import *

pygame.init()
color_background = (125, 125, 125)
FPS = 30

screen = pygame.display.set_mode((400, 400))


rect(screen, color_background, (x1, y1, 400, 400), 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()