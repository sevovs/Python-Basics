hours = int(input())
minutes = int(input())
minutes += 15
hours += minutes // 60
minutes %= 60
if hours > 23:
    hours = 0
if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
