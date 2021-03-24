import pygame.draw as draw
import math
from random import randint
from CONSTANTS import *


class Ball:
    def __init__(self, x, y, born_time=0):
        """
        Шарик - это по сути пулька, которую испускает пушка при стрельбе
        :param x: х координата позиции, на которой происходит появление
        :param y: у координата позиции, на которой происходит появление
        :param born_time: время, в которое шарик появился на экрене
        self.born_time - вермя рождения шарика (когда появился на поле)
        self.time_of_live - время жизни шарика
        self.r  - радиус шарика
        self.vx - скорость шарика по оси х
        self.vy - скорость по оси у (нужно помнить, что она идет в обратном направлении)
        self.color - индекс цвета в массиве COLORS
        self.is_alive - живой или нет
        self.on_the_floor - находится ли на полу (нижняя часть экрана;
        проверка происходит по типу "если коснулся и скорость маленькая => True")
        """
        self.born_time = born_time
        self.time_of_live = TIME_BALLLIFE  # milliseconds
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = randint(1, 5)
        self.is_alive = True
        self.on_the_floor = False

    def draw(self):
        """
        Определяет КАК будет отрисовываться шарик
        """
        draw.circle(SCREEN, COLORS[self.color], (self.x, self.y), self.r, width=7)

    def check_alive(self, time):
        """
        Проверяет, не закончилось ли время жизни у шарика
        :param time: текущеее время
        """
        if time - self.born_time >= self.time_of_live:
            self.is_alive = False

    def move(self, time):
        """
        Стандартный move (см docs.txt)
        :param time: текущее время (планируется привязка к реальному времени, пока она есть, но сомнительная)
        - не используется
        """

        if self.x >= SCREEN_X - self.r:
            if math.fabs(self.vx) < 4:
                self.vx = 0
            self.x = SCREEN_X - self.r
            self.vx = -0.5 * self.vx
            self.x += self.vx

        if self.x <= self.r:
            if math.fabs(self.vx) < 4:
                self.vx = 0
            self.x = self.r
            self.vx = -0.5 * self.vx
            self.x += self.vx

        if self.y >= SCREEN_Y - self.r:
            if math.fabs(self.vy) < 4:
                self.vy = 0
                self.on_the_floor = True
            self.y = SCREEN_Y - self.r
            self.vy = -0.5 * self.vy
            self.y -= self.vy

        if self.y <= self.r:
            self.y = self.r
            self.vy = -0.5 * self.vy
            self.y -= self.vy

        if not self.on_the_floor:
            self.vy += FREE_FALL_ACCEL
        else:
            if math.fabs(self.vx):
                self.vx = (math.fabs(self.vx)/self.vx) * (math.fabs(self.vx) - K_OF_TRENIE * K_UP_SPEED)
            if self.vx ** 2 + self.vy ** 2 < 2:
                self.vx = 0
                self.vy = 0

        self.x += self.vx
        self.y -= self.vy

    def hittest(self, obj):
        """
        Проверка, столкнулся ли шарик с объектом obj. Для этого объекта ДОЛЖНЫ БЫТЬ опредены х, у и r
        К сожалению, пока только реализованы столкновения с круглыми объектами
        :param obj:
        :return: True - если столкнулся и False в противном случае
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False

    def update(self, time):
        """
        Стандартный апдейт (см docs.txt)
        :param time: текущее время
        """
        self.move(time)
        self.check_alive(time)


class Gun:
    def __init__(self, x, y):
        """
        Инициализирует параметры пушечки
        :param x: х координата положения относительно которое вращаемся
        :param y: у координата положения относительно которое вращаемся
        self.f2_power - начальная сила пушки (см. CONSTANTS.py)
        self.f2_on - находится ли в атаке (булевая: значит либо 0, либо 1)
        self.color - индекс цвета в массиве COLOR_OF_GUNS (см. CONSTANTS.py)
        self.angle - угол поворота
        self.start_pos - tuple отвечающий за точку, относительно которой вращаемся
        self.end_pos -  tuple отвечающий за конечую точку дула (для отрисовки и запуска шариков)
        self.is_alive - жив или нет
        """
        self.f2_power = START_POWER_OF_GUNS
        self.f2_on = 0
        self.color = 0
        self.angle = 0
        self.start_pos = (x, y)
        self.end_pos = (self.f2_power * math.cos(self.angle), self.f2_power * math.sin(self.angle))
        self.is_alive = True

    def draw(self):
        draw.line(SCREEN, COLOR_OF_GUN[self.color], self.start_pos, self.end_pos, width=10)
        draw.circle(SCREEN, COLORS[4], self.start_pos, 15)
        draw.circle(SCREEN, COLOR_OF_GUN[self.color], self.end_pos, 7)

    def fire_start(self):
        """
        Ставит пушке состояние "заряжается" (удлиннение дула и тд и тп; вызывается после обработки нажатой кнопки)
        """
        self.f2_on = 1
        self.color = 1

    def fire_end(self, time):
        """
        Обработка окончания атаки (вызывается после обработки события отжатой кнопки)
        :param time: текущее время в игре (ставится запущенному шарику)
        :return:
        """
        new_ball = Ball(self.end_pos[0], self.end_pos[1], born_time=time)
        new_ball.vx = (self.f2_power*K_UP_SPEED) * math.cos(self.angle)
        new_ball.vy = - (self.f2_power*K_UP_SPEED) * math.sin(self.angle)
        self.f2_on = 0
        self.f2_power = START_POWER_OF_GUNS
        self.color = 0
        return new_ball

    def targetting(self, event: pygame.event = None):
        """
        Прицеливание. Зависит от положения мыши.
        В переменную event передаётся событие "курсор подвигался" или ничего
        так как эта функция должна корректно рабоать даже если событий не происходит
        """
        if event:
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN \
                    or event.type == pygame.MOUSEBUTTONUP:
                if self.f2_on:
                    self.color = 1
                else:
                    self.color = 0
                if self.start_pos[0] != event.pos[0]:
                    self.angle = \
                        (-1) * math.atan((event.pos[1] - self.start_pos[1]) / (self.start_pos[0] - event.pos[0]))
                if event.pos[0] < self.start_pos[0]:
                    self.angle += math.pi
                self.end_pos = (self.f2_power * math.cos(self.angle) + self.start_pos[0],
                                self.f2_power * math.sin(self.angle) + self.start_pos[1])
        else:
            self.end_pos = (self.f2_power * math.cos(self.angle) + self.start_pos[0],
                            self.f2_power * math.sin(self.angle) + self.start_pos[1])

    def power_up(self):
        """
        Занимается удлиннением дула пушки, если она в состоянии "заряжается"
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 2
            else:
                self.f2_power = 100
        else:
            self.f2_power = START_POWER_OF_GUNS

    def event_loop(self, event, drawclass, gamelogicclass, time, counting_balls=True):
        """
        Сердце работы пушки - обработчик событий
        :param event: событие из pygame
        :param drawclass: (ссылка на) класс, отвечающий за отрисовку всего на свете
        :param gamelogicclass: (ссылка на) класс, отвечающий за обновления
                                состояния всего на свете и взаимодействие мд различными классами
        :param time: реальное время в игре
        :param counting_balls: булевая переменная по умолчанию, логически значащая "считать выпущенные щарики или нет"
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.fire_start()
        if event.type == pygame.MOUSEBUTTONUP:
            link_to_new_ball = self.fire_end(time)
            drawclass.append(link_to_new_ball)
            gamelogicclass.append(ball=link_to_new_ball)
            if counting_balls:
                drawclass.amount_of_all_balls += 1
        self.targetting(event)

    def update(self, time):
        """
        Стандартный апдейт (см docs.txt)
        :param time: текущее время
        """
        self.power_up()
        self.targetting()


class Target:
    def __init__(self, number):
        """
        Инициализируем данные для мишени
        :param number: отладочная переменная; позволяет делать вывод в консольку в читабельном виде
        self.x = х координата положения спавна
        self.y = у координата положения спавна
        self.r = радиус мишени
        self.color - ЦВЕТ (НЕ ИНДЕКС ЦВЕТА!!!!!)
        self.is_alive - жив или нет
        self.enum - отладочная переменная; позволяет делать вывод в консольку в читабельном виде
        self.points - очки, выдаваемые за изничижение мишени
        """
        self.x = randint(200, SCREEN_X)
        self.y = randint(20, SCREEN_Y - 200)
        self.r = randint(7, 50)
        self.color = 'RED'
        self.is_alive = True
        self.enum = number
        if self.r > 20:
            self.points = 1
        else:
            self.points = 2

    def __str__(self):
        """
        Всё ради удобста отладки
        """
        return "{ T: " + str(self.enum) + " }"

    def draw(self):
        """
        Стандартный draw
        """
        draw.circle(SCREEN, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        Стандартный move (см docs.txt)
        """
        self.x += randint(-2, 2)
        self.y += randint(-2, 2)
        # сделатьченитьадекватное

    def update(self, time):
        """
        Cтандартный апдейт (см docs.txt)
        :param time: текущее время
        """
        # self.move()
        pass
