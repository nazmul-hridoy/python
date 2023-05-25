#Python program for 'Guess the Number Game'
from random import *
guessesTaken = 0  #to keep count of number of guesses
print('What is your name?')
myName = input()  #getting the user name
number = randint(1, 20) #generating a number within the range 1 to 20
print('Hello, ' + myName + ', I am thinking of a number between 1 and 20')
while guessesTaken < 4:  #number of guesses = 4
  print('Take a guess')
  guess = int(input())  #getting the guessed number from the user
  guessesTaken = guessesTaken + 1  #for each and every input from the user, this variable keeps incrementingif guess < number:
    print('Guess is too low. Try again')
  if guess > number:
    print('Guess is too high. Try again')
  if guess == number:
    break

#executes when the user guessed the correct number
if guess == number:
  guessesTaken = str(guessesTaken)
  print('Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')

#executes when the user crosses the guess limit of 4
if guess != number:
  number = str(number)
  print('oops. You have reached the guessing limit. The number that I was thinking is ' + number)