import pyautogui as pyag
import time
import sys
import keyboard

#Paint with keyboard

'''print("#Open paint before opening this.")
time.sleep(2)
print("Are you ready ?")

myChoice = input()
if myChoice == 'yes' or myChoice == 'Yes' or myChoice == 'y':
    print("Let's begin.")
else:
    print('Okay, take your time. Re-run the code when ready.')
    sys.exit()

time.sleep(2)

print(' Left key = left '
      '\n Right key = right '
      '\n Up key = up '
      '\n Down Key = down ')
time.sleep(2)'''

while True:
    try:
        if keyboard.is_pressed('right'):
            pyag.dragTo(1, 0)
            continue
        if keyboard.is_pressed('left'):
            pyag.moveTo(-1, 0)
            continue
        else:
            continue
    except:
        continue
