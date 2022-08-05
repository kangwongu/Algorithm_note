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



max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!