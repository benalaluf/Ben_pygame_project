__author__ = 'Ben'

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ben's Game")
    clock = pygame.time.Clock()
    font_test = pygame.font.Font(None, 50)

    test_surface = pygame.Surface((200, 200))
    test_surface.fill('Blue')

    text_surface = font_test.render("coolest dog in the neighborhood", True, 'Green')

    background = pygame.image.load('graphics/cool_dog.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(background, (45, 150))
        screen.blit(text_surface, (150, 40))

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    print(r"""    
          __          ___         
         / /  __ __  / _ )___ ___ 
        / _ \/ // / / _  / -_) _ \
       /_.__/\_, (_)____/\__/_//_/
            /___/                      
                         """)
    main()
