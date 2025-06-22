def new_order() -> bool:
    answer = input(f"Are you going to make a new order?; y/n: ").strip().lower()
    if answer == 'y':
        return False
    elif answer == 'n':
        return True


def get_order(ingredients: list[str]) -> list[str]:
    order: list[str] = []
    for ingredient in ingredients:
        command = input(f"Add {ingredient}; y/n: ").strip().lower()
        if command == 'y':
            order.append(ingredient)
    return order    

def check_order(order: list[str]) -> bool:
    if not order:
        print("You didn't order anything!")
        return new_order()
    for ingredient in order:
        print(ingredient)
    answer = input(f"Correct order?; y/n: ").strip().lower()    
    if answer == 'y':
        print("Order accepted. Please wait.")
        return True
    elif answer == 'n':
        return new_order()
    

def main() -> None:
    while True:
        ingredients = ['tomatoes', 'mushrooms', 'cheese', 'sausage', 'olives']
        order = get_order(ingredients)
        if check_order(order):
            exit() 

main()            

