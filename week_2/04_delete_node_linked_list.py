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

    # 특정 인덱스에 노드 추가하기
    def add_node(self, index, data):
        new_node = Node(data)
        # head가 없다면 특정 인덱스에 뭘 추가할 수 없다
        if self.head == None:
            return None

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # index의 노드를 가져온다
        seleted_node = self.get_node(index-1) # 지정한 인덱스의 앞 노드
        next_node = seleted_node.next   # index에 해당하는 노드의 다음 노드를 담아둔다
        seleted_node.next = new_node    # index에 해당하는 노드의 다음 노드에 새 노드를 연결
        new_node.next = next_node       # 새 노드의 다음 노드에 new_node로 담아두었던 노드 연결

    # 특정 인덱스의 노드 삭제하기
    def delete_node(self, index):
        # head가 없다면 삭제할 게 없다
        if self.head == None:
            return None
        # 0번째(head)를 삭제한다면
        if index == 0:
            # head값을 다음 노드로 변경시킨다
            self.head = self.head.next
            return

        seleted_node = self.get_node(index - 1)  # 지정한 인덱스의 앞 노드
        # 지정한 인덱스의 앞 노드의 다음 노드 연결을 다다음 노드로 변경시킨다 (삭제)
        seleted_node.next = seleted_node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
print(linked_list.get_node(1).data)
print('---------')
linked_list.add_node(1,6)
linked_list.print_all()