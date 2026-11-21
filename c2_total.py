from c1_lookup import price_of

def slot_price(code : str) -> float:
    price = price_of(code)

    if (price < 0):
        return 0.0
    else:
        return price

def add_vat(net : float, rate : float = 0.19) -> float:
    total = round(net * (1 + rate), 2)
    return total

def order_total(code1 : str, code2 : str, code3 : str) -> float:
    subtotal = slot_price(code1) + slot_price(code2) + slot_price(code3)
    total = add_vat(subtotal)
    return total

def warn_if_unknown(code : str) -> None:
    clean_code = code.strip()

    if (clean_code != "" and price_of(clean_code) < 0):
        print(f"Warning: unknown code {clean_code}")

code1 = input("Code 1: ")
code2 = input("Code 2: ")
code3 = input("Code 3: ")

warn_if_unknown(code1)
warn_if_unknown(code2)
warn_if_unknown(code3)

print(order_total(code1, code2, code3))
