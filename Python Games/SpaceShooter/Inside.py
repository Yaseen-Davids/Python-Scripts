import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class PlayerBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/Spaceship.png').convert_alpha()
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

class EnermyBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/images.png').convert_alpha()
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def update(self):
        self.rect.y += 4
        if self.rect.bottom > 650:
            self.rect.top = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/bullet1.png').convert_alpha()

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/ammo.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 3

class Spawn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/spawn.png').convert_alpha()
        self.rect = self.image.get_rect()

    def moveLeft(self,pixels):
        self.rect.x -= 5

    def moveRight(self,pixels):
        self.rect.x += 5

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

class EnermyBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/bullett.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

class Wall(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

class AmmoScore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/ammoscore.png').convert_alpha()
        self.rect = self.image.get_rect()

class HealthScore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/health.jpg').convert_alpha()
        self.rect = self.image.get_rect()

class EnermyMeteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/images2.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 4
        if self.rect.bottom > 650:
            self.rect.top = 0

class Spawn2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('Data/Images/tank.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2
