class BinarySearchNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #
    # 1. insert
    #
    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchNode(value)
        elif self.value < value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchNode(value)

    #
    # 2. search
    #
    def search(self, value):
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                raise ValueError
        elif value == self.value:
            return self
        elif self.value < value:
            if self.right:
                return self.right.search(value)
            else:
                raise ValueError

    #
    # 3. list
    #
    def list(self):
        left = self.left.list() if self.left else []
        center = [self.value]
        right = self.right.list() if self.right else []
        return left + center + right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    #
    # 4. delete
    #

    # 4.1. delete_left
    def delete_left(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete_left(value)
                promoted = self
            else:
                raise ValueError
        elif value == self.value:
            if self.left:
                promoted = self.left._search_max()
                promoted.left = self.left._delete_max()
                promoted.right = self.right
            else:
                promoted = self.right
        elif self.value < value:
            if self.right:
                self.right = self.right.delete_left(value)
                promoted = self
            else:
                raise ValueError
        return promoted

    def _search_max(self):
        if self.right:
            return self.right._search_max()
        else:
            return self

    def _delete_max(self):
        if self.right:
            self.right = self.right._delete_max()
            promoted = self
        else:
            promoted = self.left
        return promoted

    # 4.2. delete_right
    def delete_right(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete_right(value)
                promoted = self
            else:
                raise ValueError
        elif value == self.value:
            if self.right:
                promoted = self.right._search_min()
                promoted.right = self.right._delete_min()
                promoted.left = self.left
            else:
                promoted = self.left
        elif self.value < value:
            if self.right:
                self.right = self.right.delete_right(value)
                promoted = self
            else:
                raise ValueError
        return promoted

    def _search_min(self):
        if self.left:
            return self.left._search_min()
        else:
            return self

    def _delete_min(self):
        if self.left:
            self.left = self.left._delete_min()
            promoted = self
        else:
            promoted = self.right
        return promoted
