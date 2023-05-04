from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_blackjack(hand_cards):
  hand_blackjack = [[11, 10], [10, 11]]
  for hand in hand_blackjack:
    if hand == hand_cards:
      return True

def calculate_scores(hand):
  set_hand = deal_card()
  hand_score = sum(hand)
  change_ace(hand_score, set_hand)
  return hand_score

def change_ace(score_hand, hand_cards):
  is_hand_burst = score_hand > 21
  blackjack_hand = check_blackjack(hand_cards)
  if is_hand_burst and  blackjack_hand:
    hand_cards = []
    return hand_cards.extend([10, 1])

def deal_card():
  set_hand = []
  random_hand = random.choices(cards, k=2)
  set_hand.extend(random_hand)
  check_blackjack(set_hand)
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

def end_game():
  has_winner = who_is_winner()
  is_burst = user_score > 21 or comp_score > 21
  
  if has_winner or is_burst:
    print('Burst!')
    return


new_cards = deal_card()
user_score =calculate_scores(new_cards)

new_cards_comp = deal_card()
comp_score = calculate_scores(new_cards_comp)

end_game()

print(f'cards computer: {new_cards_comp} ')
print(f'cards user: {new_cards} ')

print(f'user score: {user_score}')
print(f'comp score: {comp_score}')