import random
from art import logo, vs
from game_data import data

print(logo)
should_continue = True
score = 0
text_b = random.choice(data)

#generate a random card from data
def generate_card(random_number):
  card_name = random_number['name']
  card_description = random_number['description']
  card_country = random_number['country']
  print (f'{card_name} is a {card_description} from {card_country}')

def get_followers(random_item):
  return random_item['follower_count']

def comparator(prev_question, next_question):
  global should_continue
  global score
  #ask the user for a guess
  guess = input('Who has more followers?: ').upper()
  is_prev_greater = get_followers(prev_question) > get_followers(next_question)
  is_next_greater = get_followers(prev_question) < get_followers(next_question)
  
  if guess == 'A':
    #check if is correct
    if is_prev_greater:
      #give feedback to user
      score += 1
      print(f'U are right. Score: {score}')
    else:
      should_continue = False
  if guess == 'B':
    if is_next_greater:
      score += 1
      print(f'U are right. Score: {score}')
    else:
      should_continue = False

while should_continue:
  text_a = text_b
  text_b = random.choice(data)
  while text_a == text_b:
    text_b = random.choice(data)
  
  generate_card(text_a)
  print(vs)
  generate_card(text_b) 
  comparator(text_a, text_b)
print(f'Game Over. Score: {score}') 