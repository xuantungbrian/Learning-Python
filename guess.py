import random

guessTaken = 0
print('Hello, what is your name?')
myName = input()
number = random.randint(1, 20)
print('Well, '+ myName + ', I am thinking of a number between 1 and 20')

while (guessTaken < 6):
    print('Take a guess')
    guess = input()
    guess = int(guess)
    guessTaken = guessTaken + 1

    if guess<number:
        print('Your guess is too low')
    elif guess>number:
        print('Your guess is too high')
    else:
        print('You are correct')
        break
if guess == number:
    guessTaken = str(guessTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessTaken + ' guesses')
else:
    print('Sorry brah, I was thinking of the number '+str(number))
