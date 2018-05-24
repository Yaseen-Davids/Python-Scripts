import time
import datetime
import os
import pyautogui as py
import clipboard
import pygame

def theDate():
    while True:
        date = datetime.datetime.now().strftime("%H:%M")
        if date == clipboard.paste():
            pygame.mixer.init()
            pygame.mixer.music.load("Alarm.mp3")
            pygame.mixer.music.play()
            break

theDate()
print("DONE")
time.sleep(15)

