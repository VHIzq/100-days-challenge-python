from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_blackjack(hand_cards):
    hand_blackjack = [[11, 10], [10, 11]]
    for hand in hand_blackjack:
        if hand == hand_cards:
            return True
    return False  # Agregado para manejar caso de que no sea blackjack.


def calculate_scores(hand):
    hand_score = sum(hand)
    # La función debe recibir el mismo argumento que se usó para llamarla.
    change_ace(hand_score, hand)
    return hand_score


def change_ace(score_hand, hand_cards):
    if score_hand > 21:
        for i, card in enumerate(hand_cards):
            if card == 11:
                hand_cards[i] = 1
                break


def deal_card():
    set_hand = []
    random_hand = random.choices(cards, k=2)
    set_hand.extend(random_hand)
    if check_blackjack(set_hand):
        print("Blackjack!")  # Agregado para indicar que hay blackjack.
    return set_hand


def who_is_winner(user_score, comp_score, new_cards, new_cards_comp):
    is_user_greater = user_score > comp_score
    is_comp_greater = comp_score > user_score

    is_user_winner = check_blackjack(new_cards)
    is_comp_winner = check_blackjack(new_cards_comp)

    if is_user_winner or is_user_greater:
        print('Game Over: U Win!')
    elif is_comp_winner or is_comp_greater:
        print('Game Over: U Lose!')
    else:
        print("It's a tie!")  # Agregado para manejar caso de empate.


def draw_new_card(hand_cards):
    ask_card = input(
        'Type "y" if you want to get another card or "n" if you don\'t: ')
    if ask_card.lower() == 'y':
        extra_card = random.choice(cards)
        hand_cards.append(extra_card)


def end_game():
    new_cards = deal_card()
    user_score = calculate_scores(new_cards)
    new_cards_comp = deal_card()
    comp_score = calculate_scores(new_cards_comp)

    print(f'Computer cards: {new_cards_comp}')
    print(f'Your cards: {new_cards}')
    print(f'Your score: {user_score}')
    draw_new_card(new_cards)
    while comp_score < 17:
        draw_new_card(new_cards_comp)
        comp_score = calculate_scores(new_cards_comp)
        print(f'Computer cards: {new_cards_comp}')
        print(f'Computer score: {comp_score}')
    who_is_winner(user_score, comp_score, new_cards, new_cards_comp)


end_game()
