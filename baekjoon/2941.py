str = input()
croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 크로아티아 알파벳

for croatia in croatia_list:
    str = str.replace(croatia, 'a')  # 문장 중에, 크로아티아 알파벳이 있으면 a로 변경 (카운트 위해 a로 변경함)

print(len(str))