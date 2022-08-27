str = input()
total_time = 0

for ch in str:
    if ch in 'ABC':
        total_time += 3
    elif ch in 'DEF':
        total_time += 4
    elif ch in 'GHI':
        total_time += 5
    elif ch in 'JKL':
        total_time += 6
    elif ch in 'MNO':
        total_time += 7
    elif ch in 'PQRS':
        total_time += 8
    elif ch in 'TUV':
        total_time += 9
    elif ch in 'WXYZ':
        total_time += 10

print(total_time)

# dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# str = input()
# total_time = 0
#
# for i in range(len(str)):
#     for dial in dials:
#         if str[i] in dial:
#             total_time += dials.index(dial) + 3
# print(total_time)