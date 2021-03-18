import pygame
from pygame import *


def main():
    # 1 create a window
    screen = pygame.display.set_mode((602, 967), 0, 32)

    # 2 load background image
    background = pygame.image.load("./background.png")
    player = pygame.image.load("./airplane.jpeg")

    # 3 load background image to the window
    screen.blit(background, (0, 0))
    screen.blit(player, (602/2 - 225/2, 700))

    while True:
        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                # exit pygame and exit python program
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                elif event.key == K_SPACE:
                    print("space")
        # 4 display the window
        pygame.display.update()


# Click mouse or anything is an event, you need to create a event handler to handle it.
if __name__ == '__main__':
    main()
