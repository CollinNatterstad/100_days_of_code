from pickle import TRUE
from replit import clear
from OHDC_9_Art import logo

bidders = {}

def new_bidder(name,bid):
    bidders[name] = bid

#setting flag for while loop condition
should_continue = True
while should_continue:
    #clear previous contents
    clear()
    #print logo/welcome
    print(logo)
    print("Welcome to the silent auction")
    #get inputs from users
    name = input("What is your Name? \n").lower()
    bid = int(input("What is your bid?\n$"))

    #pass inputs into funciton created above. 
    new_bidder(name=name, bid=bid)
    continue_bidding = input("Are there any other bidders? Type yes or no?\n").lower()
 
    if continue_bidding == 'no':
        should_continue = False
clear()
winner = max(bidders,key = bidders.get)
value = bidders[winner]
print(f'Congratulations {winner}, you won the silent action with a bid of ${value}')

