# This is a guess the number game
import random
import time

guessesTaken = 0

Hello = "Sup Human Person"

print(Hello + "!" + 'What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

while guessesTaken < 6:
    print('Take a guess.') # Four spaces for new block
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low, ' + myName + ', Try Again') # There are eight spaces

    if guess > number:
        print('Your guess is too high, ' + myName + ', Try Again')

        time.sleep(1.5)

    if guess == number:
        break

time.sleep(1.5)

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses')

time.sleep(1.5)

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

