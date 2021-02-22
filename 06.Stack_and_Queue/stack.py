class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        pass

    def push(self, value: str) -> bool:
        new_node = Node(value)
        self.length += 1

        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.bottom
            self.top = new_node

        if not self.bottom:
            self.bottom = new_node

        return True

    def pop(self):
        pass

    def show(self):
        actual_node = self.top

        while actual_node is not None:
            print(actual_node.value)
            actual_node = actual_node.next


class Stack2:
    def __init__(self, ):
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        self.size += 1

        if not self.bottom:
            self.bottom = new_node

        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self) -> bool:
        if not self.top:
            return
        self.size -= 1
        self.top = self.top.next
        return True

    def peek(self):
        return self.top

    def traverse(self):
        actual_node = self.top
        while actual_node:
            print(actual_node.value)
            print(' |')
            print(' V')
            actual_node = actual_node.next
