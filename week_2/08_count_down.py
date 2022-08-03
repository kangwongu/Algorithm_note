# 카운트 다운
def count_down(number):
    # 탈출조건
    if number < 0:
        return

    print(number)
    # 재귀
    count_down(number-1)

count_down(60)