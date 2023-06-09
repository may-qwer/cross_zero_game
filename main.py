import pygame
import random
import time

LINE_COORD = [[[200, 20], [200, 580]],
              [[400, 20], [400, 580]],
              [[20, 200], [580, 200]],
              [[20, 400], [580, 400]]]
CIRCLES_COORD = [[200, 200],
                 [200, 400],
                 [400, 200],
                 [400, 400]]
CELL_POS = [[[0, 0], [200, 200]],
            [[202, 0], [400, 200]],
            [[402, 0], [600, 200]],
            [[0, 202], [200, 400]],
            [[202, 202], [400, 400]],
            [[402, 202], [600, 400]],
            [[0, 402], [200, 600]],
            [[202, 402], [400, 600]],
            [[402, 402], [600, 600]]]
WIN_COMBINATIONS = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]


class AI:
    def __init__(self, list_for_ai, win_combination):
        self.list_for_ai = list_for_ai
        self.win_matrix = []
        for comb in win_combination:
            self.win_matrix.append(comb)

    def list_to_matrix(self):
        return [[self.list_for_ai[0], self.list_for_ai[1], self.list_for_ai[2]], [self.list_for_ai[3], self.list_for_ai[4], self.list_for_ai[5]], [self.list_for_ai[6], self.list_for_ai[7], self.list_for_ai[8]]]

    def replace_cross_or_zero_in_win_comb(self, sum_zero, sum_cross):
        choose_cell = ''
        for comb in self.win_matrix:
            num_zero = 0
            num_cross = 0
            for j in range(0, 3):
                if self.list_for_ai[comb[j]] == 'cross':
                    num_cross += 1
                elif self.list_for_ai[comb[j]] == 'zero':
                    num_zero += 1

            if num_zero == sum_zero and num_cross == sum_cross:
                for j in range(0, 3):
                    if self.list_for_ai[comb[j]] != 'cross' and self.list_for_ai[comb[j]] != 'zero':
                        choose_cell = self.list_for_ai[comb[j]]

        return choose_cell

    def make_choose(self):
        choose_cell = ''

        # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
        choose_cell = self.replace_cross_or_zero_in_win_comb(2, 0)

        # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if choose_cell == '':
            choose_cell = self.replace_cross_or_zero_in_win_comb(0, 2)

        # 3) если 1 фигура своя и 0 чужих - ставим
        if choose_cell == '':
            choose_cell = self.replace_cross_or_zero_in_win_comb(1, 0)

        # 4) центр пуст, то занимаем центр
        if choose_cell == '':
            if self.list_for_ai[4] != 'cross' and self.list_for_ai[4] != 'zero':
                choose_cell = 4

        # 5) если цент занят, то занимаем любую ячейку
        if choose_cell == '':
            if self.list_for_ai[0] != 'cross' and self.list_for_ai[0] != 'zero':
                choose_cell = 0

        if choose_cell == '':
            choose_random = True
            while choose_random:
                choose_cell = random.choice(self.list_for_ai)
                if type(choose_cell) == int:
                    choose_random = False

        return choose_cell


class Player:
    def __init__(self, mouse_pos, window, cells_pos, list_for_ai):
        self.cells_pos = cells_pos
        self.list_for_ai = list_for_ai
        self.matrix_for_ai = [[], [], []]
        self.mouse_pos = mouse_pos
        self.window = window
        self.go_cross = True
        self.go_zero = False
        self.game_end = False
        self.cross_num_of_cells_that_are_left = 0
        self.zero_num_of_cells_that_are_left = 0



    def create_cross(self):
        if self.go_cross:
            for cell in self.cells_pos:
                if cell[0][0] <= self.mouse_pos[0] and cell[1][0] >= self.mouse_pos[0] and cell[0][1] <= self.mouse_pos[1] and cell[1][1] >= self.mouse_pos[1]:
                    pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 40, cell[0][1] + 40), (cell[1][0] - 40, cell[1][1] - 40), 6)
                    pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 160, cell[0][1] + 40), (cell[1][0] - 160, cell[1][1] - 40), 6)
                    global CELL_POS
                    self.cross_num_of_cells_that_are_left = CELL_POS.index(cell)
                    self.list_for_ai.remove(self.cross_num_of_cells_that_are_left)
                    self.list_for_ai.insert(self.cross_num_of_cells_that_are_left, 'cross')
                    self.cells_pos.remove(cell)
                    self.go_cross = False
                    self.go_zero = True

    def create_zero(self):
        if len(self.cells_pos) != 0 and self.go_zero:
            global CELL_POS
            ai = AI(self.list_for_ai, WIN_COMBINATIONS)
            choose_cell_index = ai.make_choose()
            print(choose_cell_index)
            print(self.cells_pos)
            choose_cell = CELL_POS[choose_cell_index]
            pygame.draw.circle(self.window, [255, 88, 27], ((choose_cell[0][0]+choose_cell[1][0])/2, (choose_cell[0][1]+choose_cell[1][1])/2), 90, 6)
            self.zero_num_of_cells_that_are_left = CELL_POS.index(choose_cell)
            self.list_for_ai.remove(self.zero_num_of_cells_that_are_left)
            self.list_for_ai.insert(self.zero_num_of_cells_that_are_left, 'zero')
            self.cells_pos.remove(choose_cell)
            self.go_zero = False
            self.go_cross = True

    def end_game_screen(self):
        if len(self.cells_pos) == 0:
            self.window.fill((20, 20, 20))
            self.window.blit(pygame.font.Font(None, 80).render('Game end!', True, (26, 255, 255)), (150, 220))
            self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, (19, 137, 155)), (30, 290))
            self.game_end = True

    def cross_win_screen(self):
        self.window.fill((20, 20, 20))
        self.window.blit(pygame.font.Font(None, 80).render('You WIN!', True, [57, 50, 255]), (170, 220))
        self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, [36, 31, 183]), (30, 290))
        self.cells_pos = []

    def zero_win_screen(self):
        self.window.fill((20, 20, 20))
        self.window.blit(pygame.font.Font(None, 80).render('You LOSS!', True, [255, 88, 27]), (150, 220))
        self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, [193, 71, 27]), (30, 290))
        self.cells_pos = []



def main():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe Game')
    clock = pygame.time.Clock()
    pygame.font.init()
    window.fill((0, 0, 0))
    cells_pos = []
    list_for_cross_win = []
    list_for_zero_win = []
    list_for_ai = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for cell in CELL_POS:
        cells_pos.append(cell)
    for line in LINE_COORD:
        pygame.draw.line(window, (255, 255, 255), line[0], line[1], 2)
    for circle in CIRCLES_COORD:
        pygame.draw.circle(window, [0, 0, 0], circle, 20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player = Player(mouse_pos, window, cells_pos, list_for_ai)
                player.end_game_screen()
                if not player.game_end:
                    for combination in WIN_COMBINATIONS:
                        if combination[0] in list_for_zero_win and combination[1] in list_for_zero_win and combination[2] in list_for_zero_win:
                            player.zero_win_screen()
                            break
                    for combination in WIN_COMBINATIONS:
                        if combination[0] in list_for_cross_win and combination[1] in list_for_cross_win and combination[2] in list_for_cross_win:
                            player.cross_win_screen()
                            break
                    if player.go_cross or player.go_zero:
                        player.create_cross()
                        player.create_zero()
                    list_for_cross_win.append(player.cross_num_of_cells_that_are_left)
                    list_for_cross_win.sort()
                    list_for_zero_win.append(player.zero_num_of_cells_that_are_left)
                    list_for_zero_win.sort()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()