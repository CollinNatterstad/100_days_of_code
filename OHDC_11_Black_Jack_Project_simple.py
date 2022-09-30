import random
from tracemalloc import start
from OHDC_11_art import logo



'''
logo

your cards: [cards]
computer's first card: card
Type 'y' to get another card, type 'n' to pass:
your final hand: [cards]
comuter's final hand [cards]
Result 
Do you want to play another game of blackjack? type 'y' or 'n'
recursive call > call function with y condition.

'''

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def starting_cards(cards, number_drawn):
    draw = random.sample(cards,number_drawn)
    return draw


player_cards = starting_cards(cards=cards, number_drawn=2)
dealer_cards = starting_cards(cards=cards, number_drawn=2)