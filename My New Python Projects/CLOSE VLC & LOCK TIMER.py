import time
import pyautogui

print("How long until lock ? :")
myTimer = int(input())


time.sleep(myTimer)        
pyautogui.click(button='left')
pyautogui.click(button='left')
time.sleep(1)
pyautogui.moveTo(437, 878)
pyautogui.click(button='right')
time.sleep(1)
pyautogui.moveTo(424, 831)
pyautogui.click(button='left')

time.sleep(2)

pyautogui.moveTo(30, 875)
time.sleep(1)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(336, 831)
time.sleep(0.5)
pyautogui.moveTo(376, 782)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(0.5)
    


