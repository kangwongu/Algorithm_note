def find_not_repeating_first_character(string):
    # 빈도수 구하기
    alphabet_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_index = ord(alphabet) - ord("a")
            alphabet_array[alphabet_index] += 1

    # 빈도수를 구한 배열을 이용해서, 중복되지 않은 문자 도출
    no_dup_alphabet_array = []
    for index in range(len(alphabet_array)):
        current_occurrence_alphabet = alphabet_array[index]
        if current_occurrence_alphabet == 1:
            no_dup_alphabet_array.append(chr(index + ord("a")))

    # 문장중에 중복되지 않은 문자의 처음값 출력
    for char in string:
        if char in no_dup_alphabet_array:
            return char

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))