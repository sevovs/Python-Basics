budget = float(input())
quantity_gpu = int(input())
quantity_cpu = int(input())
quantity_ram = int(input())
price_gpu = 250
total_gpu = quantity_gpu * price_gpu
price_cpu = total_gpu * 0.35
price_ram = total_gpu * 0.1
total_amount = total_gpu + quantity_ram * price_ram + quantity_cpu * price_cpu
if quantity_gpu > quantity_cpu:
    total_amount -= total_amount * 0.15
needed_budget = abs(total_amount - budget)
if total_amount <= budget:
    print(f"You have {needed_budget:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_budget:.2f} leva more!")
