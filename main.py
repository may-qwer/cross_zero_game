import pygame

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
cells_pos = []


class Player:
    def __init__(self, mouse_pos, window, cells_pos):
        self.cells_pos = cells_pos
        self.mouse_pos = mouse_pos
        self.window = window
        self.game_end = False

    def create_cross(self):
        for cell in self.cells_pos:
            if cell[0][0] <= self.mouse_pos[0] and cell[1][0] >= self.mouse_pos[0] and cell[0][1] <= self.mouse_pos[1] and cell[1][1] >= self.mouse_pos[1]:
                pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 40, cell[0][1] + 40), (cell[1][0] - 40, cell[1][1] - 40), 6)
                pygame.draw.line(self.window, [57, 50, 255], (cell[0][0] + 160, cell[0][1] + 40), (cell[1][0] - 160, cell[1][1] - 40), 6)
                self.cells_pos.remove(cell)

    def end_game_screen(self):
        if len(self.cells_pos) == 0:
            self.game_end = True
            self.window.fill((20, 20, 20))
            self.window.blit(pygame.font.Font(None, 80).render('Game end!', True, (26, 255, 255)), (150, 220))
            self.window.blit(pygame.font.Font(None, 40).render('Press SPACE to restart. Press ESC to quit.', True, (19, 137, 155)), (30, 290))


def main():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe Game')
    clock = pygame.time.Clock()
    pygame.font.init()
    window.fill((0, 0, 0))
    cells_pos = CELL_POS
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
                    cells_pos = CELL_POS
                    main()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player = Player(mouse_pos, window, cells_pos)
                player.create_cross()
                player.end_game_screen()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()