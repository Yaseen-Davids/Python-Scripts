import pygame
import random
import time
import sys
#IMPORTING ALL CREATED CLASSES FORM INSIDE.PY
from Inside import PlayerBlock
from Inside import EnermyBlock
from Inside import Bullet
from Inside import Block
from Inside import Spawn
from Inside import Wall
from Inside import AmmoScore
from Inside import EnermyBullet
from Inside import HealthScore
from Inside import EnermyMeteor
from Inside import Spawn2
pygame.init()

#PLAY SOUND
pong = pygame.mixer.Sound('Data/Sounds/bullet.ogg')
pong.set_volume(0)

#PLAY MUSIC LOOP
backmus = pygame.mixer.Sound('Data/Sounds/game.wav')
backmus.play(-1)
backmus.set_volume(0)

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

#SCREEN RESOLUTION
Screen_Height = 600
Screen_Width = 800
size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

#SCROLLING BACKGROUND
background = pygame.image.load('Data/Images/back.jpeg').convert_alpha()
background_size = background.get_size()
background_rect = background.get_rect()
w,h = background_size
x = 0
y = 0
x1 = 0
y1 = -h

#SPRITE GROUPS
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
ammo_list = pygame.sprite.Group()
spawn_new = pygame.sprite.Group()
spawn2_new = pygame.sprite.Group()
all_wall = pygame.sprite.Group()
eBullet_list = pygame.sprite.Group()
wall_right = pygame.sprite.Group()
wall_left = pygame.sprite.Group()
wall_top = pygame.sprite.Group()
repair_list = pygame.sprite.Group()

eBullet = EnermyBullet()

player = PlayerBlock()
player.rect.x = 350
player.rect.y = 450

spawn = Spawn()
spawn.rect.x = 100
spawn.rect.y= -60

spawn2 = Spawn2()
spawn2.rect.x = 200
spawn2.rect.y = -60

spawn3 = Spawn2()
spawn3.rect.x = 600
spawn3.rect.y = -60

ammo = Block()
ammo.rect.x = (random.randint(50,700))
ammo.rect.y = 0

ammoScore = AmmoScore()
ammoScore.rect.x = 690
ammoScore.rect.y = 10

health = HealthScore()
health.rect.x = 690
health.rect.y = 65

enermy1 = EnermyBlock()
enermy2 = EnermyBlock()
enermy3 = EnermyBlock()
enermy4 = EnermyBlock()
enermy5 = EnermyBlock()
enermy_1 = EnermyMeteor()
enermy_2 = EnermyMeteor()

Wall_bot = Wall(BLUE, 800,1)
Wall_bot.rect.x = 0
Wall_bot.rect.y = 610
all_wall.add(Wall_bot)

Wall_r = Wall(BLUE, 1,600)
Wall_r.rect.x = 820
Wall_r.rect.y = 0
wall_right.add(Wall_r)

Wall_l = Wall(BLUE, 1,600)
Wall_l.rect.x = -25
Wall_l.rect.y = 0
wall_left.add(Wall_l)

Wall_t = Wall(BLACK, 800,1)
Wall_t.rect.x = 0
Wall_t.rect.y = 330
wall_top.add(Wall_t)

enermy_list = pygame.sprite.Group()

#POSITION OF ENERMY SPRITE
enermy1.rect.x = random.randrange(750)
enermy1.rect.y = random.randrange(50, 350)
enermy2.rect.x = random.randrange(750)
enermy2.rect.y = random.randrange(50, 350)
enermy3.rect.x = random.randrange(750)
enermy3.rect.y = random.randrange(50, 350)
enermy4.rect.x = random.randrange(750)
enermy4.rect.y = random.randrange(50, 350)
enermy5.rect.x = random.randrange(750)
enermy5.rect.y = random.randrange(50,350)
enermy_1.rect.x = random.randrange(750)
enermy_1.rect.y = random.randrange(50, 350)
enermy_2.rect.x = random.randrange(750)
enermy_2.rect.y = random.randrange(50, 350)
#GAME SETTINGS
random_bullets = random.randint(1,10)
pong = pygame.mixer.Sound('Data/Sounds/bullet.ogg')
pong.set_volume(0)
dead_sound = pygame.mixer.Sound('Data/Sounds/game_over.ogg')
ammo_crate_sound = pygame.mixer.Sound('Data/Sounds/up.ogg')
ammo_crate_sound.set_volume(8)
spawn_gun_sound = pygame.mixer.Sound('Data/Sounds/spawn1.ogg')
spawn_gun_sound.set_volume(8)
score = 0
bullets = 50
player_health = 100
MiniBossHealth = 40
carryOn = True
direction = 'down'
right_side = 200
change = 1
change_v = 2
change_e = 1
clock=pygame.time.Clock()
pygame.mouse.set_visible(1)
game_start = pygame.image.load('Data/Images/forward.png').convert_alpha()
gx = 300
gy = 300

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn=False
                elif event.key == pygame.K_SPACE:
                    if bullets > 0:
                        pong.play(0)
                        bullet = Bullet()
                        bullet.rect.x = player.rect.x + 28
                        bullet.rect.y = player.rect.y - 40
                        if change == 0:
                            bullets -= 1
                            all_sprites_list.add(bullet)
                            bullet_list.add(bullet)
                    if bullets <= 0:
                        bullet = Bullet()
                        bullet.remove()


        bullet = Bullet()
        if bullets == random_bullets:
            all_sprites_list.add(ammo)
            ammo_list.add(ammo)
        #KEYS
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)
        if keys[pygame.K_UP]:
            player.moveUp(5)
        if keys[pygame.K_DOWN]:
            player.moveDown(5)

        #background image
        y1 += 2
        y += 2
        screen.blit(background,(x,y))
        screen.blit(background,(x1,y1))
        if y > h:
            y = -h
        if y1 > h:
            y1 = -h

        font = pygame.font.Font(None, 36)
        #ALL TEXTS
        text6 = font.render("CLICK TO START!", 2, (200, 200, 200))
        text = font.render("Score = "+str(score), 2, (200, 100, 100))
        text2 = font.render(str(bullets), 2, (BLUE))
        text3 = font.render("No Ammo", 2, (CYAN))
        text5 = font.render("YOU DIED!", 2, (RED))
        spawnHealth = font.render("Mini Boss Health = "+str(MiniBossHealth), 2, (RED))

        screen.blit(text, (25,25))
        screen.blit(text2, (750,25))

        if change == 1:
            screen.blit(background,(0,0))
            screen.blit(text6, (260,200))
            screen.blit(game_start, (gx,gy))

        if event.type == pygame.MOUSEBUTTONDOWN:
            change = 0
            pong.set_volume(10)
            #backmus.set_volume(10)
            all_sprites_list.add(player)
            all_sprites_list.add(enermy1)
            all_sprites_list.add(enermy2)
            all_sprites_list.add(enermy3)
            all_sprites_list.add(enermy4)
            all_sprites_list.add(enermy5)
            all_sprites_list.add(enermy_1)
            all_sprites_list.add(enermy_2)
            all_sprites_list.add(health)
            #ADDING SPRITES TO GAME
            enermy_list.add(enermy1)
            enermy_list.add(enermy2)
            enermy_list.add(enermy3)
            enermy_list.add(enermy4)
            enermy_list.add(enermy5)
            enermy_list.add(enermy_1)
            enermy_list.add(enermy_2)

        all_sprites_list.update()
        bullet = Bullet()

        '''end_game = font.render("You finished the game!!", 2, (RED))'''
        talk_shit = font.render('Wow, you are worse than shit.', 2, (BLUE))
        talk_shit2 = font.render('Seriously, you are useless.', 2, (BLUE))

        if player_health == 100:
            healthNum = pygame.image.load('Data/Images/NUM/0.png').convert_alpha()
            screen.blit(healthNum, (780,75))
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/100.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 90:
            healthNum = pygame.image.load('Data/Images/NUM/0.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/9.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 80:
            healthNum = pygame.image.load('Data/Images/NUM/0.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/8.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 70:
            healthNum = pygame.image.load('Data/Images/NUM/0.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/7.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 60:
            healthNum = pygame.image.load('Data/Images/NUM/0.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/6.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 50:
            healthNum = pygame.image.load('Data/Images/NUM/000.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/5.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 40:
            healthNum = pygame.image.load('Data/Images/NUM/000.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/4.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 30:
            healthNum = pygame.image.load('Data/Images/NUM/00.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/3.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 20:
            healthNum = pygame.image.load('Data/Images/NUM/00.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/2.png').convert_alpha()
            screen.blit(healthNum1, (745,75))
        if player_health == 10:
            healthNum = pygame.image.load('Data/Images/NUM/00.png').convert_alpha()
            screen.blit(healthNum, (763,75))
            healthNum1 = pygame.image.load('Data/Images/NUM/1.png').convert_alpha()
            screen.blit(healthNum1, (745,75))


        if bullets <= 0:
            screen.blit(text3, (200,300))
        if -10 >= score >-20:
            screen.blit(talk_shit,(250,300))
        if score <= -20:
            screen.blit(talk_shit2,(250,300))
        for bullet in bullet_list:
            bullet_hit_list = pygame.sprite.spritecollide(bullet, enermy_list, False)
            for enermy in bullet_hit_list:
                score += 1
                #bullets += 1
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                enermy.rect.x = random.randrange(700)
                enermy.rect.y = 0
                pygame.time.wait(1)
                #all_sprites_list.remove(explosion)

        '''This is the collision between player and ammo crate'''
        for ammo in ammo_list:
            ammo_collision_list = pygame.sprite.spritecollide(player, ammo_list,False)
            for ammo in ammo_collision_list:
                bullets += 50
                ammo_crate_sound.play(0)
                all_sprites_list.remove(ammo)
                ammo_list.remove(ammo)
                ammo.rect.x = (random.randint(50,700))
                ammo.rect.y = 0

        '''This is the collision between player and health crate'''
        for repair in repair_list:
            repair_collision_list = pygame.sprite.spritecollide(player, repair_list,False)
            for repair in repair_collision_list:
                health == 100
                all_sprites_list.remove(repair)
                repair_list.remove(repair)
                repair.rect.x = (random.randint(50,700))
                repair.rect.y = 0
                change = 0

        '''This is the collision for the enermy and the Spaceship'''
        crash_collision_list = pygame.sprite.spritecollide(player,enermy_list,False)
        for enermy in crash_collision_list:
            enermy.rect.x = (random.randint(50,700))
            enermy.rect.y = -50
            player_health -= 10

        '''This is the bullet spawn collision'''
        spawn_collision_list = pygame.sprite.spritecollide(bullet,spawn_new,False)
        for spawn in spawn_collision_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            MiniBossHealth -= 1

        '''This is the player enermy-Bullet collision'''
        enermyB_player_collision_list = pygame.sprite.spritecollide(player,eBullet_list,False)
        for eBullet in enermyB_player_collision_list:
            eBullet_list.remove(eBullet)
            all_sprites_list.remove(eBullet)
            player_health -= 20

        '''This is the player wall collisions'''
        wall_r_player_collision_list = pygame.sprite.spritecollide(player,wall_right,False)
        for wall_r in wall_r_player_collision_list:
            player.moveLeft(5)
        wall_l_player_collision_list = pygame.sprite.spritecollide(player,wall_left,False)
        for wall_l in wall_l_player_collision_list:
            player.moveRight(5)
        wall_b_player_collision_list = pygame.sprite.spritecollide(player,all_wall,False)
        for Wall_bot in wall_b_player_collision_list:
            player.moveUp(5)
        wall_t_player_collision_list = pygame.sprite.spritecollide(player,wall_top,False)
        for Wall_top in wall_t_player_collision_list:
            player.moveDown(5)

        '''This is the enermy wall collisions'''
        enermy_wall_collision = pygame.sprite.spritecollide(enermy1,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy1.rect.x = (random.randint(50,700))
            enermy1.rect.y = -50
            score -=1
        enermy_wall_collision = pygame.sprite.spritecollide(enermy2,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy2.rect.x = (random.randint(50,700))
            enermy2.rect.y = -50
            score -=1
        enermy_wall_collision = pygame.sprite.spritecollide(enermy3,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy3.rect.x = (random.randint(50,700))
            enermy3.rect.y = -50
            score -=1
        enermy_wall_collision = pygame.sprite.spritecollide(enermy4,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy4.rect.x = (random.randint(50,700))
            enermy4.rect.y = -50
            score -=1
        enermy_wall_collision = pygame.sprite.spritecollide(enermy5,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy5.rect.x = (random.randint(50,700))
            enermy5.rect.y = -50
            score -=1
        enermy_wall_collision = pygame.sprite.spritecollide(enermy_1,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy5.rect.x = (random.randint(50,700))
            enermy5.rect.y = -50
        enermy_wall_collision = pygame.sprite.spritecollide(enermy_2,all_wall,False)
        for Wall_bot in enermy_wall_collision:
            enermy5.rect.x = (random.randint(50,700))
            enermy5.rect.y = -50

        if score >= 40:
            if enermy1.rect.y >= 100:
                enermy1.remove()
                all_sprites_list.remove(enermy1)
                enermy_list.remove(enermy1)
            if enermy2.rect.y >= 100:
                enermy2.remove()
                all_sprites_list.remove(enermy2)
                enermy_list.remove(enermy2)
            if enermy_1.rect.y >= 100:
                enermy_1.remove()
                all_sprites_list.remove(enermy_1)
                enermy_list.remove(enermy_1)
            if enermy_2.rect.y >= 100:
                enermy_2.remove()
                all_sprites_list.remove(enermy_2)
                enermy_list.remove(enermy_2)
            if enermy3.rect.y >= 100:
                enermy3.remove()
                all_sprites_list.remove(enermy3)
                enermy_list.remove(enermy3)
            if enermy4.rect.y >= 100:
                enermy4.remove()
                all_sprites_list.remove(enermy4)
                enermy_list.remove(enermy4)
            if enermy5.rect.y >= 100:
                enermy5.remove()
                all_sprites_list.remove(enermy5)
                enermy_list.remove(enermy5)
                spawn_new.add(spawn)
                all_sprites_list.add(spawn)
                spawn.add()
                change_v = 3
                if change_v == 3:
                    screen.blit(spawnHealth, (200,50))
                    if direction == 'down':
                        spawn.rect.y += 5
                        if spawn.rect.y == 140:
                            direction = 'right'
                    elif direction == 'right':
                        spawn.rect.x += 5
                        if spawn.rect.x == 700:
                            direction = 'up'
                    elif direction == 'up':
                        spawn.rect.y -= 5
                        if spawn.rect.y == 0:
                            direction = 'left'
                    elif direction == 'left':
                        spawn.rect.x -= 5
                        if spawn.rect.x == 0:
                            direction = 'down'

        if (spawn.rect.x == 90):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if (spawn.rect.x == 200):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if (spawn.rect.x == 300):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if (spawn.rect.x == 400):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if (spawn.rect.x == 500):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if (spawn.rect.x == 600):
            eBullet = EnermyBullet()
            spawn_gun_sound.play(0)
            eBullet.rect.x = spawn.rect.x + 90
            eBullet.rect.y = spawn.rect.y + 95
            all_sprites_list.add(eBullet)
            eBullet_list.add(eBullet)

        if player_health <= 0:
            screen.blit(background,(0,0))
            screen.blit(text5, (350,300))
            spawn.remove()
            spawn_new.remove(spawn)
            all_sprites_list.remove(spawn)
            eBullet.remove()
            eBullet_list.remove(eBullet)
            all_sprites_list.remove(eBullet)
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            all_sprites_list.remove(player)
            all_sprites_list.remove(enermy_list)
            dead_sound_play = True
            if dead_sound_play == True:
                dead_sound.play(- 1)
                dead_sound_play =   False
        if MiniBossHealth <= 0:
            change_v = 2
            spawn_gun_sound.set_volume(0)
            spawn.remove()
            spawn_new.remove(spawn)
            all_sprites_list.remove(spawn)
            eBullet.remove()
            eBullet_list.remove(eBullet)
            all_sprites_list.remove(eBullet)
            all_sprites_list.add(spawn2)
            all_sprites_list.add(spawn3)
            all_sprites_list.add(enermy4)
            all_sprites_list.add(enermy5)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
