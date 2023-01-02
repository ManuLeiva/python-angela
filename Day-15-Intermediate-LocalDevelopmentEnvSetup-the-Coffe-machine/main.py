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
    user_input = input("What whould you like?")
    if user_input == "off":
        return print("Good bye")
    elif user_input == "report":
        print("Water:", resources["water"])
        print("Milk:", resources["milk"])
        print("Coffee:", resources["coffee"])
        print("Money:") ## TODO: check the money 
    elif user_input == "espresso":
        print("hello")
    elif user_input == "latte":
        print("hello")
    elif user_input == "cappuccino":
        print("hello")


main()