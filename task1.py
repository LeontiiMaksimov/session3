from menu import MENU

def price_of(code : str) -> float:
    temp_dictionary = MENU.get(code, -1)

    if (temp_dictionary == -1):
        return -1
    else:
        price = temp_dictionary.get("price")
        return price

code = input()
print(price_of(code))
