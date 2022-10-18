from turtle import clear
from coffe_menu import menu
import time


def check_resources():
    """Function to check if there are enough resources"""
    if int(menu[drink]["Water"]) > int(report["Water"]):
        return "Sorry. There is not enough water in machine."
    elif int(menu[drink]["Milk"]) > int(report["Milk"]):
        return "Sorry. There is not enough milk in the machine."
    elif int(menu[drink]["Coffee"]) > int(report["Coffee"]):
        return "Sorry. There is not enough coffee in the machine"
    else:
        return 0


def check_money():
    difference1 = total_sum - float(menu[drink]["Money"])
    if total_sum < float(menu[drink]["Money"]):
        return "Sorry that's not enough money. Money refunded!"
    elif total_sum > float(menu[drink]["Money"]):
        return round(difference1, 3)
    else:
        return "Right on point. Penny on penny. No change!"


def after_buy(profit=0):
    global report
    for item in report:
        report[item] -= menu[drink][item]
    profit += float(menu[drink]["Money"])
    report["Money"] = profit


report = {
    "Water": 300,
    "Milk": 300,
    "Coffee": 300,
    "Money": 0,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
while True:
    drink = input("What would you like to drink? Espresso/latte/cappuccino? ").title()
    if drink == "Espresso" or drink == "Latte" or drink == "Cappuccino" or drink == "Report":
        while drink == "Report":
            print(report)
            drink = input("What would you like to drink? Espresso/latte/cappuccino? ").title()
        if drink == "Off":
            clear()
            print("Coffee machine has turned off")
            break
    else:
        print(f"No coffee found as {drink}.")
        break
    if check_resources() != 0:  # Checking if we have enough resources to make coffee
        print(check_resources())
        break
    print("Please insert in the money: ")
    no_quarters = int(input("Quarters: "))
    no_dimes = int(input("Dimes: "))
    no_nickles = int(input("Nickles: "))
    no_pennies = int(input("Pennies: "))
    total_sum = no_quarters * quarters + no_dimes * dimes + no_nickles * nickles + no_pennies * pennies  # User paid
    difference = total_sum - float(menu[drink]["Money"])  # Exchange
    cost = float(menu[drink]["Money"])
    if total_sum < cost:
        print(check_money())
        break
    elif total_sum == cost or total_sum > cost:
        if total_sum > cost:
            print(f"Here is your {drink} ☕️. Enjoy it!\n")
            time.sleep(2.5)
            print(f"Oh.. and here is your exchange, ${check_money()}")
            after_buy()
        else:
            print(f"Here is your {drink} ☕️. Enjoy it!\n")
            time.sleep(2.5)
            print(f"Oh.. and, yeah, there is no exchange, you paid right on point ;) ")
            after_buy()
            drink = input("What would you like to drink? Espresso/latte/cappuccino? ").title()
