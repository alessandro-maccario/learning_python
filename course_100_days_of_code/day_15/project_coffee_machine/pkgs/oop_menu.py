class MenuItem:
    def __init__(
        self, name: str, cost: float, water: int, milk: int, coffee: int
    ) -> None:
        """Models each menu item. Each menu item contains the name, the cost, the water, the milk and the coffee.

        Parameters
        ----------
        name : str
            The name of the drink. e.g.: 'espresso'
        cost : float
            The price of the drink. e.g.: 1.5
        ingredients : dict
            The ingredients and amounts required to make the drink. e.g. {'water': 100, 'milk': 0, 'coffee': 16}
        """
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string. e.g. 'espresso/latte/cappuccino'"""
        options = "|"
        for item in self.menu:
            options += f" {item.name} | "
        return options

    def find_drink(self, order_name):
        """
        Parameter
        ---------
        order_name: (str)
            The name of the drinks order.
            Searches the menu for a particular drink by name.

        Returns
        -------
            A MenuItem object if it exists, otherwise returns None.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, item not available.")
