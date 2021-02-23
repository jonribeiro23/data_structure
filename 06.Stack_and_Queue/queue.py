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

    def enqueue(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        else:
            # new_node.next = self.last
            # self.last = new_node
            self.last.next = new_node
            self.last = new_node
        return True

    def dequeue(self):
        if self.length == 0:
            return

        if self.first == self.last:
            return None

        removed_node = self.first
        self.first = self.first.next
        self.length -= 1
        return removed_node.data

    def traverse(self):
        actual_node = self.first
        while actual_node:
            print(f" <- {actual_node.data}", end='')
            actual_node = actual_node.next


q = Queue()
q.enqueue('google')
q.enqueue('microsoft')
q.enqueue('facebook')
q.enqueue('amazon')
q.traverse()
print()
print('removed node: ', q.dequeue())
# print('removed node: ', q.dequeue())
print()
q.traverse()
print()
item = q.peek()
print('item peeked: ', item.data)


print('items: ', q.length)
