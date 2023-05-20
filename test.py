import pygame

# инициализация Pygame
pygame.init()

# установка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# создание экрана
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Контур круга")

# рисование круга
x, y = 250, 250
radius = 50
thickness = 2
pygame.draw.circle(screen, WHITE, (x, y), radius, thickness)

# обновление экрана
pygame.display.flip()

# главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# выход из Pygame
pygame.quit()