price_for_travel = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_of_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_toys = number_trucks + number_dolls + number_minions + number_of_bears + number_puzzles
total_toys_price = number_puzzles * 2.60 + number_dolls * 3 + number_of_bears * 4.10 + number_minions * 8.20\
             + number_trucks * 2
if total_toys >= 50:
    total_toys_price -= total_toys_price * 0.25
total_earned = total_toys_price - total_toys_price * 0.1
needed_sum = abs(total_earned - price_for_travel)
if total_earned >= price_for_travel:
    print(f"Yes! {needed_sum:.2f} lv left.")
else:
    print(f"Not enough money! {needed_sum:.2f} lv needed.")
