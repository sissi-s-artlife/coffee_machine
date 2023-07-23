from dict import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def check_resources_sufficient(choice, resources):
    drink = MENU[choice]
    required_resources = drink["ingredients"]

    for resource, amount in required_resources.items():
        if resources[resource] < amount:
            print(f"Sorry, there is not enough {resource}.")
            return False

    return True


def calculate_coin(cost):
    quarters = int(input("Enter the number of quarters: ")) * 0.25
    dimes = int(input("Enter the number of dimes: ")) * 0.10
    nickels = int(input("Enter the number of nickels: ")) * 0.05
    pennies = int(input("Enter the number of pennies: ")) * 0.01
    coins_given = quarters + dimes + nickels + pennies
    return coins_given


def transaction_successful(cost, coins_given, required_resources):
    if coins_given < cost:
        print("Not enough money.Money refunded.")
        return False
    elif coins_given >= cost:
        if coins_given > cost:
            change = coins_given - cost
            print(f"Here is ${change:.2f} in change.")
        return True


def make_coffee(choice, required_resources):
    global profit
    for resource, amount in required_resources.items():
        resources[resource] -= amount
    print(f"Here is your {choice}. Enjoy!")
    profit += MENU[choice]["cost"]


def get_required_resources(choice):
    return MENU[choice]["ingredients"]


profit = 0

while True:
    choice = input(
        "What would you like? Espresso/Latte/Cappuccino? You can type 'off' to turn off the machine or type 'report' to report resources: ").lower()

    if choice == "off":
        print("Goodbye!")
        break

    elif choice == "report":
        report()
    elif choice in MENU:
        if check_resources_sufficient(choice, resources):
            cost = MENU[choice]["cost"]
            coins_given = calculate_coin(cost)
            if transaction_successful(cost, coins_given, get_required_resources(choice)):
                make_coffee(choice, get_required_resources(choice))
    else:
        print("Invalid choice. Please try again.")



