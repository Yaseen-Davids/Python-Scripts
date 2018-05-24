import pygame
from Inside import Block
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
Screen_Width = 800

size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RUNNER")

def main():

    all_sprites_list = pygame.sprite.Group()
    block = Block(RED, 50, 50)
    block.rect.x = 500
    block.rect.y = 200
    all_sprites_list.add(block)

    carryOn = True
    clock=pygame.time.Clock()
    while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block.moveUp(50)

        screen.fill(WHITE)
        all_sprites_list.update()

        if block.rect.y >= 555:
            block.moveUp(2)

        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__ == "__main__":
    main()
