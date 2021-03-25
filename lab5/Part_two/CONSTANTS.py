import pygame

# в данном файле описаны константы, через которые мы общаемся с настройками нашей игры

FPS = 60
# время жизни мячиков, которые пуляет пушка
TIME_BALLLIFE = 6000
# Это коэффициент, который преобразует силу пушки в скорость шарика (обратно пропорционален FPS)
# (попытка привязки скорости шариков к реальному времени).
K_UP_SPEED = 30/FPS
# Количество мишеней на раунд
AM_OF_TARGETS = 20
# Ширина и высота игрового поля (не стоит менять)
SCREEN_X = 800
SCREEN_Y = 600
# Далее - константы цветов
RED = 'RED'
BLUE = 'BLUE'
YELLOW = 'YELLOW'
GREEN = 'GREEN'
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
# Массив с ними
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Цвета пушки: позиция 0 - не заряжена, позиция 1 - заряжена
COLOR_OF_GUN = ['BLACK', 'RED']
# Создание рабочей области
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
# "Ускорение свободного падения"
FREE_FALL_ACCEL = -2
# Минимальная сила пушки (даёт минимальную скорость снаряду при обычном клике)
START_POWER_OF_GUNS = 30
# Коэффициент трения для нижней границы экрана (фича для движения шариков)
K_OF_TRENIE = 0.03
# вермя одного раунда
if AM_OF_TARGETS > 5:
    LEVEL_TIME = 2000 * AM_OF_TARGETS
if AM_OF_TARGETS > 10:
    LEVEL_TIME = 1000*AM_OF_TARGETS
if AM_OF_TARGETS < 5:
    LEVEL_TIME = 3000*AM_OF_TARGETS
