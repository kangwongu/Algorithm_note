hour, minute = map(int, input().split())
timer = int(input())

current_minute = minute + timer

while current_minute >= 60:
    hour += 1
    current_minute -= 60
    if hour > 23:
        hour = 0

print(hour, current_minute)
