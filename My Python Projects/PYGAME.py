#this is a pygame test
import pygame
import time
import sys
import random
import socket

name = "BATMAN"

print('#DISCLAIMER - YOU HAVE TO BE OLDER THAN 15 TO PLAY'
      ' THIS GAME.')

time.sleep(2)

print('Hello, I am ' + socket.gethostname() + '.')
time.sleep(1)
# This is a pause
print('What is your name?')
# This is a pause
myName = input()
time.sleep(1.5)
# This is a pause
print('That is nice.')
time.sleep(1)
# This is a pause
print('How old are you ' + myName + ' ?')
myAge = input()
myAge = int(myAge)

time.sleep(0.5)

if myAge >= 15:
    print('You are old enough to play.')

if myAge == 15:
    print('You are old enough to play.')

if myAge <= 15:
    print('You are not old enough to play.')
    sys.exit()
    
time.sleep(0.5)
start = input( myName + ', would you like to play a game?')
if start == 'yes' or start == 'Yes' or start == 'no' or start == 'No':
    print('Lets begin this.')
    
time.sleep(1)
#This is a pause

pygame.init()
screen = pygame.display.set_mode((1440, 900))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

def draw(self):
        """
            draws the paddle onto screen.
        """
        pygame.draw.rect(screen, (0,0,0), (self._xLoc,self._yLoc,self._width,self._height),0)
def update(self):
        """
            moves the paddle at the screen via mouse
        """
        x,y = pygame.mouse.get_pos()
        if x >= 0 and x <= (self.__W - self._width):
            self._xLoc = x

# Add this somewhere after the event pumping and before the display.flip() 
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
