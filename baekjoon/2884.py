H_str, M_str = input().split()
H = int(H_str)
M = int(M_str)

def alarm(H, M):
    if H >= 24:
        return "잘못된 시간 입력"

    if M >= 60:
        return "잘못된 분 입력"

    if M < 45:
        H -= 1
        M += 15
        if H < 0:
            H = 23
    else:
        M -= 45
    print(H, M)

alarm(H, M)


