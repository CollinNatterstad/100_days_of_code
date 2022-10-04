import random
from completed.OHDC_11_art import logo
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

affirm = ['y','yes','yeah','start','yep']
deny = ['n','no','nah','nope','end']
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def build_hand(cards, number_drawn):
    draw = random.sample(cards,number_drawn)
    return draw

def add_a_card(player_cards):
    player_cards += build_hand(cards=player_cards, number_drawn=1)
    player_value = calculate(cards = player_cards)
    return  player_cards, player_value

def calculate(cards):
    count = 0
    for card in cards:
        count += card
    return count

def value_check(value,cards):
    if value > 21 and 11 in cards:
        value -= 10
        return True,value,cards
    elif value > 21:
        return False
    elif value < 21:
        return True

def dealer_wins(player_value, dealer_value):
    if dealer_value > player_value and dealer_value <= 21:
        return True
    elif player_value > 21:
        return True
    else:
        return False

def tie(player_value, dealer_value):
    if player_value == dealer_value:
        return True


def error_catch():
        continue_check = True
        while continue_check:

            print("You've entered a value that is not correct. Please ensure you've entered an appropriate value before you can start.")
            carry_on_check = input("Would you like to start over?").lower()
            
            if carry_on_check not in affirm or carry_on_check not in deny:
                print("Please enter an appropriate value.")
                if carry_on_check in deny:
                    print("Thanks for playing today!")
                else: 
                    continue_check = False
                    play_the_game()

def next_game():
        next_game = input("Would you like to play another hand? yes or no?\n").lower()
        if next_game in affirm:
            play_the_game()
        else:
            print("Thanks for playing today!")
            exit()

def play_the_game():
    #printing the starting logo
    print(logo)

    #would you like to play statement
    play = input("Are you ready to play a hand of blackjack? yes or no?\n").lower()

    #checking if the input variable exists within the previous terms. If it isn't one of those terms it is kicked out 
    if play not in affirm and play not in deny:
        error_catch(play=play)

    if play in affirm:

        player_cards = build_hand(cards=cards, number_drawn=2)
        dealer_cards = build_hand(cards=cards, number_drawn=2)      
        player_value = calculate(cards = player_cards)
        dealer_value = calculate(cards = dealer_cards)
        print(f"Your card's are: {player_cards[0]},{player_cards[1]}")
        print(f"The dealer's upcard is: {dealer_cards[0]}")
        print(F"The combined value of your current cards are: {player_value}")


        continue_draw = True
        while continue_draw:
            draw = input("Would you like to draw another card? yes or no?\n").lower()

            if draw in affirm:
                player_cards, player_value = add_a_card(player_cards=player_cards)
                print(f"Your Cards: {player_cards}\n Your Running Total: {player_value}")

            elif draw in deny:
                continue_draw = False

            if not value_check(value=player_value,cards=player_cards):
                continue_draw = False
                print("You Bust!")
                play_the_game()
        
        print(f"The Dealer's upcard is {dealer_cards[0]}, their downcard is {dealer_cards[1]}")

        while dealer_value <= 17:
            dealer_cards,dealer_value = add_a_card(player_cards=dealer_cards)
            print(f"The dealer draws a card. Their running total is {dealer_value}")

        if tie(player_value,dealer_value) and not dealer_wins(player_value,dealer_value):
            print(f"player's total:{player_value}")
            print(f"dealer's total:{dealer_value}")
            print("You Push!")
        
        elif dealer_wins(player_value=player_value, dealer_value=dealer_value): 
            print(f"player's total:{player_value}")
            print(f"dealer's total:{dealer_value}")
            print("The dealer wins, You Lose!")

        elif not dealer_wins(player_value=player_value, dealer_value=dealer_value):
            print(f"player's total:{player_value}")
            print(f"dealer's total:{dealer_value}")
            print("You win! Congrats")

        next_game()

    elif play in deny:
        print("Thanks for playing today!")
        exit()

play_the_game()