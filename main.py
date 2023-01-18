__author__ = 'Ben'

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ben's Game")
    clock = pygame.time.Clock()

    test_surface = pygame.Surface((100, 100))
    test_surface.fill('Blue')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(test_surface, (350, 350))
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
