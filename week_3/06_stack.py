# 노드 클래스
class Node:
    # 생성자
    def __init__(self, data):
        self.data = data
        self.next = None

# 스택 (링크드 리스트로 구현)
class Stack:
    # 생성자
    def __init__(self):
        self.head = None

    # 추가
    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head   # 새 노드의 다음 값을 head로 변경
        self.head = new_node        # head를 새 노드로 변경

    # 삭제
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    # 가장 위의 값 출력
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.head.data

    # 비어있는 지 확인
    def is_empty(self):
        return self.head is None