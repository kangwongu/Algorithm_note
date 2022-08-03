# 팩토리얼
def factorial(n):
    # 탈출 조건
    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))