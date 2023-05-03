from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_blackjack(hand_cards):
  hand_blackjack = [[11, 10], [10, 11]]
  for hand in hand_blackjack:
    if hand == hand_cards:
      print('Has Black Jack')
      return True

def calculate_scores(hand):
  hand_score = sum(hand)
  print(f'Hand score is: {hand_score}')
  return hand_score

def deal_card():
  set_hand = []
  random_hand = random.choices(cards, k=2)
  set_hand.extend(random_hand)
  print(set_hand)
  check_blackjack(set_hand)
  return set_hand


new_cards = deal_card()
calculate_scores(new_cards)

cards_computer = new_cards
cards_user = new_cards

print(f'cards computer: {cards_computer} ')
print(f'user computer: {cards_user} ')