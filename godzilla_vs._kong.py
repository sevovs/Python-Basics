budget = float(input())
number_of_statists = int(input())
price_for_outfit = float(input())
decor = budget * 0.1
outfit_price = number_of_statists * price_for_outfit
if number_of_statists > 150:
    outfit_price *= 0.9
needed_sum = decor + outfit_price
difference = abs(needed_sum - budget)
if needed_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

