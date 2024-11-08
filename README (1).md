
# Coffee Maker Project

This project simulates a coffee vending machine that takes orders, processes payments, and manages resources. It's written in Python and is an ideal project to understand classes, objects, and basic simulation of real-life operations in programming.

## Project Structure

The project is organized into four main Python files:

- **main.py**: The main file that initializes and runs the coffee machine simulation. It imports and uses functions from the other three modules.
- **menu.py**: Defines the `Menu` and `MenuItem` classes, modeling the coffee menu and individual drinks with ingredients and prices.
- **coffee_maker.py**: Contains the `CoffeeMaker` class, which manages the resources (water, milk, coffee), checks resource sufficiency, and makes the coffee.
- **money_machine.py**: Implements the `MoneyMachine` class, handling the monetary transactions, calculating total from coin inputs, and verifying if the customer has inserted enough money for their drink.

## Features

- **Menu Management**: Displays available coffee options and allows the user to select a drink.
- **Resource Tracking**: Tracks quantities of water, milk, and coffee, and checks if enough resources are available for a selected drink.
- **Payment Processing**: Accepts coin inputs (quarters, dimes, nickels, and pennies), calculates the total, and verifies payment.
- **Order Fulfillment**: Deduces resources from the coffee maker’s storage and serves the coffee.

## Classes Overview

- `MenuItem`: Represents an individual drink on the menu with ingredients and cost.
- `Menu`: Stores a list of available drinks and provides methods to retrieve and find drinks by name.
- `CoffeeMaker`: Manages resources, checks if resources are sufficient, and deducts ingredients for each coffee order.
- `MoneyMachine`: Handles coin input, calculates payment, and checks if sufficient payment has been made.

## How to Run

1. Clone the repository to your local machine.
2. Make sure Python 3 is installed.
3. Run the main file:
   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to order a coffee, insert coins, and receive your drink if payment and resources allow.

## Example Output

```
What would you like? (latte/espresso/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is your latte ☕️. Enjoy!
```

## Future Improvements

- Add more drink options.
- Implement a graphical interface.
- Add a maintenance mode to refill resources or empty the money machine.

## License

This project is licensed under the MIT License.
