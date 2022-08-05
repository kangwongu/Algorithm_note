class MaxHeap:
    def __init__(self):
        self.items = [None] # 트리의 맨 앞은 None

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)        # 마지막에 노드 추가
        cur_index = len(self.items)-1   # 가장 마지막에 넣은 노드의 인덱스

        # 부모와 비교해서 최대값이 가장 위로 오도록
        while cur_index > 1:            # 트리 맨 꼭대기까지 순회
            parent_index = cur_index // 2
            # 자식이 부모보다 크면 자리교체
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 1. 루트 노드와 맨 끝에 있는 원소를 교체
        # 2. 맨 뒤에 있는 원소(루트 노드) 삭제
        # 3. 변경된 노드와 자식 노드들을 비교, 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 변경
        # 4. 자식 노드 둘 보다 부모 노드가 더 크거나 가장 바닥에 도달하지 않을때까지 3.을 반복
        # 5. 2에서 제거한 원래 루트 노드를 반환

        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1

        while cur_index <= len(self.items)-1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            # 왼쪽 자식 노드가 있다는 의미, 왼쪽 자식 노드가 현재 노드보다 크면
            if left_child_index <= len(self.items)-1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            # 오른쪽 자식 노드가 있다는 의미, 왼쪽 자식 노드가 현재 노드보다 크면
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 최대값 인덱스가 현재 인덱스면, 종료
            if max_index == cur_index:
                break

            # 자리 변경
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]