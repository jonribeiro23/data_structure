class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def push(self, data):
        new_node = Node(data)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        else:
            new_node.next = self.last
            self.last = new_node
        return True

    def pop(self):
        actual_node = self.last
        while actual_node:
            if actual_node.next is None:
                self.first = previous_node
                self.first.next = None
            previous_node = actual_node
            actual_node = actual_node.next

    def traverse(self):
        actual_node = self.last
        while actual_node:
            print(f"{actual_node.data} -> ", end='')
            self.first = actual_node.next
            actual_node = actual_node.next


q = Queue()
q.push('google')
q.push('microsoft')
q.push('facebook')
q.push('amazon')
q.traverse()
q.pop()
print()
q.traverse()
# item = q.peek()
# print(item.data)
# q.pop()
# item = q.peek()
# print(item.data)
