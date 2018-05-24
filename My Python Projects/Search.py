import time
import pyautogui

print('What would you like to search?')
print(':')
mySearch = input()
time.sleep(1)
pyautogui.keyDown('win')
pyautogui.keyUp('win')
time.sleep(2)
pyautogui.typewrite(mySearch, interval=0.2)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
