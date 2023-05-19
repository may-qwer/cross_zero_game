import pygame

LINE_COORD = [[[200, 20], [200, 580]],
              [[400, 20], [400, 580]],
              [[20, 200], [580, 200]],
              [[20, 400], [580, 400]]]
CIRCLES_COORD = [[200, 200],
                 [200, 400],
                 [400, 200],
                 [400, 400]]

class Player:
    def __init__(self, mouse_pos):
        # [[firstX, firstY], [lastX, lastY]] firstX < pos_mouse < lastX
        # pos_mouse = (150, 150)

        self.cells_pos = [[[0, 0], [200, 200]],
                                [[202, 0], [400, 200]],
                                [[402, 0], [600, 200]],
                                [[0, 202], [200, 400]],
                                [[202, 202], [400, 400]],
                                [[402, 202], [600, 400]],
                                [[0, 402], [200, 600]],
                                [[202, 402], [400, 600]],
                                [[402, 402], [600, 600]]]
        self.mouse_pos = mouse_pos



    def create_cross(self):
        pass

    def check_cell(self):
        if self.cells_pos[0][0][0] <= self.mouse_pos[0] and self.cells_pos[0][1][0] >= self.mouse_pos[0] and self.cells_pos[0][0][1] <= self.mouse_pos[1] and self.cells_pos[0][1][1] >= self.mouse_pos[1]:
            print('1 cell')
        elif self.cells_pos[1][0][0] <= self.mouse_pos[0] and self.cells_pos[1][1][0] >= self.mouse_pos[0] and self.cells_pos[1][0][1] <= self.mouse_pos[1] and self.cells_pos[1][1][1] >= self.mouse_pos[1]:
            print('2 cell')
        elif self.cells_pos[2][0][0] <= self.mouse_pos[0] and self.cells_pos[2][1][0] >= self.mouse_pos[0] and self.cells_pos[2][0][1] <= self.mouse_pos[1] and self.cells_pos[2][1][1] >= self.mouse_pos[1]:
            print('3 cell')
        elif self.cells_pos[3][0][0] <= self.mouse_pos[0] and self.cells_pos[3][1][0] >= self.mouse_pos[0] and self.cells_pos[3][0][1] <= self.mouse_pos[1] and self.cells_pos[3][1][1] >= self.mouse_pos[1]:
            print('4 cell')
        elif self.cells_pos[4][0][0] <= self.mouse_pos[0] and self.cells_pos[4][1][0] >= self.mouse_pos[0] and self.cells_pos[4][0][1] <= self.mouse_pos[1] and self.cells_pos[4][1][1] >= self.mouse_pos[1]:
            print('5 cell')
        elif self.cells_pos[5][0][0] <= self.mouse_pos[0] and self.cells_pos[5][1][0] >= self.mouse_pos[0] and self.cells_pos[5][0][1] <= self.mouse_pos[1] and self.cells_pos[5][1][1] >= self.mouse_pos[1]:
            print('6 cell')
        elif self.cells_pos[6][0][0] <= self.mouse_pos[0] and self.cells_pos[6][1][0] >= self.mouse_pos[0] and self.cells_pos[6][0][1] <= self.mouse_pos[1] and self.cells_pos[6][1][1] >= self.mouse_pos[1]:
            print('7 cell')
        elif self.cells_pos[7][0][0] <= self.mouse_pos[0] and self.cells_pos[7][1][0] >= self.mouse_pos[0] and self.cells_pos[7][0][1] <= self.mouse_pos[1] and self.cells_pos[7][1][1] >= self.mouse_pos[1]:
            print('8 cell')
        elif self.cells_pos[8][0][0] <= self.mouse_pos[0] and self.cells_pos[8][1][0] >= self.mouse_pos[0] and self.cells_pos[8][0][1] <= self.mouse_pos[1] and self.cells_pos[8][1][1] >= self.mouse_pos[1]:
            print('9 cell')

def main():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe Game')
    clock = pygame.time.Clock()
    window.fill((0, 0, 0))
    for line in LINE_COORD:
        pygame.draw.line(window, (255, 255, 255), line[0], line[1], 1)
    for circle in CIRCLES_COORD:
        pygame.draw.circle(window, [0, 0, 0], circle, 20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player = Player(mouse_pos)
                player.check_cell()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()