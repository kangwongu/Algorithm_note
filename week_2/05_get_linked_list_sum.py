class Node:
    # 생성자
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # 생성자
    def __init__(self, data):
        self.head = Node(data)

    # 추가
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

# 두 링크드 리스트의 합을 반환하는 함수
def get_linked_list_sum(linked_list_1, linked_list_2):
    # head를 활용, 링크드 리스트를 순회하기 위해선 head가 필요하다
    sum1 = get_sum(linked_list_1)
    sum2 = get_sum(linked_list_2)

    return sum1 + sum2

def get_sum(linked_list):
    head = linked_list.head
    sum = 0
    while head is not None:
        sum = (sum * 10) + head.data
        head = head.next
    return sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))