from Draw_and_Logic import *


def pause(score):
    """
    Функция, обрабатывающая паузу (когда все мишеньки убиты и есть некоторое время между раундами)
    :param score: счёт для отрисовки
    :return:
    """
    pause_tick = 1000 / FPS
    pause_time = 0

    while pause_time < 3000:
        pause_time += pause_tick
        clock.tick(FPS)
        for pause_event in pygame.event.get():
            GUN1.event_loop(pause_event, draw_master, game_logic, pause_time, counting_balls=0)

        SCREEN.fill('WHITE')

        draw_master.draw(pause_time, score, True)
        game_logic.update_game_procces(pause_time)

        pygame.display.update()


pygame.init()
finished = False  # был ли нажат крестик или нет
global_score = 0  # полный счёт игры

# Главный цикл игры
while not finished:
    clock = pygame.time.Clock()
    end_of_level = False

    score_of_one_level = 0  # счёт конктреного уровня

    GUN1 = Gun(50, 500)

    game_logic = GameLogic(GUN1)
    draw_master = DrawMaster(GUN1)

    one_tick = 1000 / FPS  # количество миллисекунд на один тик часов
    game_time = 0  # полное время в миллисекундах

    # создаём мишеньки
    for i in range(AM_OF_TARGETS):
        t = Target(i)
        game_logic.append_targets(t)
        draw_master.append(t)

    # основный цикл уровня
    while not end_of_level:
        game_time += one_tick
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                end_of_level = True
            GUN1.event_loop(event, draw_master, game_logic, game_time)

        # проверка на нажите крестика (работает, так как значение False может быть выставлено по завершении игры только
        # ПОСЛЕ проверки этого условия
        if end_of_level:
            break
        # и если не нажат крестик, то продолжаем

        SCREEN.fill('WHITE')
        draw_master.draw(game_time, score_of_one_level + global_score)
        end_of_level, score_of_one_level = game_logic.update_game_procces(game_time)
        pygame.display.update()
        if end_of_level:
            global_score += score_of_one_level
            pause(global_score)

pygame.quit()
