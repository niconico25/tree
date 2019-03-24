#
# Iterator
#
from .sequencial import BinarySearchNode as Sequencial


class BinarySearchNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    #
    # 1. insert
    #
    def insert(self, value):
        child = self
        while child:
            parent = child
            side = 'left' if value <= child.value else 'right'
            child = getattr(parent, side)
        parent._connect(side, BinarySearchNode(value))

    #
    # 2. search
    #
    search = Sequencial.search

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
            # 1) promoted
            promoted = deleted.left._search_max()

            # 2) promoted.left
            deleted_left = deleted.left
            deleted._cut('left')
            promoted._connect('left', deleted_left._delete_max())

            # 3)
            deleted_right = deleted.right
            deleted._cut('right')
            promoted._connect('right', deleted_right)
        else:
            promoted = deleted.right

        # if self is not deleted,
        # if root is not deleted,
        if parent:
            parent._cut(side)
            parent._connect(side, promoted)
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
        assert not self.parent, 'self should be root.'

        if not self.right:
            # self is max, so delete self.
            self_left = self.left
            self._cut('left')
            return self_left

        grand = self
        parent = grand.right
        child = parent.right
        while child:
            grand = grand.right
            parent = parent.right
            child = child.right

        # parent is max, so delete parent.
        #
        #       grand
        #          \
        #          --- cut
        #            \
        #           parent
        #           /   \
        #     cut ---    \
        #         /       \
        # parent_left      child(None)
        #
        parent_left = parent.left
        grand._cut('right')
        parent._cut('left')
        grand._connect('right', parent_left)
        return self

    # 4.2. delete_right
    def delete_right(self, value):
        parent, side, deleted = self._search_parent(value)
        if deleted.right:
            # 1) promoted
            promoted = deleted.right._search_min()

            # 2) promoted.right
            deleted_right = deleted.right
            deleted._cut('right')
            promoted._connect('right', deleted_right._delete_min())

            # 3)
            deleted_left = deleted.left
            deleted._cut('left')
            promoted._connect('left', deleted_left)
        else:
            promoted = deleted.left

        # if self is not deleted,
        # if root is not deleted,
        if parent:
            parent._cut(side)
            parent._connect(side, promoted)
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
        assert not self.parent, 'self should be root.'

        if not self.left:
            self_right = self.right
            self._cut('right')
            return self_right

        grand = self
        parent = grand.left
        child = parent.left
        while child:
            grand = grand.left
            parent = parent.left
            child = child.left
        #
        parent_right = parent.right
        grand._cut('left')
        parent._cut('right')
        grand._connect('left', parent_right)
        return self

    #
    # 5. Connect and Cut
    #
    def _connect(self, side, child):
        setattr(self, side, child)
        if child:
            setattr(child, 'parent', self)

    def _cut(self, side):
        child = getattr(self, side)
        setattr(self, side, None)
        if child:
            setattr(child, 'parent', None)


class Iterator:
    def __init__(self, root):
        pseudo_node = BinarySearchNode(None)
        pseudo_node.right = root
        self._current_node = pseudo_node

    def __next__(self):
        if self._current_node.right:
            self._seek_right_min()
        else:
            self._seek_right_parent()
        return self._current_node.value

    def _seek_right_min(self):
        self._current_node = self._current_node.right
        while self._current_node.left:
            self._current_node = self._current_node.left

    def _seek_right_parent(self):
        while True:
            prev_node = self._current_node
            self._current_node = self._current_node.parent
            try:
                right_node = self._current_node.right
            except AttributeError:
                raise StopIteration

            if right_node is not prev_node:
                break
