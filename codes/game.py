import sys
import pygame

def runGame():
    pygame.init()
    screen = pygame.display.set_mode((600,800))


    #game loop: 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill("red")
        pygame.display.update()
