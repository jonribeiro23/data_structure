class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, ):
        self.head = None
        self.size = 0

    def insert_start(self, value):
        new_node = Node(value)
        self.size += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        self.size += 1
        actual_node = self.head
        while actual_node.next:
            actual_node = actual_node.next

        actual_node.next = new_node

    def traverse_list(self):
        actual_node = self.head
        while actual_node:
            print(actual_node.value)
            actual_node = actual_node.next



