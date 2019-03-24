from ..display.text import str_tree


class BinarySearchTree:
    def __init__(self, BinarySearchNode):
        self.root = None
        self.BinarySearchNode = BinarySearchNode

    # 1. insert
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = self.BinarySearchNode(value)

    # 2. search
    def search(self, value):
        if self.root:
            return self.root.search(value)
        else:
            raise ValueError

    # 3. list
    def list(self):
        if self.root:
            return self.root.list()
        else:
            return []

    # 4. delete
    def delete_left(self, value):
        if self.root:
            self.root = self.root.delete_left(value)
        else:
            raise ValueError

    def delete_right(self, value):
        if self.root:
            self.root = self.root.delete_right(value)
        else:
            raise ValueError

    # 5. iterator
    def __iter__(self):
        if self.root:
            return iter(self.root)
        else:
            return iter([])

    __str__ = str_tree
