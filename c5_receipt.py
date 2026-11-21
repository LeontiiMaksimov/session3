from datetime import datetime
from c1_lookup import price_of, name_of
from c3_discount import final_price
from c4_change import change_for

def print_coin(change : dict, coin : int, label : str) -> None:
    count = change.get(coin, 0)

    if (count > 0):
        print(f"    {count} × {label}")

def print_receipt(code1 : str, code2 : str, code3 : str, customer : str, hour : int, paid : float) -> None:
    subtotal = 0.0

    p1 = price_of(code1)
    p2 = price_of(code2)
    p3 = price_of(code3)

    if (code1 != "" and p1 > 0):
        subtotal = subtotal + p1
    if (code2 != "" and p2 > 0):
        subtotal = subtotal + p2
    if (code3 != "" and p3 > 0):
        subtotal = subtotal + p3

    total = final_price(subtotal, customer, hour)
    change = change_for(total, paid)

    if (change == None):
        print("Not enough money paid. Transaction declined.")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print("==============================")
    print("       CAFÉ LAMBDA")
    print(f"  {now}")
    print("------------------------------")

    if (code1 != "" and p1 > 0):
        print(f"  {name_of(code1):<16}{p1:6.2f} €")
    if (code2 != "" and p2 > 0):
        print(f"  {name_of(code2):<16}{p2:6.2f} €")
    if (code3 != "" and p3 > 0):
        print(f"  {name_of(code3):<16}{p3:6.2f} €")

    print("------------------------------")
    print(f"  Subtotal        {subtotal:6.2f} €")

    current = subtotal

    if (customer == "student"):
        discount = current * 0.10
        current = current - discount
        print(f"  Student -10%    {-discount:6.2f} €")
    elif (customer == "staff"):
        discount = current * 0.25
        current = current - discount
        print(f"  Staff -25%      {-discount:6.2f} €")

    if (hour >= 15 and hour <= 17):
        discount = current * 0.15
        current = current - discount
        print(f"  Happy hour -15% {-discount:6.2f} €")

    if (current >= 20):
        current = current - 2.0
        print(f"  Big spender     {-2.0:6.2f} €")

    vat = current * 0.19
    change_amount = paid - total

    print(f"  VAT 19%         {vat:6.2f} €")
    print(f"  TOTAL           {total:6.2f} €")
    print(f"  Paid            {paid:6.2f} €")
    print(f"  Change          {change_amount:6.2f} €")

    print_coin(change, 500, "5€")
    print_coin(change, 200, "2€")
    print_coin(change, 100, "1€")
    print_coin(change, 50, "50¢")
    print_coin(change, 20, "20¢")
    print_coin(change, 10, "10¢")
    print_coin(change, 5, "5¢")
    print_coin(change, 2, "2¢")
    print_coin(change, 1, "1¢")

    print("==============================")
    print(f"    Thank you, {customer}!")
    print("==============================")

if __name__ == "__main__":
    print_receipt("E1", "F3", "W2", "student", 14, 20.00)
