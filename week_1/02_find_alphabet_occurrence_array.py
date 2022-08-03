def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 1. for문을 돌면서, 문자인지 아닌지 판별
    for alphabet in string:
        # 2. 문자면, 배열에 넣는다.
        if alphabet.isalpha():
            # 2-1. 배열의 해당 인덱스에 값을 증가시킨다.
            alphabet_index = ord(alphabet) - ord("a")
            alphabet_occurrence_array[alphabet_index] += 1
        # 3. 문자가 아니면 패스

    # 4. 배열 반환
    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))