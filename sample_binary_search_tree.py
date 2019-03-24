from random import randint
from random import shuffle
from tree.binary_search_tree import BinarySearchTree
# from tree.binary_search_tree.recursive import BinarySearchNode
# from tree.binary_search_tree.sequencial import BinarySearchNode
from tree.binary_search_tree.parental import BinarySearchNode


bst = BinarySearchTree(BinarySearchNode)

#
# 1) Insert
#
lst = [randint(1, 5) for _ in range(10)]
for i in lst:
    bst.insert(i)
    print()
    print('# insert', i)
    print(bst)
    print(bst.list())

#
# 2) Delete
#
shuffle(lst)
for i in lst:
    # bst.delete_left(i)
    bst.delete_right(i)
    print()
    print('# delete', i)
    print(bst)
    print(list(bst))
