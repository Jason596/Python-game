import time

import pygame
from pygame import K_w, K_UP, QUIT, K_s, K_DOWN, K_LEFT, K_RIGHT, K_d, K_a, K_SPACE


class HeroPlane(object):
    def __init__(self, screen):
        self.player = pygame.image.load("./airplane.jpeg")
        # 3 load background image to the window
        self.x = 602 / 2 - 225 / 2
        self.y = 700
        self.speed = 10
        self.screen = screen
        self.bullets = []

    def key_control(self):
        key_pressed = pygame.key.get_pressed();

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            bullet = Bullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == K_a or event.key == K_LEFT:
            #         print("left")
            #     elif event.key == K_d or event.key == K_RIGHT:
            #         print("right")
            #     elif event.key == K_SPACE:
            #         print("space")
        # 4 display th e window

    def display(self):
        self.screen.blit(self.player, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()


class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./bullet-image.jpg")
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


def main():
    # 1 create a window
    screen = pygame.display.set_mode((602, 967), 0, 32)

    # 2 load background image
    background = pygame.image.load("./background.png")

    player = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))

        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                # exit pygame and exit python program
                pygame.quit()
                exit()
        player.key_control()
        player.display()

        # constantly display the window
        pygame.display.update()
        time.sleep(0.01)


# Click mouse or anything is an event, you need to create a event handler to handle it.
if __name__ == '__main__':
    main()
