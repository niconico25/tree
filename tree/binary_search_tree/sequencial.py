class BinarySearchNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #
    # 1. insert
    #
    def insert(self, value):
        child = self
        while child:
            parent = child
            side = 'left' if value <= child.value else 'right'
            child = getattr(parent, side)
        setattr(parent, side, BinarySearchNode(value))

    #
    # 2. search
    #
    def search(self, value):
        node = self
        while node:
            if value < node.value:
                node = node.left
            elif value == node.value:
                return node
            elif node.value < value:
                node = node.right
        raise ValueError(f'{value} is not found')

    #
    # 3. list
    #
    def list(self):
        sorted_list = []
        iterator = Iterator(self)
        while True:
            try:
                value = next(iterator)
            except StopIteration:
                break
            sorted_list.append(value)
        return sorted_list

    def __iter__(self):
        return Iterator(self)

    #
    # 4. delete
    #

    # 4.1. delete_left
    def delete_left(self, value):
        parent, side, deleted = self._search_parent(value)
        if deleted.left:
            promoted = deleted.left._search_max()
            promoted.left = deleted.left._delete_max()
            promoted.right = deleted.right
        else:
            promoted = deleted.right

        # if self is not deleted,
        # if root is not deleted,
        if parent:
            setattr(parent, side, promoted)
            return self
        else:
            return promoted

    def _search_parent(self, value):
        parent, side = None, None
        node = self
        while node:
            if value < node.value:
                side = 'left'
            elif value == node.value:
                return parent, side, node
            elif node.value < value:
                side = 'right'
            parent = node
            node = getattr(parent, side)
        raise ValueError(f'{value} not found')

    def _search_max(self):
        node = self
        while node:
            parent = node
            node = node.right
        return parent

    def _delete_max(self):
        """Delete max node and Return new root."""
        if not self.right:
            # self is max, so delete self.
            return self.left

        grand = self
        parent = grand.right
        child = parent.right
        while child:
            grand = grand.right
            parent = parent.right
            child = child.right

        # parent is max, so delete parent.
        grand.right = parent.left
        return self

    # 4.2. delete_right
    def delete_right(self, value):
        parent, side, deleted = self._search_parent(value)
        if deleted.right:
            promoted = deleted.right._search_min()
            promoted.right = deleted.right._delete_min()  # a)
            promoted.left = deleted.left  # b)
            # a, b を逆にしてハマる...
        else:
            promoted = deleted.left

        # if self is not deleted,
        # if root is not deleted,
        if parent:
            setattr(parent, side, promoted)
            return self
        else:
            return promoted

    def _search_min(self):
        node = self
        while node:
            parent = node
            node = node.left
        return parent

    def _delete_min(self):
        """Delete min node and return new root."""
        if not self.left:
            return self.right

        grand = self
        parent = grand.left
        child = parent.left
        while child:
            grand = grand.left
            parent = parent.left
            child = child.left
        #
        grand.left = parent.right
        return self


#
# Path
#
class Iterator:
    def __init__(self, node):
        pseudo_node = BinarySearchNode(None)
        pseudo_node.right = node
        self._route = [pseudo_node]

    def __next__(self):
        if self._current_node().right:
            self._seek_right_min()
        else:
            self._seek_right_parent()
        return self._current_node().value

    def _seek_right_min(self):
        self._route.append(self._current_node().right)
        while self._current_node().left:
            self._route.append(self._current_node().left)

    def _seek_right_parent(self):
        try:
            while self._route.pop() == self._current_node().right:
                pass
        except IndexError:
            raise StopIteration

    def _current_node(self):
        return self._route[-1]

    def __iter__(self):
        return self
