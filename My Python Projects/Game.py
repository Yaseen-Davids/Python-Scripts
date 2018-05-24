# This is a guess the number game
import random

guessesTaken = 0

Hello = "Sup fucker"

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
        print('Your guess is too low.') # There are eight spaces

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

