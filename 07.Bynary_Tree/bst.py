class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right


class Bst:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        node = Node(data)

        if self.empty_tree():
            self.root = node
        else:
            dad_node = None
            current_node = self.root

            while True:
                if current_node != None:
                    dad_node = current_node

                    if node.get_key() < current_node.get_key():
                        current_node = current_node.get_left()
                    else:
                        current_node = current_node.get_right()
                else:
                    if node.get_key() < dad_node.get_key():
                        dad_node.set_left(node)
                    else:
                        dad_node.set_right(node)
                    break

    def empty_tree(self):
        if self.root == None:
            return True
        return False


    def show(self, current_node):
        if current_node != None:
            print(current_node.get_key(), end=' ')
            self.show(current_node.get_left())
            self.show(current_node.get_right())


    def get_root(self):
        return self.root