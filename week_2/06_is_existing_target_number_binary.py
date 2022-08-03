finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 이진 탐색
def is_existing_target_number_binary(target, array):
    # 범위, 인덱스로 비교
    min = 0             # 최소
    max = len(array)-1  # 최대
    mid = (min + max) // 2

    # 종료 조건
    while min <= max:
        # 도출한 중위값이 target과 일치?
        if array[mid] == target:
            return True
        # 최대값 변경
        elif array[mid] > target:
            max = mid-1
        # 최소값 변경
        else:
            min = mid+1
        # 반복문이 한 번 실행될때마다 중위값 업데이트
        mid = (min + max) // 2

    # 반복문을 탈출했다면 일치x
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)