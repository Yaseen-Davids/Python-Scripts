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
SCREEN = pygame.display.set_mode(size)
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

    def moveBot(self, pixels):
        self.rect.y += pixels

    def moveTop(self, pixels):
        self.rect.y -= pixels

    def moveRight(self, pixels):
        self.rect.x -= pixels

class Ball(object):
    def __init__ (self, SCREEN):
        direction = 'right'
    def draw(self):
        """
            draws the ball onto screen.
        """
        self.image = pygame.Surface([width, height])
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
    def update(self):
        """
            moves the ball at the screen.
            contains some collision detection.
        """
        if direction == 'right':
            Ball.moveRight(5)

'''class Ball(object):
    def main(self):
        pygame.mouse.set_visible(0)

    def draw(self):
        ball = pygame.draw.ellipse(SCREEN, GREEN, [50,50],[50,50],0 )
        ballrect = ball.get_rect()'''

all_sprites_list = pygame.sprite.Group()
paddle_1 = Paddle(PURPLE, 40, 100)
paddle_1.rect.x = 50
paddle_1.rect.y = 250

paddle_2 = Paddle(RED, 40, 100)
paddle_2.rect.x = 610
paddle_2.rect.y = 250

poles_1 = Paddle(BLACK, 5, 600)
poles_1.rect.x = 40
poles_1.rect.y = 0

poles_2 = Paddle(BLACK, 5, 600)
poles_2.rect.x = 655
poles_2.rect.y = 0

theWall_top = Paddle(BLACK, 615, 5)
theWall_top.rect.x = 40
theWall_top.rect.y = 0

theWall_bot = Paddle(BLACK, 615, 5)
theWall_bot.rect.x = 40
theWall_bot.rect.y = 595

'''block_ball = Paddle(GREEN, 50,50)
block_ball.rect.x = 100
block_ball.rect.y = 200'''

all_sprites_list.add(paddle_1)
all_sprites_list.add(paddle_2)
all_sprites_list.add(poles_1)
all_sprites_list.add(poles_2)
all_sprites_list.add(theWall_bot)
all_sprites_list.add(theWall_top)
'''all_sprites_list.add(block_ball)'''

all_top_wall = pygame.sprite.Group()
all_top_wall.add(theWall_top)
all_bot_wall = pygame.sprite.Group()
all_bot_wall.add(theWall_bot)

carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        keys = pygame.key.get_pressed()
        #paddle1
        if keys[pygame.K_UP]:
            paddle_1.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddle_1.moveDown(5)
        #paddle2
        if keys[pygame.K_w]:
            paddle_2.moveTop(5)
        if keys[pygame.K_s]:
            paddle_2.moveBot(5)

        ball = Ball(SCREEN,50,50)

        all_sprites_list.update()
        SCREEN.fill(WHITE)

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

        halway_line = pygame.draw.line(SCREEN, BLACK, [350,0],[350,Screen_Height],5)
        halfway = pygame.draw.ellipse(SCREEN, BLACK, [300, 250,100, 100],5)

        ball.draw()
        ball.update()

        all_sprites_list.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
