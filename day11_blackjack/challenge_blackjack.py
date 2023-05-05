from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_blackjack(hand_cards):
  hand_blackjack = [[11, 10], [10, 11]]
  for hand in hand_blackjack:
    if hand == hand_cards:
      return True
  return False

def calculate_scores(hand):
  hand_score = sum(hand)
  change_ace(hand_score, hand)
  return hand_score

def change_ace(score_hand, hand_cards):
  is_hand_burst = score_hand > 21
  if is_hand_burst:
    for i, card in enumerate(hand_cards):
      if card == 11:
        hand_cards[i] = 1
        break

def deal_card():
  set_hand = []
  random_hand = random.choices(cards, k=2)
  set_hand.extend(random_hand)
  if check_blackjack(set_hand):
    print('Blackjack!')
  return set_hand


def who_is_winner():
  is_user_greater = user_score > comp_score
  is_comp_greater = comp_score > user_score

  is_user_winner = check_blackjack(new_cards)
  is_comp_winner = check_blackjack(new_cards_comp)

  
  if is_user_winner or is_user_greater:
    print('Game Over: U Win!')
    
  elif is_comp_winner or is_comp_greater:
    print('Game Over: U Lose!')
  else:
    print('Game Over: Tie!')

def draw_new_card(hand_cards):
  ask_card = input(
    "Type 'y' if you want to get another card or 'n' if you donn't: "
  ).lower()
  
  if ask_card == 'y':
    extra_card = random.choice(cards)
    hand_cards.append(extra_card)

def end_game():
  draw_new_card(new_cards)
  while comp_score < 17:
    draw_new_card(new_cards_comp)
  who_is_winner()
  

new_cards = deal_card()
user_score =calculate_scores(new_cards)

new_cards_comp = deal_card()
comp_score = calculate_scores(new_cards_comp)

end_game()

print(f'cards computer: {new_cards_comp} ')
print(f'cards user: {new_cards} ')

print(f'user score: {user_score}')
print(f'comp score: {comp_score}')