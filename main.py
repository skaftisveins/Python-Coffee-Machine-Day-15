from data import MENU, resources, profit

# 1b. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
still_serving = True

# 5c. Process coins.
PENNIES = 0.01
NICKLES = 0.05
DIMES = 0.1
QUARTERS = 0.25

# 4b. Check resources are sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


# 5b. Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    try:
        print("Please insert coins")
        total = int(input("How many quarters?: ")) * QUARTERS
        total += int(input("How many dimes?: ")) * DIMES
        total += int(input("How many nickles?: ")) * NICKLES
        total += int(input("How many pennies?: ")) * PENNIES
        return total
    except print("Did you enter a valid number?"):
        pass


# 6b. Check transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded..")
        return False


# 7b. Make coffee
def make_coffee(coffee_type, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_type}. Enjoy! ☕")

     
# 1a. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while still_serving:
    
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        still_serving = False
    
    # 3. Print report.
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    else:
        try: 
            # 4a. Check resources sufficient?
            drink = MENU[choice]
            if is_resource_sufficient(drink['ingredients']):
            
                # 5a. Process coins
                payment = process_coins()

                # 6a. Check transaction successful
                if is_transaction_successful(payment, drink['cost']):
                
                    # 7a. Make coffee
                    make_coffee(choice, drink['ingredients'])

        except: print("Sorry, not a valid choice or something is wrong.")
