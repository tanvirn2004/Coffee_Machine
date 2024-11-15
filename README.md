
# Coffee Machine Project

A Python-based simulation of a coffee machine, designed to demonstrate object-oriented programming principles and provide a simple console-based interface for user interaction.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Detailed Code Documentation](#detailed-code-documentation)
  - [menu.py](#menupy)
  - [coffee_maker.py](#coffee_makerpy)
  - [money_machine.py](#money_machinepy)
  - [main.py](#mainpy)
- [Example Interaction](#example-interaction)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project simulates the functionality of a coffee machine. Users can choose from a menu of coffee options, make payments, and receive their drink while the system tracks resource usage and profits.

## Features
- Order coffee (latte, espresso, cappuccino).
- Simulate coin-based payments and provide change.
- Track machine resources like water, milk, and coffee.
- Display a detailed report of resources and profit.
- Turn off the machine when done.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coffee-machine.git
   cd coffee-machine
   ```

2. Ensure Python 3.x is installed.

3. Run the program:
   ```bash
   python main.py
   ```

---

## Usage
1. Run `main.py` to start the program.
2. Enter your choice:
   - Order coffee by typing its name (e.g., "latte").
   - Enter `report` to view resource and profit details.
   - Enter `off` to stop the machine.

---

## Detailed Code Documentation

### menu.py

#### `MenuItem` Class
Represents a single menu item (e.g., latte, espresso).
- **Attributes:**
  - `name`: The name of the drink.
  - `cost`: The price of the drink.
  - `ingredients`: A dictionary containing the required quantities of water, milk, and coffee.
- **Purpose:** Provides a structure for defining individual drinks.

#### `Menu` Class
Manages the list of available drinks.
- **Attributes:**
  - `menu`: A list of `MenuItem` objects.
- **Methods:**
  - `get_items()`: Returns a comma-separated string of all drink names in the menu.
  - `find_drink(order_name)`: Searches for and returns a `MenuItem` object matching the given name. Returns `None` if the item is not found.

---

### coffee_maker.py

#### `CoffeeMaker` Class
Models the functionality of the coffee machine.
- **Attributes:**
  - `resources`: A dictionary tracking the available quantities of water, milk, and coffee.
- **Methods:**
  - `report()`: Prints the current levels of all resources.
    ```python
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    ```
    **Explanation:** Displays the available resources in the machine.
  - `is_resource_sufficient(drink)`: Checks if the machine has enough resources to prepare the selected drink.
    ```python
    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    ```
    **Explanation:** Loops through the drink's ingredients and compares them with the available resources.
  - `make_coffee(order)`: Deducts the required ingredients from the machine's resources and confirms coffee preparation.

---

### money_machine.py

#### `MoneyMachine` Class
Handles all monetary transactions and keeps track of profits.
- **Attributes:**
  - `CURRENCY`: Specifies the currency symbol (`$`).
  - `COIN_VALUES`: Defines the values of quarters, dimes, nickels, and pennies.
  - `profit`: Tracks the total money earned by the machine.
  - `money_received`: Temporary storage for the money inserted by the user.
- **Methods:**
  - `report()`: Prints the total profit earned.
  - `process_coins()`: Prompts the user to insert coins and calculates the total value.
    ```python
    def process_coins(self):
        self.money_received = 0
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}?: "))
            self.money_received += count * self.COIN_VALUES[coin]
        return self.money_received
    ```
    **Explanation:** Iterates through each coin type, collects the count from the user, and calculates the total amount.
  - `make_payment(cost)`: Checks if the inserted amount covers the cost, provides change if necessary, and updates profits.

---

### main.py

Acts as the program's entry point and coordinates interactions between the `Menu`, `CoffeeMaker`, and `MoneyMachine` classes.
- **Workflow:**
  1. Initializes objects for `Menu`, `CoffeeMaker`, and `MoneyMachine`.
  2. Runs a loop to interact with the user:
     - Displays available menu options.
     - Processes user commands (`off`, `report`, or a coffee name).
     - Checks resource sufficiency and processes payments.
     - Prepares the drink if all conditions are met.

---

## Example Interaction
```plaintext
What would you like to have (latte, espresso, cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---