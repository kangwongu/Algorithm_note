N = int(input())

for i in range(N):
    S, R = input().split()
    for ch in R:
        print(ch*int(S), end='')
    print()