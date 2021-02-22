class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = {}
        self.cont = 0

    def _hash(self, key: str) -> int:
        hash_key = 0
        for i in range(len(key)):
            hash_key = (hash_key + i * i) % self.size
        return hash_key  # really fast. We consider O(1)

    def set(self, key: str, info: int) -> bool:
        hash_key = self._hash(key)
        if self.cont <= self.size:
            self.data[hash_key] = [key, info]
            self.cont += 1
            return True  # O(n)
        return False

    def get(self, key: str) -> list:
        hash_key = self._hash(key)
        if hash_key in self.data.keys():
            return self.data[hash_key][1]  # O(1)
        return None

    def table_keys(self):
        keys = []
        for key in self.data:
            keys.append(self.data[key][0])
        return sorted(keys)


test = HashTable(50)
test.set('cavalo', 123)
test.set('polvo', 4423)
test.set('pato', 573)
print(test.data)
# print(test.get('cavalo'))
print(test.table_keys())
