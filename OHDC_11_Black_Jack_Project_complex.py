from OHDC_11_art import logo
import random

print(logo)

'''goal is to make a black jack game 
primary functionality 

the game
continue playing component. 
single deck... 52 cards 4 suits 2->a
'''
#build a 52 card deck with a value for each suit type.
def build_deck():
    suits = ['sp', 'di','hr','cl']
    face_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = []

    for values in suits:
        for value in face_values:
            deck.append(value + values)
    return deck

# draw card from the deck. 
def draw_card(deck,number_of_cards):
    


def play_hand(deck):
    face_cards = ['J', 'Q','K','A']
    card_value_player = 0
    card_value_dealer = 0 

    player_hand = random.sample(deck,2)
    print(f"The Player's Hand is: {player_hand[0]} and {player_hand[1]}")
    
    dealer_hand = random.sample(deck,2)
    print(f"The Dealer's up card is: {dealer_hand[0]}")


    for items in player_hand:
        carry_on = True
        while carry_on:

            if items[0] in face_cards:

                if items[0] in face_cards[0:2]:
                    print(items[0])
                    card_value_player += 10
                    print(card_value_player)

                elif items[0] == 'A':
                    print(items[0])
                    if card_value_player >21:
                        card_value_player += 1
                    else:
                        card_value_player +=11
            
            else:
                card_value_player += int(items[0])
                print(card_value_player)

            if card_value_player < 21:
                print(card_value_player)
                carry = input("Would you like another card? y/n").lower()
                
                if carry == 'n':
                    carry_on = False
                



            








deck = build_deck()

play_hand(deck = deck)