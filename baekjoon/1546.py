N = int(input())
score_list = list(map(int, input().split()))
max_val = max(score_list)

for i in range(N):
    score_list[i] = score_list[i]/max_val*100

average = sum(score_list) / N
print(average)