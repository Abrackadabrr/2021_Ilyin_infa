import pygame
import pygame.draw as draw
from random import randint

pygame.init()

FPS = 30
SCREEN_X = 1200
SCREEN_Y = 750

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCORE = 0
AM_OF_FIGS = 10  # количество движущихся фигур
name = "Аноним"  # начальное стандартное имя


def new_figure_data(s="rand"):
    """
    Генерирует новую фигуру в рандомном месте
    :param s: строка, если "ball" - то генерит шарик; "sq" - генерит квадрат;
                что-то ещё или совсем ничего - рандом фгиура
    :return вся информацию о фигуре
    """
    if s == "ball":
        type = 1
    elif s == "sq":
        type = 2
    else:
        type = randint(1, 2)
    x = randint(100, SCREEN_X - 100)
    y = randint(100, SCREEN_Y - 100)
    size = randint(10, 100)
    color = randint(0, 5)
    x_vel = pm() * randint(1, 10)
    y_vel = pm() * randint(1, 10)
    data_of_ball = [type, x, y, size, color, x_vel, y_vel]
    return data_of_ball


def pm():
    """
    :return: + или -
    """
    if randint(1, 3) == 1:
        return -1
    else:
        return 1


def draw_figure(type, x, y, size, color, x_vel, y_vel):
    """
    Рисует фиугрку
    :param type: тип
    :param x: очевидно
    :param y: очевидно
    :param size: радиус для кружо4ка или сторона квадрата
    :param color: цвет (номер в массиве COLORS)
    :param x_vel: скорость по х
    :param y_vel: скорость по у
    :return: ничево
    """
    if type == 2:
        draw.rect(screen, COLORS[color], (x, y, size, size))
    if type == 1:
        draw.circle(screen, COLORS[color], (x, y), size)


def click_check(figures, event):
    """
    Обрабатывает клики и пишет в переменную счета
    :param figures: лист фигурок
    :param event: событие
    :return: булевая переменна "есть попадание или нет"
    """
    global SCORE
    click = False
    for i in range(AM_OF_FIGS):
        if figures[i][0] == 1:
            if ((event.pos[0] - figures[i][1]) ** 2 + (event.pos[1] - figures[i][2]) ** 2) <= (figures[i][3]) ** 2:
                pygame.display.update()
                SCORE += figures[i][0]
                figures[i] = new_figure_data("rand")
                click = True
        if figures[i][0] == 2:
            if ((event.pos[0] - figures[i][1]) < figures[i][3]) and (
                    abs(event.pos[1] - figures[i][2]) < figures[i][3]) and \
                    (event.pos[0] - figures[i][1]) > 0 and (event.pos[1] - figures[i][2]):
                pygame.display.update()
                SCORE += figures[i][0]
                figures[i] = new_figure_data("rand")
                click = True
    return click


def update_fgures(figures):
    """
    Обновляет данные фигурок
    :param figures: лист фигурок
    :return: ни4ево
    """
    for data in figures:
        if data[0] == 1:
            data[1] += data[5]
            data[2] += data[6]
            if data[1] >= SCREEN_X - data[3]:
                data[5] *= -1
                data[6] = pm() * randint(1, 10)
            if data[1] <= data[3]:
                data[5] *= -1
                data[6] = pm() * randint(1, 10)
            if data[2] >= SCREEN_Y - data[3]:
                data[6] *= -1
                data[5] = pm() * randint(1, 10)
            if data[2] <= data[3]:
                data[6] *= -1
                data[5] = pm() * randint(1, 10)
            draw_figure(*data)

        elif data[0] == 2:

            if data[1] >= SCREEN_X - data[3]:
                data[3] = randint(5, data[3])
                data[5] *= -1
                data[6] = pm() * randint(1, 10)
                data[1] -= 10
            if data[1] <= 0:
                data[3] = randint(5, data[3])
                data[5] *= -1
                data[6] = pm() * randint(1, 10)
                data[1] += 10
            if data[2] >= SCREEN_Y - data[3]:
                data[3] = randint(5, data[3])
                data[6] *= -1
                data[5] = pm() * randint(1, 10)
                data[2] -= 10
            if data[2] <= 0:
                data[3] = randint(5, data[3])
                data[6] *= -1
                data[5] = pm() * randint(1, 10)
                data[2] += 10

            data[1] += data[5]
            data[2] += data[6]
            draw_figure(*data)


def update_screen(figures):
    """
    Обновляет целиком экран
    :param figures: лист фигурок
    :return: ни4его
    """
    update_fgures(figures)
    score_text = pygame.font.SysFont('None', 40)
    score_text = score_text.render(name + ": Счёт: " + str(SCORE), True, COLORS[2])
    screen.blit(score_text, (SCREEN_X // 40, SCREEN_Y // 40))
    pygame.display.update()


def set_figures():
    """
    Создает массив фигурок по заданному числу "AM_OF_FIGURES"
    :return: этот массив
    """
    fig = []
    for i in range(AM_OF_FIGS):
        fig.append(new_figure_data("rand"))
    return fig


def print_text(text, color, position, size, screen):
    """
    Удобное общение с распечаткой текста
    :param text: сообщение
    :param color: его цвет (НЕ ИНДЕКС!!!!)
    :param position: тут ясно
    :param size: тут понятно
    :param screen: экран на котором отрисовывается всё
    :return:
    """
    f1 = pygame.font.Font(None, size)
    text1 = f1.render(text, True,
                      color, BLACK)

    screen.blit(text1, position)


def check_name(data):
    """
    Проверяет, если ли введённое имя в уже имеющемся списки результатов (то есть нельзя такое же)
    :param data: массив строк, считываемый из файла
    :return: цвет, которым нужно выделить строчку с именем на экране (красный/зеленый)
    """
    global name
    is_shadow = False
    name = name + '\n'
    for line in data:
        if str(name) == str(line[1]):
            is_shadow = True
    name = name[:-1]
    if is_shadow:
        return 'RED'
    else:
        return 'GREEN'


def menu(is_enter_name, screen):
    """
    Вызов менюшки
    :param is_enter_name: "введено ли уже имя?"
    :param screen: экран куда отрисовать менюшку
    :return: булевая переменная "вышел ли пользователь из игры" (далее - если да, то валим из приложения)
    """
    global name
    finish = False
    data = read_from_file()
    while not is_enter_name:
        color_of_name = check_name(data)
        print_text("Enter your name: " + name, color_of_name, (100, 300), 70, screen)
        print_text("Press Enter to start", GREEN, (150, 400), 70, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
                is_enter_name = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if color_of_name != 'RED':
                        is_enter_name = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_q:
                    finish = True
                    is_enter_name = True
                else:
                    name += event.unicode
        pygame.display.update()
        screen.fill(BLACK)
    return finish


def write_to_file_new_result(data):
    """
    Запись результата в файл
    :param data: строчку с ним в формате "результат|имя"
    :return: ничиво
    """
    f = open('scores.txt', 'a')
    f.write(data)
    f.close()


def read_from_file():
    """
    Считать из файла
    :return: лист строк с данными о прошлых результатах
    """
    f = open('scores.txt', 'r')
    data = [line.split('|') for line in f]
    return data


def write_top(data):
    """
    Обновить топ (сортировка по полю результат)
    :param data: результат
    :return: лист строк с описанием результатов в порядке возрастания
    """
    f = open('scores.txt', 'w')
    data.sort(key=lambda a: int(a[0]), reverse=True)
    for lines in data:
        line = str(lines[0]) + "|" + lines[1]
        write_to_file_new_result(line)
    return data


clock = pygame.time.Clock()
game_time = -1
figures = set_figures()
MAKE_TRASH = False  # попробуйте поставить True...

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.SRCALPHA)
is_menu_end = False

finished = menu(is_menu_end, screen)

# главный цикл игры
while not finished:
    game_time += 1
    clock.tick(FPS)

    update_screen(figures)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if MAKE_TRASH:
                figures.append(new_figure_data("rand"))
                AM_OF_FIGS += 1
            else:
                click_check(figures, event)

    screen.fill(BLACK)

pygame.quit()

# запись в файлик
data = str(SCORE) + "|" + name + '\n'
write_to_file_new_result(data)
data = read_from_file()  # список списков со строками с данными
write_top(data)
