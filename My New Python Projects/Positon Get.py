#THIS IS THE TESTER SHELL
import datetime
import os
import pyautogui
import keyboard
import time

def keyPress():
    while True:
        if keyboard.is_pressed('1'):
            print(pyautogui.position())
            time.sleep(0.2)
            keyPress()
        if keyboard.is_pressed('2'):
            break
keyPress()
