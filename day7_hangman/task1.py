# Step 1


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess_list = list(chosen_word)
display = []
blanks_count = 0

while blanks_count == 0:
  guess = input('Try to guess a letter from the word \n').lower()
  print(guess)
  for char in guess_list:
    isMatch = char == guess

  if isMatch:
    print('matches!')
    display.append(guess)
  else:
    print('Shot!')
    display.append('_')
      
blanks_count = display.count('_')


print(display)
print(blanks_count)

