#DISCOUNT PRICES
def customer_discount(subtotal: float, customer: str) -> float:
    if customer == "student":
        return subtotal * 0.90
    elif customer == "staff":
        return subtotal * 0.75
    elif customer == "regular":
        return subtotal
    else:
        return subtotal

def happy_hour_discount(amount: float, hour: int) -> float:
    if hour >= 15 and hour <= 17:
        return amount * 0.85
    else:
        return amount

def big_spender_bonus(amount: float) -> float:
    if amount >= 20:
        return amount - 2
    else:
        return amount

def add_vat(net: float) -> float:
    return net * 1.19

def final_price(subtotal: float, customer: str, hour: int) -> float:
    a = customer_discount(subtotal, customer)
    b = happy_hour_discount(a, hour)
    c = big_spender_bonus(b)
    return round(add_vat(c), 2)

subtotal = float(input("Subtotal: "))
customer = input("Customer: ")
hour = int(input("Hour: "))

if customer not in ("student", "staff", "regular"):
    print("Warning: unknown customer type.")

print(final_price(subtotal, customer, hour))