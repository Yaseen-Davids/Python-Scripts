#THIS IS THE TESTER SHELL
import datetime
import os
import pyautogui as py
import time
import os
import webbrowser as wb
import keyboard
import sys

def loop():
    while True:
        print('Try and stop me.')
        if keyboard.is_pressed('Esc'):
            sys.exit()
        loop()
loop()

