def explain_price(subtotal : float, customer : str, hour : int) -> str:
    if (subtotal == 0):
        return "Subtotal: 0.00 €\nFINAL: 0.00 €"

    text = f"Subtotal: {subtotal:.2f} €\n"
    current = subtotal

    if (customer == "student"):
        discount = current * 0.10
        current = current - discount
        text = text + f" - Student discount (-10%): -{discount:.2f} € → {current:.2f} €\n"
    elif (customer == "staff"):
        discount = current * 0.25
        current = current - discount
        text = text + f" - Staff discount (-25%): -{discount:.2f} € → {current:.2f} €\n"

    if (hour >= 15 and hour <= 17):
        discount = current * 0.15
        current = current - discount
        text = text + f" - Happy hour (-15%): -{discount:.2f} € → {current:.2f} €\n"

    if (current >= 20):
        current = current - 2.0
        text = text + f" - Big-spender bonus (-2.00 €): -2.00 € → {current:.2f} €\n"

    vat = current * 0.19
    final = round(current + vat, 2)
    text = text + f" + VAT (19%): +{vat:.2f} € → {final:.2f} €\n"
    text = text + f"FINAL: {final:.2f} €"

    return text

if __name__ == "__main__":
    print(explain_price(30.00, "student", 16))
