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
WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]



class Player:
    def __init__(self, mouse_pos, window, cells_pos):
        self.cells_pos = cells_pos
        self.mouse_pos = mouse_pos
        self.window = window
        self.go_cross = True
        self.go_zero = False
        self.cross_num_of_cells_that_are_left = 0
        self.zero_num_of_cells_that_are_left = 0



    def create_cross(self):
        if self.go_cross:
            for cell in self.cells_pos:
                if cell[0][0] <= self.mouse_pos[0] and cell[1][0] >= self.mouse_pos[0] and cell[0][1] <= self.mouse_pos[1] and cell[1][1] >= self.mouse_pos[1]:
                    pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 40, cell[0][1] + 40), (cell[1][0] - 40, cell[1][1] - 40), 6)
                    pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 160, cell[0][1] + 40), (cell[1][0] - 160, cell[1][1] - 40), 6)
                    global CELL_POS
                    self.cross_num_of_cells_that_are_left = CELL_POS.index(cell)+1
                    self.cells_pos.remove(cell)
                    self.go_cross = False
                    self.go_zero = True

    def create_zero(self):
        if len(self.cells_pos) != 0:
            if self.go_zero:
                choose_cell = random.choice(self.cells_pos)
                pygame.draw.circle(self.window, [255, 88, 27], ((choose_cell[0][0]+choose_cell[1][0])/2, (choose_cell[0][1]+choose_cell[1][1])/2), 90, 6)
                global CELL_POS
                self.zero_num_of_cells_that_are_left = CELL_POS.index(choose_cell) + 1
                self.cells_pos.remove(choose_cell)
                self.go_zero = False
                self.go_cross = True

    def end_game_screen(self):
        if len(self.cells_pos) == 0:
            self.window.fill((20, 20, 20))
            self.window.blit(pygame.font.Font(None, 80).render('Game end!', True, (26, 255, 255)), (150, 220))
            self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, (19, 137, 155)), (30, 290))

    def cross_win_screen(self):
        self.window.blit(pygame.font.Font(None, 80).render('You WIN!', True, [196, 166, 255]), (170, 220))
        self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, [36, 31, 183]), (30, 290))

    def zero_win_screen(self):
        self.window.blit(pygame.font.Font(None, 80).render('You LOSS!', True, [255, 88, 27]), (150, 220))
        self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, [193, 71, 27]), (30, 290))


def main():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe Game')
    clock = pygame.time.Clock()
    pygame.font.init()
    window.fill((0, 0, 0))
    cells_pos = []
    list_for_cross_win = []
    list_for_zero_win = []
    game_end = False
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
                player = Player(mouse_pos, window, cells_pos)
                player.end_game_screen()
                if player.go_cross or player.go_zero and not game_end:
                    player.create_cross()
                    list_for_cross_win.append(player.cross_num_of_cells_that_are_left)
                    list_for_cross_win.sort()
                    for combination in WIN_COMBINATIONS:
                        if combination[0] in list_for_cross_win and combination[1] in list_for_cross_win and combination[2] in list_for_cross_win:
                            player.cross_win_screen()
                            game_end = True
                            break
                    player.create_zero()
                    list_for_zero_win.append(player.zero_num_of_cells_that_are_left)
                    list_for_zero_win.sort()
                    for combination in WIN_COMBINATIONS:
                        if combination[0] in list_for_zero_win and combination[1] in list_for_zero_win and combination[2] in list_for_zero_win:
                            player.zero_win_screen()
                            game_end = True
                            break
                    # list_for_cross_win.append(player.cross_num_of_cells_that_are_left)
                # list_for_cross_win.sort()
                # if not game_end:
                #     for combination in WIN_COMBINATIONS:
                #         if combination[0] in list_for_cross_win and combination[1] in list_for_cross_win and combination[2] in list_for_cross_win:
                #             player.cross_win_screen()
                #             game_end = True
                #             break
                #     list_for_zero_win.append(player.zero_num_of_cells_that_are_left)
                #     list_for_zero_win.sort()
                # if not game_end:
                #     for combination in WIN_COMBINATIONS:
                #         if combination[0] in list_for_zero_win and combination[1] in list_for_zero_win and combination[2] in list_for_zero_win:
                #             player.zero_win_screen()
                #             game_end = True
                #             break
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()