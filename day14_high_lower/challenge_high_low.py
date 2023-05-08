import random
from art import logo, vs
from game_data import data

print(logo)

#create generate_card to show the name, details and country from each question
number_a = random.choice(data)
number_b = random.choice(data)

def generate_card(random_number):
  card_name = random_number['name']
  card_description = random_number['description']
  card_country = random_number['country']

  return f'{card_name} is a {card_description} from {card_country}'

card_a = f'Compare A: {generate_card(random_number=number_a)}'
card_b = f'Against B: {generate_card(random_number=number_b)}'

followers_a = number_a['follower_count']
followers_b = number_b['follower_count']

def print_card(card_item, followers_item):
  print(card_item)
  print(followers_item)

print_card(card_a, followers_a)
print(vs)
print_card(card_b, followers_b)

#ask to user to pick an option.
asking = input('Who has more followers? Type "A" or "B": ').upper()
  
#generate a comparator() to review who has more followers
def comparator():
  is_a_greater = followers_a > followers_b
  is_b_greater = followers_b > followers_a
  response_a = asking == 'A'
  response_b = asking == 'B'
  
  if response_a:
    if is_a_greater:
      print('You are right!')
    else:
      print('You are wrong!')
  elif response_b:
    if is_b_greater:
      print('You are right!')
    else:
      print('You are wrong!')
  else:
    print('Introduce a valid option: ')


#If option selected is true, then this is going to be compared to new question. Don't game over
if comparator():
  print(card_b)
  
  print(vs)
  
  number_c = random.choice(data)
  card_c = generate_card(random_number=number_c)
  print(card_c)
  followers_c = number_c['follower_count']


#if pick a wrong option, game over



