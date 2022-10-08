import enum
import re


drinks = [
{   "Name":"Espresso",
    "Water(mL)": 50,
    "Milk(mL)": 0,
    "Coffee(g)": 18,
    "Price": 1.50
},
{
    "Name":"Latte",
    "Water(mL)": 200,
    "Milk(mL)":150,
    "Coffee(g)": 24,
    "Price":2.50
},
{
    "Name":"Cappuccino",
    "Water(mL)": 250,
    "Milk(mL)": 100,
    "Coffee(g)": 24,
    "Price":3.50
}]

Machine_capacity = {
    "Water(mL)": 1000,
    "Milk(mL)": 1000,
    "Coffee(g)": 500,
}

#Input request
#program needs to print report. What resources it has left.
#Check that resources are sufficient for the drink itself.
#you should input how many coins are provided. What the value of each coin is. and if it is sufficient to cover the cost of the item. 

#intro statement pulling drink type. returning in title case to match the drink in dictionary. 
def intro():
    print("\nWelcome to the Coffee Machine!\n\nYou have three options to choose from: an Espresso, a Latte, and a Cappuccino.")
    print("If you'd like to verify the current resource contents of the machine type 'report'.\n")

    choices = ['espresso','latte','cappuccino','report']

    while True:
        user_choice = input("What would you like to purchase today?\n").title()

        if user_choice.lower() not in choices:
            print("Please ensure that you've selected the correct drink.")

        else:
            return user_choice.title()

#function that accesses and returns the contents of a specified dictionary that matches a user input. 
def drink_characteristics(drinks,user_choice):

    for items in drinks:

        if items["Name"] == str(user_choice).title():    
        
            name = items["Name"]
            water = items["Water(mL)"]
            milk = items["Milk(mL)"]
            coffee = items["Coffee(g)"]
            price = items["Price"]

            return name, water, milk, coffee, price

#instead of refunding if resource capacity is low. Refilled based on boolean. 
def refilling_resources(machine_capcity, refill=False):

    if refill == True:
        water_available = machine_capcity["Water(mL)"]
        milk_available = machine_capcity["Milk(mL)"]
        coffee_available = machine_capcity["Coffee(g)"]
        

        return water_available, milk_available, coffee_available

#convert user input into a dollar amount. 
def amount_paid():
    quarter_value = .25
    quarter_quantity = int(input("How many quarters would you like to use?"))
    amount_quarter = quarter_value*quarter_quantity

    dime_value = .1
    dime_quantity = int(input("How many dimes would you like to use?"))
    amount_dime = dime_value*dime_quantity

    nickle_value = .05
    nickle_quantity = int(input("How many nickles would you like to use?"))
    amount_nickle = nickle_value*nickle_quantity

    total_paid = amount_quarter + amount_dime+ amount_nickle
    
    return total_paid

def compare_price(price_drink,total_paid):
    if total_paid >= price_drink:
        change = total_paid - price_drink
        return True, change
    
    elif total_paid < price_drink:
        remaining_balance = price_drink-total_paid
        return False, remaining_balance

def next_drink():
    user_choice = input("Would you like to purchase another drink today?").lower()

    deny = ['n','no','nope','end','nah']

    if user_choice in deny:
        print("Thanks for buying coffee today!")
        return True

#The ACTUAL FUNCTION
def coffee_machine():

    water_available = 0
    milk_available = 0
    coffee_available = 0
   
    carry_on = True
    while carry_on:
        
        #refill condition set refill to true and pass it into the 
        if water_available == 0 and milk_available == 0 and coffee_available == 0:
            water_available, milk_available, coffee_available = refilling_resources(Machine_capacity,refill = True)

        elif water_available <= 250 or milk_available <= 150 or coffee_available <= 24:
            water_available, milk_available, coffee_available = refilling_resources(Machine_capacity,refill = True)
            print("\nPlease wait while we refill the Coffee Machine")
        
        user_choice = intro()

        if user_choice.lower() == "report":
            print(f"\nThere are {water_available} mL of water, {milk_available} mL of milk, and {coffee_available} g of coffee remaining.\n")
        
        else:
            name_drink,water_required,milk_required,coffee_required,price_drink = drink_characteristics(drinks=drinks, user_choice=user_choice)

            water_available -= water_required
            milk_available -= milk_required
            coffee_available -= coffee_required 

            print(f"You've Purchased a {name_drink}, that will cost ${price_drink}")

            remaining = False
            while not remaining:
                total_paid = amount_paid()
                remaining, balance = compare_price(total_paid=total_paid,price_drink=price_drink)
                
                if remaining == False:
                    print(f"You need to insert {balance} more dollars for this drink.")
                
                else:
                    print(f"You're change comes to ${balance}.")
            
            go_again = next_drink()

            if go_again:
                carry_on = False
                exit()

coffee_machine()