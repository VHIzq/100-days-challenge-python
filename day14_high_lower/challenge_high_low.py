import random
from art import logo, vs
from game_data import data

print(logo)

#create generate_card to show the name, details and country from each question
def generate_card(random_number):
  card_name = random_number['name']
  card_description = random_number['description']
  card_country = random_number['country']
  return f'{card_name} is a {card_description} from {card_country}'

def comparator(prev_question, next_question, random_item):
  global should_continue
  followers_a = prev_question['follower_count']
  followers_b = next_question['follower_count']
  #ask to user to pick an option.
  asking = input('Who has more followers? Type "A" or "B": ').upper()
  is_a_greater = followers_a > followers_b
  is_b_greater = followers_b > followers_a
  response_a = asking == 'A'
  response_b = asking == 'B'
  
  if response_a:
    if is_a_greater:
      print('You are right!')
      new_question = random.choice(data)
    else:
      print('You are wrong!')
      should_continue = False
  elif response_b:
    if is_b_greater:
      print('You are right!')
    else:
      should_continue = False
      print('You are wrong!')
  else:
    print('Introduce a valid option: ')
    comparator()