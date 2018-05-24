import time
import sys

wait = time.sleep

print ('Welcome to The Party ')
wait(1)
begin = input("Would you like to begin?: ")
if begin == "yes" or begin == "Yes" or begin == "Okay" or begin == "okay" :
    print('Lets Begin')
    time.sleep(1)
    print('What is your name?')
    myName = input()
    wait(1)
    print("That's a nice name, " +  myName + " .")
    
else :
    print('Stop wasting my time. Goodbye')
    wait(1)
    sys.exit()

wait(1)
    
age = input('Are you older than 15?')
if age == "yes" or age == "Yes" :
    print('You are old enough')

else :
    print('You are not old enough.')
    wait(0.5)
    print('Try again Next year')


