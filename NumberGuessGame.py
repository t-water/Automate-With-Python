import random

maxNum = 20
maxGuesses = 6

def gameLoop():
    target = random.randint(1, maxNum)
    numGuesses = 0
    userGuess = 0

    print('Well', name, 'I am thinking of a number between 1 and', str(maxNum))

    while(numGuesses < maxGuesses and userGuess != target):
        if numGuesses == 0:
            print('Take a guess')
        elif userGuess < target:
            print('Your guess is too low')
        else:
            print('Your guess is too high')
        
        userGuess = int(input())
        numGuesses = numGuesses + 1

    if userGuess == target:
        print('Good job', name, 'you guessed my number in', numGuesses, 'guesses.')
    elif numGuesses >= maxGuesses:
        print('Nope. The number I was thinking of was', str(target))

print('Hello, what is your name?')
name = input()

def game():
    continueGame = True

    while continueGame:
        gameLoop()

        print('Would you like to play again (y/n)')
        continueGame = input().lower() == 'y'

game()