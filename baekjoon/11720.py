# N1 = int(input())
# N2 = sum(map(int,input()))
#
# print(N2)

N1 = int(input())
N2 = input()
sum = 0

for i in range(N1):
    sum += int(N2[i])
print(sum)