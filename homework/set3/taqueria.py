menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def _capital(menu_str):
    try:
        new_menu = []
        for new_item in menu_str.split():
            new_item = new_item.capitalize()
            new_menu.append(new_item)
        return " ".join(new_menu)
    except AttributeError:
        return menu_str.capitalize()


total = 0
while True:
    try:
        item = _capital(input("Item: "))
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except (KeyboardInterrupt, EOFError):
        break
