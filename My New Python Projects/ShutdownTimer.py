#SHUTDOWN TIMER
import os
import time

print("How long until Shutdown?")
timer = int(input())

time.sleep(timer)
os.system('shutdown -s')
