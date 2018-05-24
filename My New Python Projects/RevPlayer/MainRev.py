#Rev Player Main
import time
import pyautogui as py
import datetime
import os
import pygame
import webbrowser as wb
import clipboard
import keyboard
import pyperclip

def mainRev():
    while True:
        date = datetime.datetime.now().strftime('%d')
        if date == '13':
            wb.open_new('https://www.google.co.za/search?client=firefox-b&dcr=0&ei=_s6CWuHJI8KRgAap2I3ABQ&q=time+now&oq=time+now&gs_l=psy-ab.3...5283.6209.0.6336.8.6.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..8.0.0....0.vkq6YCIcP7U')
            time.sleep(7)
            py.moveTo(205, 313)
            time.sleep(1)
            py.click(button='left', clicks=3)
            py.keyDown('Ctrl')
            py.keyDown('c')
            py.keyUp('Ctrl')
            py.keyUp('c')
            time.sleep(0.5)
            print(clipboard.paste())
            date2 = datetime.datetime.now().strftime('%H:%M')
            if clipboard.paste() == date2:
                os.system('SubRev.py')
            break
mainRev()
