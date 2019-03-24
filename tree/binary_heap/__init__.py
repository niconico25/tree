from ..display.text import str_tree  # type: ignore


class BinaryHeap:
    def __init__(self, sequence):
        pseudo_root = BinaryHeapNode(None)
        for i, e in enumerate(sequence):
            self._insert(pseudo_root, i, e)
        self.root = pseudo_root.right

    @staticmethod
    def _insert(pseudo_root, i, e):
        i = i + 1
        s = list(reversed(bin(i)[2:]))
        d = {'0': 'left', '1': 'right'}
        child = pseudo_root

        while s:
            parent = child
            side = d[s.pop()]
            child = getattr(parent, side)

        assert not child
        setattr(parent, side, BinaryHeapNode(e))

    __str__ = str_tree


class BinaryHeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
