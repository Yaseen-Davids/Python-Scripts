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
Screen_Width = 700

size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, radius):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.ellipse(self.image, color, [0, 0, width, height], radius)
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.y += pixels

    def moveRight(self, pixels):
        self.rect.y -= pixels

all_sprites_list = pygame.sprite.Group()
paddle_1 = Paddle(RED, 50 ,50)
paddle_1.rect.x = 30
paddle_1.rect.y = 250

paddle_2 = Paddle(BLUE, 50, 50)
paddle_2.rect.x = 630
paddle_2.rect.y = 250

poles_1 = Paddle(BLACK, 5, 600)
poles_1.rect.x = 680
poles_1.rect.y = 0

poles_2 = Paddle(BLACK, 5, 600)
poles_2.rect.x = 20
poles_2.rect.y = 0

theWall_top = Paddle(BLACK, 660, 5)
theWall_top.rect.x = 20
theWall_top.rect.y = 0

theWall_bot = Paddle(BLACK, 660, 5)
theWall_bot.rect.x = 20
theWall_bot.rect.y = 595

ball = Ball(GREEN, 50, 50, 0)
ball.rect.x = 325
ball.rect.y = 275

all_sprites_list.add(paddle_1)
all_sprites_list.add(paddle_2)
all_sprites_list.add(poles_1)
all_sprites_list.add(poles_2)
all_sprites_list.add(theWall_bot)
all_sprites_list.add(theWall_top)
all_sprites_list.add(ball)

all_top_wall = pygame.sprite.Group()
all_top_wall.add(theWall_top)
all_bot_wall = pygame.sprite.Group()
all_bot_wall.add(theWall_bot)

the_ball = pygame.sprite.Group()
the_ball.add(ball)

direction = 'right'

halfwayLine = (325,275)
carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_1.moveUp(5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            paddle_1.moveDown(5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_2.moveUp(5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            paddle_2.moveDown(5)

        '''if direction == 'right':
            paddle_1.rect.x += 5
            if paddle_1.rect.x == 655:
                direction = 'left'
        elif direction == 'left':
            paddle_1.rect.x -= 5
            if paddle_1.rect.x == 5:
                direction = 'right'
        elif direction == 'right':
            paddle_1.rect.x += 5'''

        spamRect = paddle_2

        if direction == 'right':
            ball.rect.x += 5
            if (ball.rect.x) == (paddle_2.rect.x):
                direction = 'left'
        elif direction == 'left':
            ball.rect.x -= 5
            if (ball.rect.x) == (paddle_1.rect.x):
                direction =  'right'

        all_sprites_list.update()
        screen.fill(WHITE)

        if (ball.rect.x) == (paddle_2.rect.x):
            ball.rect.x -= 5
        elif ( ball.rect.x) == (paddle_1.rect.x):
            ball.rect.x += 5

        if ball.rect.x == 700:
            (ball.rect.x, ball.rect.y) = (halfwayLine)
        if ball.rect.x == 0:
            (ball.rect.x, ball.rect.y) = (halfwayLine)


        paddle_collision_list = pygame.sprite.spritecollide(paddle_1,all_bot_wall,False)
        for paddle in paddle_collision_list:
                paddle_1.moveUp(5)
                carryOn = True

        paddle_collision_list = pygame.sprite.spritecollide(paddle_1,all_top_wall,False)
        for paddle in paddle_collision_list:
                paddle_1.moveDown(5)
                carryOn = True

        paddle_collision_list = pygame.sprite.spritecollide(paddle_2,all_bot_wall,False)
        for paddle in paddle_collision_list:
                paddle_2.moveUp(5)
                carryOn = True

        paddle_collision_list = pygame.sprite.spritecollide(paddle_2,all_top_wall,False)
        for paddle in paddle_collision_list:
                paddle_2.moveDown(5)
                carryOn = True

        halway_line = pygame.draw.line(screen, BLACK, [350,0],[350,Screen_Height],5)
        halfway = pygame.draw.ellipse(screen, BLACK, [300, 250,100, 100],5)

        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
