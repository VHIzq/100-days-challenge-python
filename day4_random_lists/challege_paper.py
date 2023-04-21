import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))

gamer_choices  = [rock, paper, scissors]

is_rock = user_choice == 0
is_paper = user_choice == 1
is_scissors = user_choice == 2

computer_choice = random.randint(0,2)
is_rock_comp = computer_choice == 0
is_paper_comp = computer_choice == 1
is_scissors_comp = computer_choice == 2

print('User choice:')
print(gamer_choices[user_choice])
  
print('Computer  choice:')
print(gamer_choices[computer_choice])


if is_rock and is_scissors_comp:
  print('You win')
  
elif is_rock and is_paper_comp:
  print('You lose')

elif is_paper and is_scissors_comp:
  print('You lose')

elif is_paper and is_rock_comp:
  print('You win')

elif is_scissors and is_paper_comp:
  print('You win')

elif is_scissors and is_rock_comp:
  print('You lose')
  
elif user_choice == computer_choice:
  print('Is tie')

