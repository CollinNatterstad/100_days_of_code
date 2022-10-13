class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = []
        for item in self.menu:
            options.append(item.name)
        return options

    def item_exists(self,drinks=list,order_name=str,):
        """Checks to make sure an item exists"""
        if order_name in drinks:
            return True
        else:
            return False

    def get_characteristics(self, order_name = str, drinks = list):
        """Searches the menu for a particular drink by name. Returns that item"""
        pass_test = self.item_exists(order_name=order_name, drinks=drinks)

        if pass_test:       
            for item in self.menu:
                if item.name == order_name:
                    return item
        
        else:
            print("I'm sorry that item does not exist.")