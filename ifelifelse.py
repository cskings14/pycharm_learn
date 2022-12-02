# TODO CHALLENGE: make a number guesser game

import random

num = random.randint(1,100)
print('Guess the number from 1 to 100: ')


if num >= 50:
    print('The number is greater than or equal to 50')
else:
    print('The number is less than 50')


count = 1
guessnum = int(input())

while guessnum != num:
    if guessnum == num:
        break
    count += 1
    if (guessnum > 100 or guessnum < 1):
        print('ERROR: out or range 1-100')

    if guessnum < num:
        print('TOO LOW')

    if guessnum > num:
        print('TOO HIGH')

    print('wrong try again: ')
    guessnum = int(input())




if guessnum == num:
    print(f'{num} was the correct number. You guessed the right number. It took you {count} tries')





