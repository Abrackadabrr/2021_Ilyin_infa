from Draw_and_Logic import *


class Game:
    def __init__(self):
        self.score = 0
        self.amount_of_targets = AM_OF_TARGETS
        self.am_of_modified_targets = AM_OF_MODI_TARCS
        self.amount_of_guns = AM_OF_GUNS
        self.number_of_level = 1
        self.draw_class = DrawMaster()
        self.logic_class = GameLogic()
        self.clock = pygame.time.Clock()
        self.one_tick = 1000 / FPS  # количество миллисекунд на один тик часов
        self.game_time = 0
        self.is_level_ended = False
        self.is_game_ended = False
        self.followers_from_last_level = []

    def create_game_obiects(self):
        # создаём мишеньки
        if self.number_of_level > NUM_OF_LEVEL_WHEN_MODI_TARGS_CAME:
            for i in range(self.amount_of_targets - self.am_of_modified_targets):
                t = Target(i)
                self.logic_class.append_targets(t)
                self.draw_class.append(t)
            for i in range(self.am_of_modified_targets):
                t = ModTargets(i)
                self.logic_class.append_targets(t)
                self.draw_class.append(t)
        else:
            for i in range(self.amount_of_targets):
                t = Target(i)
                self.logic_class.append_targets(t)
                self.draw_class.append(t)

        # пушечки
        for i in range(self.amount_of_guns):
            gun1 = Gun(50 + i * 500, 500)
            self.draw_class.append(gun1)
            self.logic_class.append(gun=gun1)

        # забираем прошлых последователей
        for i in range(len(self.followers_from_last_level)):
            self.draw_class.append(self.followers_from_last_level[i])
            self.logic_class.append(follower=self.followers_from_last_level[i])

    def start(self):
        self.amount_of_targets += 1
        self.draw_class.__init__()
        self.logic_class.__init__()

        self.is_level_ended = False
        self.is_game_ended = False

        self.game_time = 0

        self.create_game_obiects()

    def level_run(self):
        self.start()
        print(*self.draw_class.massive_of_acting_figures)
        print(*self.logic_class.targets)
        score = 0
        while not self.is_level_ended:
            self.game_time += self.one_tick
            self.clock.tick(FPS)

            self.event_loop()

            if self.is_level_ended:
                return self.is_game_ended

            SCREEN.fill('WHITE')

            self.draw_class.draw(self.game_time, score + self.score, self.number_of_level)
            self.draw_class.draw_remaining_time(self.game_time)
            self.draw_class.draw_number_of_level(self.number_of_level)
            self.is_level_ended, score, self.is_game_ended = self.logic_class.update_game_procces(self.game_time)
            pygame.display.update()

            if self.is_level_ended and not self.is_game_ended:
                self.score += score
                self.number_of_level += 1
                self.pause(self.score)
                self.followers_from_last_level = self.logic_class.followers
                return self.is_game_ended
            if self.is_level_ended and self.is_game_ended:
                self.score += score
                self.the_end(self.score)
                return self.is_game_ended

    def pause(self, score):
        pause_tick = 1000 / FPS
        pause_time = 0

        while pause_time < 3000:
            pause_time += pause_tick
            self.clock.tick(FPS)
            for pause_event in pygame.event.get():
                for i in range(len(self.logic_class.guns)):
                    self.logic_class.guns[i].event_loop(pause_event, self.draw_class, self.logic_class, self.game_time,
                                                        counting_balls=0)

            SCREEN.fill('WHITE')

            self.draw_class.draw(self.game_time, score, self.number_of_level)
            self.draw_class.draw_end_level()
            self.logic_class.update_game_procces(pause_time)

            pygame.display.update()

    def the_end(self, score):
        pause_tick = 1000 / FPS
        pause_time = 0

        while pause_time < 3000:
            pause_time += pause_tick
            self.clock.tick(FPS)
            for pause_event in pygame.event.get():
                for i in range(len(self.logic_class.guns)):
                    self.logic_class.guns[i].event_loop(pause_event, self.draw_class, self.logic_class, self.game_time,
                                                        counting_balls=0)

            SCREEN.fill('WHITE')

            self.draw_class.draw(self.game_time, score, self.number_of_level)
            self.draw_class.draw_end_of_game(score)
            self.logic_class.update_game_procces(pause_time)

            pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_ended = True
                self.is_level_ended = True
            for i in range(len(self.logic_class.guns)):
                self.logic_class.guns[i].event_loop(event, self.draw_class, self.logic_class, self.game_time)
        for i in range(len(self.logic_class.targets)):
            self.logic_class.targets[i].time_loop(self.draw_class, self.logic_class, self.game_time)

    def main_loop(self):
        while not self.level_run():
            pass
