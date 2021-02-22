from data import MENU, resources

still_serving = True

# 1. Print report
def see_report():
    water_resource = resources["water"]
    milk_resource = resources["milk"]
    coffee_resource = resources["coffee"]
    deposit_status = resources["money"] = 0
    return (f"Water: {water_resource}ml\nMilk: {milk_resource}ml\nCoffee: {coffee_resource}g\nMoney: ${deposit_status}")


while still_serving:
    # print(MENU)
    serve = input("What would you like? (espresso/latte/cappuccino): ")
    if serve == 'report':
        print(f"{see_report()}")
    if serve == 'off':
        still_serving = False
# 2. Check resources are sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee
