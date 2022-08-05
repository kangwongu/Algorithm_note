N = int(input())

for i in range(N):
    str = list(input())
    total = 0
    score = 0
    for o in str:
        if o == 'O':
            score += 1
        else:
            score = 0

        total += score

    print(total)
