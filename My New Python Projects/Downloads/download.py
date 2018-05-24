import pyautogui
import time

print("#TIME IN SECONDS")
print("How long until downloads start? :")
myTimeAmount = int(input())

time.sleep(myTimeAmount)
pyautogui.click(button='left')
pyautogui.click(button='left')
#double click
time.sleep(2)
pyautogui.moveTo(587, 877)
pyautogui.click(button='left')
#opens utorrent on taskbar
time.sleep(2)
pyautogui.moveTo(975, 315)
pyautogui.click(button='left')
time.sleep(1)
pyautogui.moveTo(853, 232)
pyautogui.click(button='right')
#opens download menu
time.sleep(0.5)
pyautogui.moveTo(937, 422)
pyautogui.click(button='left')
#starts download
time.sleep(0.5)
pyautogui.moveTo(787, 248)
pyautogui.click(button='right')
#opens download menu
time.sleep(0.5)
pyautogui.moveTo(846, 436)
pyautogui.click(button='left')
#starts download
time.sleep(0.5)
pyautogui.moveTo(867, 266)
pyautogui.click(button='right')
#opens download menu
time.sleep(0.5)
pyautogui.moveTo(922, 451)
pyautogui.click(button='left')
#starts download
time.sleep(1)
pyautogui.moveTo(1109, 616)
pyautogui.click(button='left')
pyautogui.click(button='left')
#maximizes vlc
print("All done.")


