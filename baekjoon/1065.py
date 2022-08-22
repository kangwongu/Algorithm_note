X = int(input())

hansu = 0
for i in range(1, X+1):
    X_list = list(map(int, str(i)))
    # 1~99는 모두 등차수열 성립
    if i < 100:
        hansu += 1
    # 3자리 수는 각 공차가 같은지 검사
    elif X_list[0]-X_list[1] == X_list[1]-X_list[2]:
        hansu += 1

print(hansu)
