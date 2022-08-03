# 노드 클래스
class Node:
    # 생성자
    def __init__(self, data):
        self.data = data
        self.next = None

# 링크드 리스트 클래스
class LinkedList:
    # 생성자
    def __init__(self, data):
        self.head = Node(data)

    # 노드 추가
    def append(self, data):
        new_node = Node(data)
        # 빈 링크드리스트
        if self.head == None:
            self.head = new_node

        current_node = self.head
        # 다음 노드가 null이 아닐 때 까지 반복하며 다음 노드로 이동
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # 전체 노드 조회
    def print_all(self):
        # head가 없다면 반환할 게 없다
        if self.head == None:
            return None

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    # 특정 인덱스에 해당하는 노드를 반환하는 메소드
    def get_node(self, index):
        # head가 없다면 반환할 게 없다
        if self.head == None:
            return None

        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node




linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.print_all()
print(linked_list.get_node(2).data)