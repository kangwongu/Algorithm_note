input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없음
def find_prime_list_under_number(number):
    prime_array = []
    for i in range(2, number+1):
        for n in range(2, i):
            # 소수가 아님
            if i % n == 0:
                break
        else:
            prime_array.append(num)
    return prime_array


result = find_prime_list_under_number(input)
print(result)