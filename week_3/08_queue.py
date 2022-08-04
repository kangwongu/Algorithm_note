class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # 새 노드를 tail뒤에 연결하고 tail로 설정
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None