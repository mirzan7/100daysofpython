raw_materials = {'water': 300, 'milk': 200, 'coffee': 100, 'money': 0}
coffee_list = {'espresso': 1.50, 'latte': 2.50, 'cappuccino': 3.00}


def check_price(choice, dollar):
    if coffee_list[choice] > dollar:
        print("Insufficient amount to process the coffee")
        return 1
    else:
        return 0


def convert_to_dollar(quarters, dimes, nickels, pennies):
    dollar = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return dollar


def change(choice, dollar):
    if coffee_list[choice] < dollar:
        return dollar - coffee_list[choice]
    else:
        return None


def chosen_drink(choice, dollar):
    if choice == "espresso" and check_price(choice, dollar) == 0:
        if raw_materials['water'] >= 50 and raw_materials['coffee'] >= 18:
            raw_materials['water'] -= 50
            raw_materials['coffee'] -= 18
            raw_materials['money'] += coffee_list[choice]
            return change(choice, dollar)
        else:
            print("Insufficient raw materials")
    if choice == "latte" and check_price(choice, dollar) == 0:
        if raw_materials['water'] >= 200 and raw_materials['coffee'] >= 24 and raw_materials['milk'] >= 150:
            raw_materials['water'] -= 200
            raw_materials['coffee'] -= 24
            raw_materials['milk'] -= 150
            raw_materials['money'] += 2.50
            return change(choice, dollar)
        else:
            print("Insufficient raw materials")
    if choice == "cappuccino" and check_price(choice, dollar) == 0:
        if raw_materials['water'] >= 250 and raw_materials['coffee'] >= 24 and raw_materials['milk'] >= 100:
            raw_materials['water'] -= 250
            raw_materials['coffee'] -= 24
            raw_materials['milk'] -= 100
            raw_materials['money'] += 3
            return change(choice, dollar)
        else:
            print("Insufficient raw materials")
    if choice == 'report':
        print(raw_materials)


choice = input("What would you like? (espresso/latte/cappuccino)").lower()
if choice == 'report':
    print(raw_materials)
    exit()
print("Please insert coins:")
quarters = int(input("How many quarters? "))
dimes = int(input("How many dimes? "))
nickels = int(input("How many nickels? "))
pennies = int(input("How many pennies? "))
dollar = convert_to_dollar(quarters, dimes, nickels, pennies)

change_amount = chosen_drink(choice, dollar)
if change_amount is not None:
    print(f"Here is your change: ${change_amount:.2f}")
