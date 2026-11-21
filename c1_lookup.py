from menu import MENU

def price_of(code : str) -> float:
    clean_code = code.strip().upper()
    temp_dictionary = MENU.get(clean_code, -1)

    if (temp_dictionary == -1):
        return -1.0
    else:
        price = temp_dictionary.get("price")
        return price

def name_of(code : str) -> str:
    clean_code = code.strip().upper()
    temp_dictionary = MENU.get(clean_code, -1)

    if (temp_dictionary == -1):
        return "unknown"
    else:
        name = temp_dictionary.get("name")
        return name

def category_of(code : str) -> str:
    clean_code = code.strip().upper()
    temp_dictionary = MENU.get(clean_code, -1)

    if (temp_dictionary == -1):
        return "unknown"
    else:
        category = temp_dictionary.get("category")
        return category

if __name__ == "__main__":
    code = input("Item code: ").strip()
    price = price_of(code)

    if (price < 0):
        print("Unknown item.")
    else:
        print(f"That costs {price:.2f} €")
 
