from math import ceil

serial = input()
duration = int(input())
lunch_break = int(input())
time_for_lunch = lunch_break / 8
time_for_rest = lunch_break / 4
time_left = lunch_break - time_for_rest - time_for_lunch
needed_time = abs(duration - time_left)
if time_left >= duration:
    print(f"You have enough time to watch {serial} and left with {ceil(needed_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {ceil(needed_time)} more minutes.")
