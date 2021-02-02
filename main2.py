#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"



number = random.randrange(1,11)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input("Guess a number from 1 to 10: ")
    try:
        guess = int(guess)
        if guess != number:
            print("Nope! Give it another guess!")
    except:
        print("Are you even trying? Put in a number!")
print("Great job! You got it! You guessed the number in " + str(count) + " tries. ")