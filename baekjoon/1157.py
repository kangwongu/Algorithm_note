alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
max_count = 0
max_alphabet = 0
str = input()
lower_str = str.lower()

for alphabet in alphabet_list:
    # print(alphabet, str.count(alphabet))
    if max_count < lower_str.count(alphabet):
        max_alphabet = alphabet
        max_count = lower_str.count(alphabet)
    elif max_count == lower_str.count(alphabet):
        max_alphabet = '?'

print(max_alphabet.upper())

# str = input().upper()
# print(str)
# str_list = list(set(str))
# print(str_list)
# count_list = [str.count(i) for i in str_list]
# print(count_list)
#
# if count_list.count(max(count_list)) > 1:
#     print('?')
# else:
#     print(str_list[count_list.index(max(count_list))])