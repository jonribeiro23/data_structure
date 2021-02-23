class QueueArray:
    def __init__(self):
        self.data = []
        self.length = 0

    def enqueue(self, info):
        self.data.append(info)
        self.length += 1
        return info

    def dequeue(self):
        if self.length <= 0:
            return

        self.length -= 1
        return self.data.pop(-1)

    def peek(self):
        if self.length <= 0:
            return

        return self.data[-1]

    def traverse(self):
        for item in reversed(self.data):
            print(item)

