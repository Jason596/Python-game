import pygame


def main():
    # 1 create a window
    screen = pygame.display.set_mode((602, 967), 0, 32)

    # 2 load background image
    background = pygame.image.load("./background.png")

    # 3 load background image to the window
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 4 display the window
        pygame.display.update()


# Click mouse or anything is an event, you need to create a event handler to handle it.
if __name__ == '__main__':
    main()
