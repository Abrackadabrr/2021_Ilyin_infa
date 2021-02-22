import pygame
from pygame.draw import *
from random import randint as ri
import math as m
pygame.init()

FPS = 30
screen = pygame.display.set_mode((650, 750))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


def house(x, y, w=300, l=400):
    '''
    :param x: x-coord of start point (left Lower angle)
    :param y: y-coord of start point (left Lower angle)
    :param a: wight (default = 300)
    :param b: hight (default = 400)
    :return: draw house
    '''

    first_floor_h = l / 8
    balcony_h = l / 1.8

    w_smallwindow = w / 6  # would not recommend changing
    h_smallwindow = l / 6  # would not recommend changing
    between_small_windiws = w / 6  # would not recommend changing
    first_floor_indent = (23 / 300) * w  # would not recommend changing

    fasade_color = (50, 40, 15)  #
    dark_smallwindow_color = (50, 30, 15)  #
    light_smallwindow_color = (255, 255, 0)  #
    longwindow_color = (56, 56, 56)  #
    balcony_color = (38, 38, 38)
    roof_color = (5, 5, 5)

    rect(screen, fasade_color, (x, y - l, w, l), 0)

    # draw small windows
    for i in range(3):
        x_ = x + first_floor_indent + i * (between_small_windiws + w_smallwindow)
        y_ = y - first_floor_h - h_smallwindow
        if i == 2:
            rect(screen, light_smallwindow_color, (x_, y_, w_smallwindow, h_smallwindow), 0)
        else:
            rect(screen, dark_smallwindow_color, (x_, y_, w_smallwindow, h_smallwindow), 0)

    # draw long windows
    rect(screen, longwindow_color, (x + (35 / 300) * w, y - l, (30/300)*w, (170/400)*l), 0)
    rect(screen, longwindow_color, (x + (35 / 300) * w + (30 / 300) * w + (25 / 300) * w, y - l, (30/300)*w, (170/400)*l), 0)
    rect(screen, longwindow_color, (x + ((35 / 300) + (30 / 300) + (25 / 300) + (30 / 300) + (35 / 300)) * w, y - l, (30/300)*w, (170/400)*l), 0)
    rect(screen, longwindow_color, (x + ((35 / 300) + (30 / 300) + (25 / 300) + (30 / 300) + (35 / 300) + (30/300) + (45/300))*w, y - l, (30/300)*w, (170/400)*l), 0)

    # draw balcony
    x_of_balcony = x - (30/300)*w
    y_of_balcohy = y - balcony_h
    between_balcas = (37/300)*w  # don't change it (иначе балкон уедет)
    rect(screen, balcony_color, (x_of_balcony, y_of_balcohy, w + (60/300)*w, (30/400)*l), 0)
    rect(screen, balcony_color, (x_of_balcony + (15/300)*w, y_of_balcohy - (30/400)*l, (10/300)*w, (30/400)*l + 2), 0)
    for i in range(1, 6):
        xx = x_of_balcony + (15/300)*w + i * between_balcas + (i - 1) * (20/300)*w
        rect(screen, balcony_color, (xx, y_of_balcohy - (30/400)*l, (20/300)*w, (30/400)*l + 2), 0)
    rect(screen, balcony_color, (x_of_balcony + (15/300)*w + 6 * between_balcas + (6 - 1) * (20/300)*w - (2/300)*w, y_of_balcohy - (30/400)*l, (10/300)*w, (30/400)*l + 2),0)
    rect(screen, balcony_color, (x_of_balcony + (25/300)*w, y_of_balcohy - (50/400)*l, w + (10/300)*w + 1, (20/400)*l), 0)

    # draw roof
    polygon(screen, roof_color, ((x - (30/300)*w, y - l - 1), (x + (20/300)*w, y - l - 1), (x + (20/300)*w, y - l - (40/400)*l)))
    polygon(screen, roof_color, ((x + w + (30/300)*w, y - l - 1), (x + w - (20/300)*w, y - l - 1), (x + w - (20/300)*w, y - l - (40/400)*l)))
    rect(screen, roof_color, (x + (20/300)*w, y - l - (40/400)*l, w - (40/300)*w, (40/400)*l), 0)


def moon():
    circle(screen, (255, 255, 255), (550, 100), 50)


def clouds_r(n):
    for i in range(n):
        ellipse(screen, (ri(150, 200), 128, 128), (ri(100, 600), ri(30, 300), ri(200, 300), ri(50, 70)))


def chimney1(x, y, w=300, l=400):
    chimney_color = (56, 56, 56)
    rect(screen, chimney_color, (x + (250/300)*w, y - l - (75/400)*l, (10/300)*w, (70/400)*l+1))
    rect(screen, chimney_color, (x + (50 / 300) * w, y - l - (90 / 400) * l, (20 / 300) * w, (50 / 400) * l+1))


def chimney2(x, y, w=300, l=400):
    chimney_color = (56, 56, 56)
    rect(screen, chimney_color, (x + (200/300)*w, y - l - (90/400)*l, (25/300)*w, (60/400)*l+1))
    rect(screen, chimney_color, (x + (100/300) * w, y - l - (100 / 400) * l, (30/ 300) * w, (90 / 400) * l+1))


def set_start_environment():
    rect(screen, (128, 128, 128), (0, 0, 650, 300), 0)
    rect(screen, (15, 15, 15), (0, 300, 650, 450), 0)
    moon()


def ghost(x, y, s, k = 1,r = 1):
    circle(s, (255, 255, 255), (x, y), 25*k)
    circle(s, (25, 150, 255), (x - r*10*k, y - 9*k), 5 * k)
    circle(s, (25, 150, 255), (x + r*8*k, y - 9*k), 5 * k)
    circle(s, (0, 0, 0), (x - r*11*k, y - 9*k), 2 * k)
    circle(s, (0, 0, 0), (x + r*7 * k, y - 9 * k), 2 * k)

    a = []  # list of points
    b = []  # list that helps me create right range
    for i in range(35):
        a.append((x - 2*i*k, y + 0.1*i*i*k))
    for i in range(70):
        a.append((x - 69*k + i*k, y + 122*k - 15* k * m.sin(3.14*i/70)))
    for i in range(70):
        a.append((x + i*k, y + 122*k + 15* k * m.sin(3.14 * i / 70)))
    for i in range(35):
        b.append(35 - i)
    for i in b:
        a.append((x + 2*i*k, y + 0.1*i*i*k))
    polygon(s, 'WHITE', a)


def picture_first():
    set_start_environment()
    clouds_r(3)
    house(50, 560,300, 400)
    chimney1(50, 560,300, 400)
    clouds_r(3)
    chimney2(50, 560,300, 400)
    ghost(500, 500, screen)


def picture_second():
    set_start_environment()

    clouds_r(3)

    house(500, 350, 120, 180)
    chimney1(500, 350, 120, 180)
    chimney2(500, 350, 120, 180)
    house(300, 475, 150, 200)
    chimney1(300, 475, 150, 200)
    chimney2(300, 475, 150, 200)

    # clouds
    for i in range(4):
        k = 0.7 + 0.1*i
        surface1 = pygame.Surface((500*k, 70*k))
        ellipse(surface1, (ri(140, 200), 128, 128), (0, 0, 500*k, 70*k))
        surface1.set_colorkey((0, 0, 0))
        surface1.set_alpha(128)
        screen.blit(surface1, (ri(0, 600), ri(200, 400)))

    house(50, 600, 150, 200)
    chimney1(50, 600, 150, 200)
    chimney2(50, 600, 150, 200)

    for i in range(4):
        k = 0.7 + 0.1 * i
        surface1 = pygame.Surface((300 * k, 200 * k))
        if ri(0, 1) == 0:
            ghost(150*k, 30*k, surface1, k, 1)
        else:
            ghost(150 * k, 30 * k, surface1, k, -1)
        surface1.set_colorkey((0, 0, 0))
        surface1.set_alpha(128)
        screen.blit(surface1, (ri(0, 600), ri(500, 600)))

picture_second()
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
