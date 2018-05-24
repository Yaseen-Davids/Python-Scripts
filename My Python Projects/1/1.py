import pyautogui
import time

#this presses windows button
pyautogui.keyDown('win', pause=True)
pyautogui.keyUp('win', pause=True)
#this releases windows button
pyautogui.typewrite('run', interval=0.2)
time.sleep(0.5)
#this presses enter button
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
#this releases enter button
time.sleep(0.5)
pyautogui.typewrite('chrome.exe', interval=0.2)
#this presses enter button
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
time.sleep(25)
#this releases enter button
pyautogui.keyDown('ctrl', pause=True)
pyautogui.keyDown('t', pause=True)
time.sleep(3)
pyautogui.keyUp('ctrl', pause=False)
pyautogui.keyUp('t', pause=False)

# pyautogui.typewrite('')
time.sleep(2)
pyautogui.typewrite('http://geektyper.com/plain/', interval=0.2)
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
time.sleep(15)
pyautogui.keyDown('1', pause=False)
pyautogui.keyUp('1', pause=False)
time.sleep(2)
pyautogui.keyDown('2', pause=False)
pyautogui.keyUp('2', pause=False)
time.sleep(4)
pyautogui.keyDown('4', pause=False)
pyautogui.keyUp('4', pause=False)
time.sleep(4)
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
time.sleep(4)
pyautogui.keyDown('6', pause=False)
pyautogui.keyUp('6', pause=False)
time.sleep(4)
pyautogui.keyDown('shift', pause=False)
pyautogui.keyUp('shift', pause=False)
time.sleep(5)
pyautogui.keyDown('alt', pause=False)
pyautogui.keyDown('f4', pause=False)
pyautogui.keyUp('alt', pause=False)
pyautogui.keyUp('f4', pause=False)

#this presses windows button
pyautogui.keyDown('win', pause=True)
pyautogui.keyUp('win', pause=True)
#this releases windows button
pyautogui.typewrite('run', interval=0.2)
time.sleep(0.5)
#this presses enter button
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
#this releases enter button
time.sleep(0.5)
pyautogui.typewrite('cmd', interval=0.2)
#this presses enter button
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)
time.sleep(1)
pyautogui.typewrite('ipconfig', interval=0.2)
pyautogui.keyDown('enter', pause=False)
pyautogui.keyUp('enter', pause=False)

