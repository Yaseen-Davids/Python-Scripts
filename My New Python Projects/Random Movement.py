import pyautogui as py
import time
import keyboard
import random

'''x = random.randint(1, 1000)
y = random.randint(1, 1000)
number_x = random.randint(1, 1440)
number_y = random.randint(1, 900)'''
time.sleep(2)

def main():
    while True:
        '''x = random.randint(1, 1000)
        y = random.randint(1, 1000)'''
        number_x = random.randint(1, 1440)
        number_y = random.randint(1, 900)
        if py.position() != (0, 0):
            py.moveTo(number_x, number_y, duration=1)
            print(py.position())
            if keyboard.is_pressed('1'):
                break
            time.sleep(0.5)
            continue
main()



