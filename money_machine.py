class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        self.money_received = 0  # Reset the money received
        print("Please insert coins.")

        for coin in self.COIN_VALUES:
            while True:
                try:
                    count = int(input(f"How many {coin}?: "))
                    if count < 0:
                        print("Please enter a non-negative number.")
                        continue
                    self.money_received += count * self.COIN_VALUES[coin]
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
