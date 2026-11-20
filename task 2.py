from task1 import price_of
from menu import MENU

def add_vat(net: float, rate: float = 0.19) -> float:
    return round(net * (1 + rate), 2)

def order_total(code1: str, code2: str, code3: str) -> float:
    subtotal = price_of(code1) + price_of(code2) + price_of(code3)
    return add_vat(subtotal)

def warn_if_unknown(code: str) -> None:
    if code != "" and code not in MENU:
        print(f"warning: unknown code {code!r}")

# Test 1: E1, F1, ""
warn_if_unknown("E1")
warn_if_unknown("F1")
warn_if_unknown("")
print(order_total("E1", "F1", ""))

# Test 2: E3, F3, W2
warn_if_unknown("E3")
warn_if_unknown("F3")
warn_if_unknown("W2")
print(order_total("E3", "F3", "W2"))

# Test 3: X9, F1, ""
warn_if_unknown("X9")
warn_if_unknown("F1")
warn_if_unknown("")
print(order_total("X9", "F1", ""))

# Test 4: "", "", ""
print(order_total("", "", ""))

