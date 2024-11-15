
# Coffee Machine Project

A Python-based simulation of a coffee machine, demonstrating object-oriented programming concepts and user interactivity through the console.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
This project simulates a coffee machine's functionalities, allowing users to order coffee, process payments, and manage resources. It uses a modular approach with separate classes for the menu, coffee maker, and payment system.

## Features
- **Order Coffee:** Choose from options like latte, espresso, and cappuccino.
- **Resource Management:** Check ingredient levels and ensure sufficient supply.
- **Payment Processing:** Accepts coins, validates payments, and returns change.
- **Reports:** Display current resources and total profits.
- **Power Control:** Turn off the machine when not in use.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/coffee-machine.git
   cd coffee-machine
   ```

2. Ensure you have Python 3.x installed on your system.

3. Run the main program:
   ```bash
   python main.py
   ```

## Usage
1. Launch the program by running `main.py`.
2. Follow the on-screen prompts:
   - Enter a coffee name (`latte`, `espresso`, `cappuccino`) to order a drink.
   - Enter `report` to view the resource and profit status.
   - Enter `off` to turn off the coffee machine.

---

## Code Structure
### **menu.py**
- Defines the `Menu` and `MenuItem` classes.
- `MenuItem` models a coffee drink, including ingredients and cost.
- `Menu` manages the list of drinks and provides functionalities to fetch options or search for a drink.

### **coffee_maker.py**
- Defines the `CoffeeMaker` class.
- Manages resources like water, milk, and coffee.
- Provides methods to check ingredient sufficiency and prepare coffee.

### **money_machine.py**
- Defines the `MoneyMachine` class.
- Handles coin input, calculates totals, validates payments, and tracks profits.

### **main.py**
- Acts as the entry point for the program.
- Implements the logic for user interaction and coordinates functionality among classes.

---

## Example Interaction
1. **Start the Application:**
   ```plaintext
   Coffee Machine
   Water: 300ml
   Milk: 200ml
   Coffee: 100g
   Money: $0
   ```
2. **Order a Drink:**
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
3. **Check Reports:**
   ```plaintext
   Water: 100ml
   Milk: 50ml
   Coffee: 76g
   Money: $2.5
   ```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

