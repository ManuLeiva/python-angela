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
}

def main():
    user_input = ""
    while user_input != "off":
        user_input = input("What whould you like? ")
        if user_input == "off":
            return print("Good bye")
        elif user_input == "report":
            print("Water:", resources["water"])
            print("Milk:", resources["milk"])
            print("Coffee:", resources["coffee"])
            print("Money:") ## TODO: check the money 
        elif user_input == "coffee":
            if resources["water"] >= MENU["espresso"]['ingredients']['water'] and resources["coffee"] >= MENU["espresso"]['ingredients']['coffee']:
                print("Here is your espresso")
            else:
                if resources["water"] <= MENU["espresso"]['ingredients']['water']:
                    print("Sorry, there's not enough water")
                elif resources["coffee"] <= MENU["espresso"]['ingredients']['coffee']:
                    print("Sorry, there's not enough coffee")
        elif user_input == "latte":
            if resources["water"] >= MENU["latte"]['ingredients']['water'] and resources["coffee"] >= MENU["latte"]['ingredients']['coffee'] and resources["milk"] >= MENU["latte"]['ingredients']['milk']:
                print("Here is your latte")
            else:
                if resources["water"] <= MENU["latte"]['ingredients']['water']:
                    print("Sorry, there's not enough water")
                elif resources["coffee"] <= MENU["latte"]['ingredients']['coffee']:
                    print("Sorry, there's not enough coffee")
                elif resources["milk"] <= MENU["latte"]['ingredients']['milk']:
                    print("Sorry, there's not enough milk")
        elif user_input == "cappuccino":
            if resources["water"] >= MENU["cappuccino"]['ingredients']['water'] and resources["coffee"] >= MENU["cappuccino"]['ingredients']['coffee'] and resources["milk"] >= MENU["cappuccino"]['ingredients']['milk']:
                print("Here is your cappuccino")
            else:
                if resources["water"] <= MENU["cappuccino"]['ingredients']['water']:
                    print("Sorry, there's not enough water")
                elif resources["coffee"] <= MENU["cappuccino"]['ingredients']['coffee']:
                    print("Sorry, there's not enough coffee")
                elif resources["milk"] <= MENU["latte"]['ingredients']['milk']:
                    print("Sorry, there's not enough milk")
main()
