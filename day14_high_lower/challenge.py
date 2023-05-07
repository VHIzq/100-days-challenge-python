import random
from art import logo, vs
from game_data import data

print(logo)
""" 'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
"""

#create generate_card to show the name, details and country from each question
number_a = random.choice(data)
number_b = random.choice(data)

def generate_card(random_number):
  card_name = random_number['name']
  card_description = random_number['description']
  card_country = random_number['country']

  return f'{card_name} is a {card_description} from {card_country}'

card_a = f'Compare A: {generate_card(random_number=number_a)}'
card_b =f'Against B: {generate_card(random_number=number_b)}'

followers_a = number_a['follower_count']
followers_b = number_b['follower_count']

print(card_a)
print(followers_a)
print(vs)
print(card_b)
print(followers_b)

#ask to user to pick an option.
asking = input('Who has more followers? Type "A" or "B": ').upper()
  
#generate a comparator() to review who has more followers
def comparator():
  is_a_greater = followers_a > followers_b
  is_b_greater = followers_b > followers_a
  if asking == 'A':
    if is_a_greater:
      print('You are right!')
    else:
      print('You are wrong!')
  elif asking == 'B':
    if is_b_greater:
      print('You are right!')
    else:
      print('You are wrong!')
  else:
    print('Introduce a valid option')
    
comparator()
#If option selected is true, then this is going to be compared to new question. Don't game over

#if pick a wrong option, game over



