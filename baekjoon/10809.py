S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for ch in alphabet:
#     if ch in S:
#         print(S.index(ch), end=' ')
#     else:
#         print('-1', end=' ')

for ch in alphabet:
    print(S.find(ch), end=' ')
