input = "우영우영우"

# 회문 검사 (반복문)
def is_palindrome(string):
    length = len(string)
    for index in range(length-1):
        # 문장 첫, 끝이 일치하지 않으면 false
        if string[index] != string[length-1-index]:
            return False
    return True

print(is_palindrome(input))