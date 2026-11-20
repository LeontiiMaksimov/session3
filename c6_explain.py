#TASK 6 EXPLAINATION
def explain_price(subtotal: float, customer: str, hour: int) -> str:
    if subtotal == 0:
        return "Subtotal: 0.00 €\nFINAL: 0.00 €"

    lines = [f"Subtotal: {subtotal:.2f} €"]
    current = float(subtotal)

    if customer == "student":
        delta = -(current * 0.10)
        current = current + delta
        lines.append(f"  - Student discount (-10%): {delta:+.2f} € -> {current:.2f} €")
    elif customer == "staff":
        delta = -(current * 0.25)
        current = current + delta
        lines.append(f"  - Staff discount (-25%): {delta:+.2f} € -> {current:.2f} €")

    if hour >= 15 and hour <= 17:
        delta = -(current * 0.15)
        current = current + delta
        lines.append(f"  - Happy hour (-15%): {delta:+.2f} € -> {current:.2f} €")

    if current >= 20:
        delta = -2.0
        current = current + delta
        lines.append(f"  - Big-spender bonus (-2.00 €): {delta:+.2f} € -> {current:.2f} €")

    vat_amount = current * 0.19
    final_total = round(current + vat_amount, 2)
    lines.append(f"  + VAT (19%): {vat_amount:+.2f} € -> {final_total:.2f} €")
    lines.append(f"FINAL: {final_total:.2f} €")

    return "\n".join(lines)


if __name__ == "__main__":
    print(explain_price(10.00, "regular", 10))
    print("---")
    print(explain_price(10.00, "student", 16))
    print("---")
    print(explain_price(30.00, "staff", 16))
    print("---")
    print(explain_price(0.00, "student", 16))