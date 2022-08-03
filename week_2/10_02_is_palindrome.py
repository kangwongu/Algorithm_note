input = "우영우영우"

# 회문 검사 (재귀)
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))