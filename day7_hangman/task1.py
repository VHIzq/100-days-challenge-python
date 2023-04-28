import random
import stages
import logo
import hangman_word

lives = 6
chosen_word = random.choice(hangman_word.word_list)
end_game = False
display = ['_'] * len(chosen_word)
logo = logo.logo
print(logo)
print(display)
print(stages.stages[6])

while not end_game:
  guess = input('Guess a letter\n').lower()
  
  if guess in display:
      print(f'The letter {guess} is already entered')  
  
  for index, char in enumerate(chosen_word):
    isMatch = char == guess
    if isMatch:
      display[index] = guess
        
  if guess not in chosen_word:
    lives -= 1
    print(stages.stages[lives])
    print(lives)
    print(f'The letter {guess} is not in random word')
  
  print(display)
  
  has_blanks = '_' not in display
  if has_blanks:
    end_game = True
    print('U WIN!')
  
  is_die = lives == 0
  if is_die:
    end_game = True
    print('U LOSE!')
