import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Задаем прозрачный цвет
transparent = (255, 0, 0, 0)

# Заполняем экран прозрачным цветом
screen.fill(transparent)

# Отображаем изменения на экране
pygame.display.flip()

# Зацикливаем программу до закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()