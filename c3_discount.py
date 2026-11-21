def customer_discount(subtotal : float, customer : str) -> float:
    if (customer == "student"):
        result = subtotal * 0.90
        return result
    elif (customer == "staff"):
        result = subtotal * 0.75
        return result
    else:
        return subtotal

def happy_hour_discount(amount : float, hour : int) -> float:
    if (hour >= 15 and hour <= 17):
        result = amount * 0.85
        return result
    else:
        return amount

def big_spender_bonus(amount : float) -> float:
    if (amount >= 20):
        result = amount - 2.0
        return result
    else:
        return amount

def add_vat(net : float) -> float:
    result = net * 1.19
    return result

def final_price(subtotal : float, customer : str, hour : int) -> float:
    after_customer = customer_discount(subtotal, customer)
    after_happy = happy_hour_discount(after_customer, hour)
    after_bonus = big_spender_bonus(after_happy)
    total = round(add_vat(after_bonus), 2)

    if (total < 0):
        return 0.0
    else:
        return total

if __name__ == "__main__":
    subtotal = float(input("Subtotal: "))
    customer = input("Customer: ").strip()
    hour = int(input("Hour: "))

    if (customer != "student" and customer != "staff" and customer != "regular"):
        print("Warning: unknown customer type.")

    print(final_price(subtotal, customer, hour))
