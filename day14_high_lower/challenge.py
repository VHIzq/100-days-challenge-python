import random
from art import logo, vs
from game_data import data

print(logo)

number_a = random.choice(data)
number_b = random.choice(data)

should_continue = True
followers_a = number_a['follower_count']
followers_b = number_b['follower_count']

#generate a comparator() to review who has more followers
def comparator():
  global should_continue
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

def print_card(card_item, followers_item):
  print(card_item)
  print(followers_item)

#create generate_card to show the name, details and country from each question
def generate_card(random_number):
  card_name = random_number['name']
  card_description = random_number['description']
  card_country = random_number['country']
  return f'{card_name} is a {card_description} from {card_country}'

while should_continue:
  card_a = f'Compare A: {generate_card(random_number=number_a)}'
  card_b = f'Against B: {generate_card(random_number=number_b)}'

  print_card(card_a, followers_a)
  print(vs)
  print(card_b, followers_b)

  comparator()


#If option selected is true, then this is going to be compared to new question. Don't game over

#if pick a wrong option, game over



