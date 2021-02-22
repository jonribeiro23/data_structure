class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        self.data.pop(self.length - 1)
        self.length -= 1
        return last_item

    def delete(self, index):
        try:
            item = self.data[index]
            self.shift_items(index)
            self.data.pop(self.length)
        except KeyError:
            # raise Exception('Index out of the range!')
            return 0
        else:
            return item

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self._decrement()

    def show(self):
        print(self.data)

    def _increment(self):
        self.length += 1

    def _decrement(self):
        self.length -= 1



newArray = MyArray()
newArray.push('hi')
newArray.push('You')
newArray.push('superman')
newArray.push('Flash')
newArray.push('WW')

# newArray.delete(3)
newArray.pop()
# newArray.push('Spiderman')

print(newArray.length)
newArray.show()
