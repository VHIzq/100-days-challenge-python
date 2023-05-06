#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

game = random.randint(1, 100)
print(game)

level = int(input('Choose a difficulty level: Type "0" for easy with 10 guesses or type "1" for hard mode with 5 guesses'))

attempts = 0
if level == 0:
  attempts = 10
  print('Easy mode') 
else:
  attempts = 5
  print('Hard mode')

def guessing_number(trys):
  if trys > 0:
    guess = int(input('Guess a number between 1 and 100'))
    
    if guess == game:
      print(f'You guessed the number! It was: {game}')
      return
    else:
      if guess > game:
        print(f'Too high: {guess}')
        trys -= 1
        guessing_number(trys)
      elif guess < game:
        print(f'Too low: {guess}')
        trys -= 1
        guessing_number(trys)
        
  elif trys == 0:
    print(f'You ran out of tries. The number was: {game}')
  
guessing_number(trys=attempts)
