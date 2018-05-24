import pygame
pygame.init()

#define some colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

Screen_Height = 600
Screen_Width = 400

size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False 

        screen.fill(WHITE)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
