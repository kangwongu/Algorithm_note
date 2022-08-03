input = "hello my name is sparta"


# 가장 많은 빈도수의 알파벳 출력하기
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 1. for문을 돌면서, 문자인지 아닌지 판별
    for alphabet in string:
        # 2. 문자면, 배열에 넣는다.
        if alphabet.isalpha():
            # 2-1. 배열의 해당 인덱스에 값을 증가시킨다.
            alphabet_index = ord(alphabet) - ord("a")
            alphabet_occurrence_array[alphabet_index] += 1

    # 3. 가장 많은 빈도수를 기록한 알파벳을 찾는다.
    max_occurrence = 0                  # 최대 빈도수
    max_occurrence_alphabet_index = 0   # 최대 빈도 알파벳 인덱스

    for index in range(len(alphabet_occurrence_array)):
        # 4. 각 알파벳 빈도 수 가져오기
        current_alphabet_occurrence = alphabet_occurrence_array[index]
        # 5. 최대 빈도수와 비교
        if current_alphabet_occurrence > max_occurrence:
            # 6. 현재 최대 빈도수보다 크면 최대 빈도수로 저장하고, 알파벳 인덱스 저장
            max_occurrence = current_alphabet_occurrence
            max_occurrence_alphabet_index = index

    # 문자로 변환
    return chr(max_occurrence_alphabet_index + ord("a"))

result = find_max_occurred_alphabet(input)
print(result)
