from Real_Classes import *

# а вот тут начинаются приколы - это классы, отвечающие за нормальную реализацию взаимодействия и отрисовки


class GameLogic:
    def __init__(self, *gun):
        """
        Инициализирует обработчик взаимодействий
        :param gun: пушечки, которые изначально инициализированы
        self.guns - лист из ссылок на пушки
        self.balls - лист из ссылок на шарики (по идее можно запихнуть в сам класс пушки
                                                и общаться соответвующим образом)
        self.targets - лист из ссылок на мишени
        self.amount_of_all_balls - количество шариков (по идее можно запихнуть в сам класс пушки
                                                        и общаться соответвующим образом)
        self.score - счёт игры для данного уровня
        """
        self.guns = [*gun]
        self.balls = []
        self.targets = []
        self.amount_of_all_balls = 0
        self.score = 0

    def append_guns(self, *guns):
        """
        Добавить пушки для обработки
        """
        self.guns.append(*guns)

    def append_balls(self, *balls):
        """
        Добавить шарики для обработки
        """
        self.balls.append(*balls)

    def append_targets(self, *targets):
        """
        Добавить мишени для обработки
        """
        for i in range(len(targets)):
            self.targets.append(targets[i])

    def append(self, gun=None, ball=None, target=None):
        """
        То, что дергаем для заполнения из вызывающего кода
        :param gun: пушки
        :param ball: шарики
        :param target: мишени
        """
        if gun:
            self.append_guns(gun)
        if ball:
            self.append_balls(ball)
        if target:
            self.append_targets(target)

    def check_updates(self):
        """
        Обновляет массивы ссылок другие поля (тем самым решает, что обрабатывать, а что нет (по полю - is_alive))
        """
        new_targets = []  # запихиваем живие мишеньки для обновления массива
        deleted_targets = []  # запихиваем убитые мишеньки для подсчёта очков
        for figure in self.targets:
            if figure.is_alive:
                new_targets.append(figure)
            if not figure.is_alive:
                deleted_targets.append(figure)
        for figure in deleted_targets:
            self.score += figure.points
        self.targets = new_targets

        new_balls = []  # запихиваем шарики для обновления массива
        for figure in self.balls:
            if figure.is_alive:
                new_balls.append(figure)
        self.balls = new_balls

        new_guns = []  # запихиваем пушки для обновления массива
        for figure in self.guns:
            if figure.is_alive:
                new_guns.append(figure)
        self.guns = new_guns

    def update_game_procces(self, time):
        """"
        Функция обрабатывает взаимодействия между классами в игре, обробатыает взаимодействия (если они случились)
        и соответвующе меняет параметры объектов
        :param time: время игры
        :return: True, если игра закончилась (мишеней больше нет) и False в противном случае
                    а также счёт текущего раунда
                    - передача происходит в порядке описания
        """
        for ball in self.balls:  # логическая свзяь для обработки столкновений "шарик - мишень"
            for target in self.targets:
                if ball.hittest(target):
                    target.is_alive = False

        for i in range(len(self.balls)):  # логическая свзяь для обработки столкновений "шарик - шарик"
            for j in range(i, len(self.balls)):
                if j != i:
                    if self.balls[i].hittest(self.balls[j]):
                        self.balls[i].is_alive = False
                        self.balls[j].is_alive = False

        self.check_updates()

        if not self.targets:
            return True, self.score, False
        if time > LEVEL_TIME:
            self.targets = []
            return True, self.score, True
        return False, self.score, False


class DrawMaster:
    def __init__(self, *gun):
        """
        Класс отвечающий за отрисовку всего на свете (тыкает всех в метод update и draw)
        :param gun: пушечки, подгружаемые вначале
        self.massive_of_acting_figures - блин ну я не знаю, наверное это массив_действующих_фигур
        """
        self.massive_of_acting_figures = [*gun]
        self.amount_of_all_balls = 0

    def print_text(self, text, color, position, size):
        """
        Удобное общение с распечаткой текста
        :param text: сообщение
        :param color: его цвет (НЕ ИНДЕКС!!!!)
        :param position: тут ясно
        :param size: тут понятно
        """
        f1 = pygame.font.Font(None, size)
        text1 = f1.render(text, True, color, (255, 255, 255))
        SCREEN.blit(text1, position)

    def append(self, *args):
        """
        Добивление ссылки на объект с массив с данными, которые нужно отрисовывать
        :param args: эти самые объекты
        """
        for figure in args:
            self.massive_of_acting_figures.append(figure)

    def draw_end_level(self):
        """
        Рисует текст, отвечающий концу уровня (все цели уничтожены)
        """
        self.print_text("Цели уничтожены; количество выстрелов: " + str(self.amount_of_all_balls), COLORS[0],
                            (SCREEN_X / 7, SCREEN_Y / 4), 40)

    def draw_end_of_game(self, score):
        """
        Рисует текст, отвечающий концу игры (не успел убить все мишени)
        :param score: счет игры (полный)
        :return: is_end
        """
        self.print_text("Время вышло; получено очков: " + str(score), COLORS[0],
                        (SCREEN_X / 7, SCREEN_Y / 4), 40)

    def draw_remaining_time(self, time):
        """
        Отображает оставшееся время раунда
        :param time: текущее время игры
        """
        self.print_text("Оставшееся время: " + str(int(int(LEVEL_TIME - time)/100)/10), 'BLACK', (20, 40), 20)
        self.print_text("секунд", 'BLACK', (200, 40), 20)

    def draw_score(self, scor):
        """
        Вывод счёта на экран
        :param scor: счёт
        :return:
        """
        self.print_text("Счёт: " + str(scor), 'BLACK', (20, 20), 20)

    def check_updates(self):
        """
        Обновляет massive_of_acting_figures
        Грубо говоря - это функция для обновления количества элементов, участвующих в отрисовке
        """
        new_massive = []
        for figure in self.massive_of_acting_figures:
            if figure.is_alive:
                new_massive.append(figure)
        self.massive_of_acting_figures = new_massive

    def draw(self, time, score):
        """
        НЕСТАНДАРТНЫЙ draw
        Запинамет отрисовкой всех элементов
        Тыкает все нужные объекты по ссылке в их методы update и draw
        :param time: время игры
        :param score: счёт, для его отрисовки
        """
        for figure in self.massive_of_acting_figures:
            figure.update(time)
            figure.draw()
            self.check_updates()
        self.draw_score(score)
