import random

print('-----------------------------------')
print('Guess the number game')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)

# print(guess_text, type(guess_text))
# print(guess, type(guess))

guess = -1

name = input('Player, what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100, inclusive: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, your guess of {} is too low.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too high.'.format(name, guess))
    else:
        print('Excellent work, {}, you won. It was {}.'.format(name, guess))

print('Done.')