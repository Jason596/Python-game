import time

import pygame
from pygame import K_w, K_UP, QUIT, K_s, K_DOWN, K_LEFT, K_RIGHT, K_d, K_a


def main():
    # 1 create a window
    screen = pygame.display.set_mode((602, 967), 0, 32)

    # 2 load background image
    background = pygame.image.load("./background.png")
    player = pygame.image.load("./airplane.jpeg")

    # 3 load background image to the window

    x = 602 / 2 - 225 / 2
    y = 700
    speed = 10

    while True:
        screen.blit(background, (0, 0))
        screen.blit(player, (x, y))

        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                # exit pygame and exit python program
                pygame.quit()
                exit()

        key_pressed = pygame.key.get_pressed();

        if key_pressed[K_w] or key_pressed[K_UP]:
            y -= speed
            print("up")
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            y += speed
            print("down")
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            x -= speed
            print("left")
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            x += speed
            print("right")

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == K_a or event.key == K_LEFT:
            #         print("left")
            #     elif event.key == K_d or event.key == K_RIGHT:
            #         print("right")
            #     elif event.key == K_SPACE:
            #         print("space")
        # 4 display th e window
        pygame.display.update()
        time.sleep(0.01)


# Click mouse or anything is an event, you need to create a event handler to handle it.
if __name__ == '__main__':
    main()
