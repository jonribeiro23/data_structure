# Return the first recurring character
class HashTable:
    def __init__(self):
        self.data = {}

    def _hash(self, key):
        hash_key = 0
        for i in range(key):
            hash_key = (hash_key + i * i)
        return hash_key

    def first_recurring(self, array):
        for item in array:
            hash_key = self._hash(item)
            if (hash_key in self.data.keys()) is False:
                self.data[hash_key] = item
            else:
                return item
        return None


array_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array_3 = [1, 3, 4, 5]
test = HashTable()
print(test.first_recurring(array_1))


# Solving without hash table

def first_recurring(array):
    my_dict = {}
    for i in range(len(array)):
        if array[i] in my_dict.keys():
            return array[i]
        else:
            my_dict[array[i]] = i
    return None


print(first_recurring(array_3))
