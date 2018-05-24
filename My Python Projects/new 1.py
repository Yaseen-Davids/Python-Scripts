import pyautogui
import time

pyautogui.keyDown('Ctrl')
pyautogui.keyDown('Shift')
pyautogui.keyDown('Esc')
time.sleep(0.5)
pyautogui.keyUp('Ctrl')
pyautogui.keyUp('Shift')
pyautogui.keyUp('Esc')
