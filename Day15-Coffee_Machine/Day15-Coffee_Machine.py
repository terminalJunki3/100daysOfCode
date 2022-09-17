import time
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def show_resources():
    """Prints all of the resources stored in the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {resources['money']}")


def collect_money():
    """ Converts input into USD and returns total """
    quarters = int(input("how many quarters: ")) * .25
    dimes = int(input("how many dimes: ")) * .1
    nickels = int(input("how many nickels: ")) * .05
    pennies = int(input("how many pennies: ")) * .01
    return quarters + dimes + nickels + pennies


def check_resources(choice):
    """Checks to see if there are enough resources"""
    for item in choice:
        if choice[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def serve(choice, ingredients, payment, resources_list):
    """Updates resources and bank, then servers cofffee"""
    for item in ingredients:
        resources_list[item] -= ingredients[item]

    refund = payment - MENU[choice]['cost']
    resources_list['money'] += MENU[choice]['cost']
    print(f"Here is ${refund} in change.")
    print(f"Here is your {choice}")


def fill():
    """sets the resource values back to default"""
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100

system_on = True
while system_on:
    coffee_choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    if coffee_choice == "fill":
        fill()
    if coffee_choice == "report":
        show_resources()
    if coffee_choice == 'off':
        print("turning off...")
        time.sleep(3)
        try:
            os.system('clear')
        except:
            os.system('cls')
        print("System off. Good Bye")
        system_on = False

    if coffee_choice in MENU:
        cost = MENU[coffee_choice]['cost']
        drink = MENU[coffee_choice]['ingredients']
        has_resources = check_resources(drink)
        if has_resources:
            money = collect_money()
            if money < cost:
                print("Sorry, not enough money. Money refunded.")
            else:
                serve(coffee_choice, drink, money, resources)


