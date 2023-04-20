from cofee_machine_specification import *


def main():
    profit = 0
    machine_working = True
    while machine_working:
        user_choose = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choose == 'off':
            machine_working = turn_off_machine()
            print("Turning off the Coffee Machine...")
        elif user_choose == 'report':
            print_report(profit)
        elif user_choose == 'espresso':
            if check_for_coffee(user_choose, ['water', 'coffee']):
                profit = process_coins(user_choose, ['water', 'coffee'], profit)
        elif user_choose == "latte":
            if check_for_coffee(user_choose, ['water', 'milk', 'coffee']):
                profit = process_coins(user_choose, ['water', 'milk', 'coffee'], profit)
        elif user_choose == "cappuccino":
            if check_for_coffee(user_choose, ['water', 'milk', 'coffee']):
                profit = process_coins(user_choose, ['water', 'milk', 'coffee'], profit)
        else:
            print("Coffee Machine does not have this comand.")


def turn_off_machine():
    machine_working = False
    return machine_working


def print_report(profit):
    print(f"""
    Water: {resources["water"]}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}gr
    Money: ${profit}
    """)


def check_for_coffee(name_of_coffee, ingredients):
    for i in ingredients:
        if resources[i] < MENU[name_of_coffee]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False

    return True


def process_coins(name_of_coffe, ingredients, profit):
    print("Insert the coins.")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    coffee_cost = MENU[name_of_coffe]['cost']
    in_change = 0

    if total < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        for i in ingredients:
            resources[i] -= MENU[name_of_coffe]['ingredients'][i]

        in_change = total - coffee_cost
        profit += coffee_cost
        print(f"Here is ${in_change:.2f} dollars in change")

        print(f"Here is your {name_of_coffe}. Enjoy!")

    return profit


if __name__ == "__main__":
    main()
