pizza_price = float(input("Enter the price of the pizza: "))
people_count = int(input("Enter the number of people: "))

if people_count >= 8:
    tip_percentage = 25
elif people_count > 4:
    tip_percentage = 20
else:
    tip_percentage = float(input("Enter the tip percentage: "))

tip_amount = pizza_price * tip_percentage / 100
total_amount = pizza_price + tip_amount
if total_amount > 50 and people_count >= 4:
    total_amount -= 10  # Apply discount
    print(
        "Discount of 10 EUR applied for groups larger than 4 with total bill over 50 EUR."
    )
price_per_person = total_amount / people_count

print(
    f"Price of Pizza is: {pizza_price:.2f} EUR and total bill is: {total_amount:.2f} EUR. Each person pays: {price_per_person:.2f} EUR."
)
