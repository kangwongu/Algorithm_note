N = int(input())
count = N  # 그룹단어를 세는 변수

for i in range(N):
    str = input()
    for j in range(len(str)-1):
        if str[j] == str[j+1]:
            pass
        # 중복 문자는 있지만, 연속되지 않은 경우 (그룹단어x)
        elif str[j] in str[j+1:]:
            count -= 1
            break

print(count)