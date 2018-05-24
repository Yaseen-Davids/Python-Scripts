import keyboard
import pyautogui as py

while True:
    try:
        if keyboard.is_pressed('1'):
            py.press('enter')
            py.typewrite("HERO MISS - CARE!!!!")
            py.press('enter')
            continue
        if keyboard.is_pressed('2'):
            py.press('enter')
            py.typewrite("share courier please")
            py.press('enter')
            continue
        if keyboard.is_pressed('3'):
            py.press('enter')
            py.typewrite("ty")
            py.press('enter')
            continue
        if keyboard.is_pressed('4'):
            py.press('enter')
            py.typewrite("-clear")
            py.press('enter')
            continue
        if keyboard.is_pressed('5'):
            py.press('enter')
            py.typewrite("Fuck you, noob.")
            py.press('enter')
            continue
        if keyboard.is_pressed('6'):
            py.keyDown('enter')
            py.keyDown('shift')
            py.keyUp('enter')
            py.keyUp('shift')
            py.typewrite("SW")
            py.press('enter')
            continue
        if keyboard.is_pressed('7'):
            py.press('enter')
            py.typewrite("Me Mid.")
            py.press('enter')
        if keyboard.is_pressed('8'):
            py.press('enter')
            py.typewrite("LAG FIX.")
            py.press('enter')
        else:
            pass
    except:
        continue

keyPresser()

