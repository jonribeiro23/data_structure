class StackArray:
    def __init__(self):
        self.data = []
        self.length = 0

    def peek(self):
        return self.data[0]

    def push(self, info):
        self.data.append(info)
        self.length += 1
        return info

    def pop(self):
        if self.length <= 0:
            return

        self.length -= 1
        return self.data.pop(0)

    def traverse(self):
        for item in self.data:
            print(f' <- {item}', end='')


sa = StackArray()
sa.push('dog')
sa.push('cat')
sa.push('horse')
sa.push('bird')

sa.traverse()
sa.pop()
sa.push('turtle')
print()
sa.traverse()
