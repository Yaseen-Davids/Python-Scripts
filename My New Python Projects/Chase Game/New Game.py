import pygame
import random
import time
import pyautogui as py
pygame.init()

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

background = pygame.image.load("images1.jpg")

Screen_Height = 600
Screen_Width = 400

size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

all_sprites_list = pygame.sprite.Group()
#BLOCKS
#1
playerBlock = Block(BLACK, 50, 50)
playerBlock.rect.x = 345
playerBlock.rect.y = 500
#2
theBlackBlock = Block(RED, 50, 50)
theBlackBlock.rect.x = random.randint(55,345)
theBlackBlock.rect.y = random.randint(55,545)
#3
theGreenBlock = Block(GREEN, 50, 50)
theGreenBlock.rect.x = random.randint(55,345)
theGreenBlock.rect.y = random.randint(55,545)
#Walls
#1
theWall_left = Block(CYAN, 3, 600)
theWall_left.rect.x = 0
theWall_left.rect.y = 0
#2
theWall_right = Block(CYAN, 3, 600)
theWall_right.rect.x = 397
theWall_right.rect.y = 0
#3
theWall_top = Block(CYAN, 400, 3)
theWall_top.rect.x = 0
theWall_top.rect.y = 0
#4
theWall_bot = Block(CYAN, 400, 3)
theWall_bot.rect.x = 0
theWall_bot.rect.y = 597

#Solo
all_sprites_list.add(playerBlock)
all_sprites_list.add(theWall_left)
all_sprites_list.add(theWall_right)
all_sprites_list.add(theWall_top)
all_sprites_list.add(theWall_bot)
all_sprites_list.add(theBlackBlock)
all_sprites_list.add(theGreenBlock)

all_coming_blocks = pygame.sprite.Group()
all_coming_blocks.add(theBlackBlock)
all_coming_blocks2 = pygame.sprite.Group()
all_coming_blocks2.add(theGreenBlock)

all_top_wall = pygame.sprite.Group()
all_top_wall.add(theWall_top)
all_bot_wall = pygame.sprite.Group()
all_bot_wall.add(theWall_bot)
all_right_wall = pygame.sprite.Group()
all_right_wall.add(theWall_left)
all_left_wall = pygame.sprite.Group()
all_left_wall.add(theWall_right)

carryOn = True
clock=pygame.time.Clock()

score = 0

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                playerBlock.moveLeft(5)
        if keys[pygame.K_RIGHT]:
                playerBlock.moveRight(5)
        if keys[pygame.K_UP]:
                playerBlock.moveUp(5)
        if keys[pygame.K_DOWN]:
                playerBlock.moveDown(5)

        all_sprites_list.update()

        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("Score = "+str(score), 2, (200, 100, 100))
        screen.blit(text, (25,50))

        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_coming_blocks,False)
        for block in block_collision_list:
                theBlackBlock.rect.x = random.randint(50,350)
                theBlackBlock.rect.y = random.randint(50,550)
                score += 1
                carryOn = True

        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_coming_blocks2,False)
        for block in block_collision_list:
                theGreenBlock.rect.x = random.randint(50,350)
                theGreenBlock.rect.y = random.randint(50,550)
                score += 1
                carryOn = True
        #Walls
        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_top_wall,False)
        for block in block_collision_list:
                playerBlock.moveDown(5)
                score -= 1
                time.sleep(0.1)
                carryOn = True

        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_bot_wall,False)
        for block in block_collision_list:
                playerBlock.moveUp(5)
                score -= 1
                time.sleep(0.1)
                carryOn = True

        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_left_wall,False)
        for block in block_collision_list:
                playerBlock.moveLeft(5)
                score -= 1
                time.sleep(0.1)
                carryOn = True

        block_collision_list = pygame.sprite.spritecollide(playerBlock,all_right_wall,False)
        for block in block_collision_list:
                playerBlock.moveRight(5)
                score -= 1
                time.sleep(0.1)
                carryOn = True

        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
