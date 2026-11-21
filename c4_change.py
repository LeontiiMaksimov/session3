def take_coin(amount_cents : int, coin : int, change : dict) -> int:
    count = amount_cents // coin
    remainder = amount_cents % coin

    if (count > 0):
        change[coin] = count

    return remainder

def make_change(amount_cents : int) -> dict:
    change = {}

    if (amount_cents <= 0):
        return change

    remainder = take_coin(amount_cents, 500, change)
    remainder = take_coin(remainder, 200, change)
    remainder = take_coin(remainder, 100, change)
    remainder = take_coin(remainder, 50, change)
    remainder = take_coin(remainder, 20, change)
    remainder = take_coin(remainder, 10, change)
    remainder = take_coin(remainder, 5, change)
    remainder = take_coin(remainder, 2, change)
    remainder = take_coin(remainder, 1, change)

    return change

def change_for(price : float, paid : float) -> dict | None:
    price_cents = round(price * 100)
    paid_cents = round(paid * 100)
    diff_cents = paid_cents - price_cents

    if (diff_cents < 0):
        return None
    else:
        change = make_change(diff_cents)
        return change

if __name__ == "__main__":
    print(make_change(0))
    print(make_change(1))
    print(make_change(7))
    print(make_change(88))
    print(make_change(1234))
    print(change_for(14.14, 20.00))
    print(change_for(20.00, 10.00))
