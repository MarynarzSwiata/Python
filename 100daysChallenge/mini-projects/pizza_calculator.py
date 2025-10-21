def determine_tip_percentage(people_count):
    if people_count >= 8:
        return int(25)
    elif people_count > 4:
        return int(20)
    else:
        return float(input("Enter the tip percentage: "))


def calculate_total_bill(pizza_price, tip_percentage, people_count):
    tip_amount = pizza_price * tip_percentage / 100
    total_amount = pizza_price + tip_amount
    if total_amount > 50 and people_count >= 4:
        total_amount -= 10  # Apply discount
        print(
            "Discount of 10 EUR applied for groups larger than 4 with total bill over 50 EUR."
        )
    return total_amount


pizza_price = float(input("Enter the price of the pizza: "))
people_count = int(input("Enter the number of people: "))
total_amount = calculate_total_bill(
    pizza_price, determine_tip_percentage(people_count), people_count
)

price_per_person = total_amount / people_count

print(
    f"Price of Pizza is: {pizza_price:.2f} EUR and total bill is: {total_amount:.2f} EUR. Each person pays: {price_per_person:.2f} EUR."
)
