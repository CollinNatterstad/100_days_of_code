from OHDC_16_Coffee_Machine_menu import Menu, MenuItem
from OHDC_16_Coffee_machine import CoffeeMaker
from OHDC_16_Coffee_Machine_Money import MoneyMachine

def user_check():

    affirm = ['y','yes','yeah','yah','yep']
    deny = ['n','no','nope','nah']
    reask = True
    user_choice = input("Would you like another coffee? Yes or No?").lower()
    while reask:
        if user_choice not in affirm and user_choice not in deny:
            print("Please make sure you entered yes or no")
        else:
            if user_choice in affirm:
                reask = False
                return True
            elif user_choice in deny:
                return False

def drink_coffee():
    drink_menu = Menu()
    coffee_order = CoffeeMaker()
    coffe_money = MoneyMachine()
    
    while True:

        drinks = drink_menu.get_items()
        capacity = coffee_order.report()
        profit  = coffe_money.report()

        order_name = input(f"What drink would you like? You can purchase a {drinks[0]}, an {drinks[1]}, or a {drinks[2]}?\n").lower()

        drink_choice = drink_menu.get_characteristics(order_name = order_name, drinks= drinks)

        can_make = coffee_order.is_resource_sufficient(drink_choice)
        if can_make:
            payment = coffe_money.make_payment(cost=drink_choice.cost)
            
            if payment:
                order_up = coffee_order.make_coffee(drink_choice)
                profit = coffe_money.report()

        user_choice = user_check()

        if user_choice != True:
            print("Thank you for purchasing a Coffee with us today!")
            exit()

drink_coffee()