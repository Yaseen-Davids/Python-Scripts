import keyboard
import pyautogui
import time as wait

pyautogui.FAILSAFE = False

while True:
    try:
        if keyboard.is_pressed('RIGHT'):
            pyautogui.moveRel(10, None)
            continue
        if keyboard.is_pressed('LEFT'):
            pyautogui.moveRel(-10, None)
            continue
        if keyboard.is_pressed('UP'):
            pyautogui.moveRel(None, -10)
            continue
        if keyboard.is_pressed('DOWN'):
            pyautogui.moveRel(None, 10)
            continue
        if keyboard.is_pressed('1'):
            pyautogui.click(button='left')
            continue1
        if keyboard.is_pressed('3'):
            pyautogui.click(button='left', clicks=2)
            continue
        if keyboard.is_pressed('2'):
            pyautogui.click(button='right')
            continue
        else:
            pass
    except:
        continue
