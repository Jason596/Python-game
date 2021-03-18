import pygame

# 1 create a window
screen = pygame.display.set_mode((602, 967), 0, 32)

# 2 load background image
background = pygame.image.load("./background.png")

# 3 load background image to the window
screen.blit(background, (0, 0))

# 4 display the window
pygame.display.update()

