class MoneyMachine:
    # --- CONSTANTS --- #
    CURRENCY = "$"

    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    # --- METHODS --- #
    def __init__(self) -> None:
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit e.g. Money: $0"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.money_received

    def make_payment(self, cost):
        """
        Parameter
        ---------
        cost: (float)
            The cost of the drink.

        Returns
        -------
        True when payment is accepted, or False if insufficient. e.g. False
        """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your change, {self.CURRENCY}{change}")
            self.profit += cost
            self.money_received = 0  # to initialize the money_received again
            return True
        else:
            print("Sorry, not enough money, insert more coins.")
            self.money_received = 0
            return False
