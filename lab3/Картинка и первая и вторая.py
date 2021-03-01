import pygame
import sys
import pygame.draw as d
from random import randint as ri
import math as m

pygame.init()

FPS = 20
screen = pygame.display.set_mode((650, 750))
pygame.display.update()
clock = pygame.time.Clock()
finished = False


def house(x, y, width=300, length=400):
    '''
    :param length:
    :param width:
    :param x: x-coord of start point (left Lower angle)
    :param y: y-coord of start point (left Lower angle)
    :param a: wight (default = 300)
    :param b: hight (default = 400)
    :return: draw house
    '''

    first_floor_h = length / 8
    balcony_h = length / 1.8

    w_smallwindow = width / 6  # would not recommend changing
    h_smallwindow = length / 6  # would not recommend changing
    between_small_windiws = width / 6  # would not recommend changing
    first_floor_indent = (23 / 300) * width  # would not recommend changing

    fasade_color = (50, 40, 15)  #
    dark_smallwindow_color = (50, 30, 15)  #
    light_smallwindow_color = (255, 255, 0)  #
    longwindow_color = (56, 56, 56)  #
    balcony_color = (38, 38, 38)
    roof_color = (5, 5, 5)

    d.rect(screen, fasade_color, (x, y - length, width, length), 0)

    # draw small windows
    for i in range(3):
        x_ = x + first_floor_indent + i * (between_small_windiws + w_smallwindow)
        y_ = y - first_floor_h - h_smallwindow
        if i == 2:
            d.rect(screen, light_smallwindow_color, (x_, y_, w_smallwindow, h_smallwindow), 0)
        else:
            d.rect(screen, dark_smallwindow_color, (x_, y_, w_smallwindow, h_smallwindow), 0)

    # draw long windows
    d.rect(screen, longwindow_color, (x + (35 / 300) * width, y - length, (30 / 300) * width, (170 / 400) * length), 0)
    d.rect(screen, longwindow_color, (
    x + (35 / 300) * width + (30 / 300) * width + (25 / 300) * width, y - length, (30 / 300) * width,
    (170 / 400) * length), 0)
    d.rect(screen, longwindow_color, (
    x + ((35 / 300) + (30 / 300) + (25 / 300) + (30 / 300) + (35 / 300)) * width, y - length, (30 / 300) * width,
    (170 / 400) * length), 0)
    d.rect(screen, longwindow_color, (
    x + ((35 / 300) + (30 / 300) + (25 / 300) + (30 / 300) + (35 / 300) + (30 / 300) + (45 / 300)) * width, y - length,
    (30 / 300) * width, (170 / 400) * length), 0)

    # draw balcony
    x_of_balcony = x - (30 / 300) * width
    y_of_balcohy = y - balcony_h
    between_balcas = (37 / 300) * width  # don't change it (иначе балкон уедет)
    d.rect(screen, balcony_color, (x_of_balcony, y_of_balcohy, width + (60 / 300) * width, (30 / 400) * length), 0)
    d.rect(screen, balcony_color, (
    x_of_balcony + (15 / 300) * width, y_of_balcohy - (30 / 400) * length, (10 / 300) * width, (30 / 400) * length + 2),
           0)
    for i in range(1, 6):
        xx = x_of_balcony + (15 / 300) * width + i * between_balcas + (i - 1) * (20 / 300) * width
        d.rect(screen, balcony_color,
               (xx, y_of_balcohy - (30 / 400) * length, (20 / 300) * width, (30 / 400) * length + 2), 0)
    d.rect(screen, balcony_color, (
    x_of_balcony + (15 / 300) * width + 6 * between_balcas + (6 - 1) * (20 / 300) * width - (2 / 300) * width,
    y_of_balcohy - (30 / 400) * length, (10 / 300) * width, (30 / 400) * length + 2), 0)
    d.rect(screen, balcony_color, (
    x_of_balcony + (25 / 300) * width, y_of_balcohy - (50 / 400) * length, width + (10 / 300) * width + 1,
    (20 / 400) * length), 0)

    # draw roof
    d.polygon(screen, roof_color, ((x - (30 / 300) * width, y - length - 1), (x + (20 / 300) * width, y - length - 1),
                                   (x + (20 / 300) * width, y - length - (40 / 400) * length)))
    d.polygon(screen, roof_color, (
    (x + width + (30 / 300) * width, y - length - 1), (x + width - (20 / 300) * width, y - length - 1),
    (x + width - (20 / 300) * width, y - length - (40 / 400) * length)))
    d.rect(screen, roof_color,
           (x + (20 / 300) * width, y - length - (40 / 400) * length, width - (40 / 300) * width, (40 / 400) * length),
           0)


def moon():
    d.circle(screen, (255, 255, 255), (550, 100), 50)

def shar():
    WIN_WIDTH = 650
    WIN_HEIGHT = 190
    RED = (255, 0, 0)
    WHITE = (255,255,255)

    clock = pygame.time.Clock()
    # screen = pygame.display.set_mode(
    # (WIN_WIDTH, WIN_HEIGHT))
    # радиус будущего круга
    r = 50
    # координаты круга
    # скрываем за левой границей
    x = 0 - r
    # выравнивание по центру по вертикали
    y = WIN_HEIGHT // 2

    while 1:
        draw()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        # заливаем фон
        #screen.fill(WHITE)
        # рисуем круг
        pygame.draw.circle(screen, RED,
                           (x, y), r)
        # обновляем окно
        pygame.display.update()

        # Если круг полностью скрылся
        # за правой границей,
        if x >= WIN_WIDTH + r:
            # перемещаем его за левую
            x = 0 - r
        else:  # Если еще нет,
            # на следующей итерации цикла
            # круг отобразится немного правее
            x += 5
        clock.tick(FPS)


def clouds_r():
        d.ellipse(screen, (219,112,147), (350, 150, 180, 50))
        d.ellipse(screen, (219, 112, 147), (470, 200, 100, 30))


def chimney1(x, y, w=300, l=400):
    '''
    :param x: the same parametr as in function "house"
    :param y: the same parametr as in function "house"
    :param w: the same parametr as in function "house"
    :param l: the same parametr as in function "house"
    :return: draw two chimney
    '''
    chimney_color = (56, 56, 56)
    d.rect(screen, chimney_color, (x + (250 / 300) * w, y - l - (75 / 400) * l, (10 / 300) * w, (70 / 400) * l + 1))
    d.rect(screen, chimney_color, (x + (50 / 300) * w, y - l - (90 / 400) * l, (20 / 300) * w, (50 / 400) * l + 1))


def chimney2(x, y, w=300, l=400):
    '''
    :param x: the same parametr as in function "house"
    :param y: the same parametr as in function "house"
    :param w: the same parametr as in function "house"
    :param l: the same parametr as in function "house"
    :return: draw another two chimney
    '''

    chimney_color = (56, 56, 56)
    d.rect(screen, chimney_color, (x + (200 / 300) * w, y - l - (90 / 400) * l, (25 / 300) * w, (60 / 400) * l + 1))
    d.rect(screen, chimney_color, (x + (100 / 300) * w, y - l - (100 / 400) * l, (30 / 300) * w, (90 / 400) * l + 1))


def set_start_environment():
    d.rect(screen, (128, 128, 128), (0, 0, 650, 300), 0)
    d.rect(screen, (15, 15, 15), (0, 300, 650, 450), 0)
    moon()



def ghost(x, y, s, k=1, r=1):
    d.circle(s, (255, 255, 255), (x, y), 25 * k)
    d.circle(s, (25, 150, 255), (x - r * 10 * k, y - 9 * k), 5 * k)
    d.circle(s, (25, 150, 255), (x + r * 8 * k, y - 9 * k), 5 * k)
    d.circle(s, (0, 0, 0), (x - r * 11 * k, y - 9 * k), 2 * k)
    d.circle(s, (0, 0, 0), (x + r * 7 * k, y - 9 * k), 2 * k)


    a = []  # list of points
    b = []  # list that helps me create right range
    for i in range(35):
        a.append((x - 2 * i * k, y + 0.1 * i * i * k))
    for i in range(70):
        a.append((x - 69 * k + i * k, y + 122 * k - 15 * k * m.sin(3.14 * i / 70)))
    for i in range(70):
        a.append((x + i * k, y + 122 * k + 15 * k * m.sin(3.14 * i / 70)))
    for i in range(35):
        b.append(35 - i)
    for i in b:
        a.append((x + 2 * i * k, y + 0.1 * i * i * k))
    d.polygon(s, 'WHITE', a)

def draw():
    set_start_environment()
    house(50, 560, 300, 400)
    chimney1(50, 560, 300, 400)
    chimney2(50, 560, 300, 400)
    ghost(500, 500, screen)
    clouds_r()
    #eyes()

draw()
shar()


pygame.display.update()

#while not finished:
    #clock.tick(FPS)
    #for event in pygame.event.get():
       # if event.type == pygame.QUIT:
        #    finished = True

pygame.quit()