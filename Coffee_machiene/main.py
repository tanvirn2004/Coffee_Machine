from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machiene = MoneyMachine()
coffee_make = CoffeeMaker()
menu = Menu()                        ##Recalling the functions
coffee_make.report()
money_machiene.report()
is_one = True

while is_one:
    options= menu.get_items()
    choice = input(f"What would you like to have{options}: ")
    if choice == "off" or choice =="Off":        #Creating function to turn off machine
        print("Machine turned off")
        is_one = False
    elif choice == "report":              #Type report to get all information about resources you have
        print("Here's the report")
        coffee_make.report()
        money_machiene.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink) and money_machiene.make_payment(drink.cost):
            coffee_make.make_coffee(drink)


