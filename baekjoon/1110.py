n = int(input())
correct = n
count = 0

while 1:
    correct = (correct%10*10) + (((correct//10) + (correct%10))%10)
    count += 1
    if correct == n:
        break

print(count)