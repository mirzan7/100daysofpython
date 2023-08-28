from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_live = True

while is_live:
    choice = input(f"What would you like {menu.get_items()} ?  ")
    if choice.lower() == "off":
        is_live = False
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)

