# python3 tree_binary_search_tree.py
import unittest
import random
from tree.binary_search_tree import BinarySearchTree
from tree.binary_search_tree import recursive
from tree.binary_search_tree import sequencial
from tree.binary_search_tree import parental


def main():
    """Test three types of binary search tree."""
    module_list = [
        recursive,
        sequencial,
        parental,
    ]

    for module in module_list:
        Test.BinarySearchNode = module.BinarySearchNode
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
        unittest.TextTestRunner().run(suite)


class Test(unittest.TestCase):
    BinarySearchNode = None

    def test_insert_list_delete_left(self):
        # insert, list
        bst = BinarySearchTree(self.BinarySearchNode)
        lst = [random.randint(0, 99) for value in range(1000)]
        for value in lst:
            bst.insert(value)
        self.assertEqual(bst.list(), sorted(lst))

        # delete_left
        random.shuffle(lst)
        for value in lst:
            bst.delete_left(value)
        self.assertEqual(bst.list(), [])

    def test_insert_iterator_delte_right(self):
        # insert, list
        bst = BinarySearchTree(self.BinarySearchNode)
        lst = [random.randint(0, 99) for value in range(1000)]
        for value in lst:
            bst.insert(value)
        self.assertEqual(list(bst), sorted(lst))

        # delete_right
        random.shuffle(lst)
        for value in lst:
            bst.delete_right(value)
        self.assertEqual(bst.list(), [])


if __name__ == '__main__':
    main()


"""
The following code looks a little bit odd,
because we pass two parameters via class variable.

def main():
    for module in module_list:
        Test.BinarySearchNode = module.BinarySearchNode


Is it good, passing parameters to unittest?
It might be wrong, I'm not sure...
But I'm nothing come up with an idea without using class variable.
I'm wondering about whether there is any better way?

> Python unittest passing arguments - stackoverflow
> https://bit.ly/2QufwCK
>
> To extend with the above comment about unit tests.
> Unit tests should stand alone in that they have no dependencies
> outside of their setup and tear down requirements,
> such as in your case setting up a email.
>
> This makes sure that each tests has
> very specific side effects and reactions to the test.
> Passing in a parameter defeats this property of unit tests
> and thus makes them in a sense invalid.
>
> Using a test configuration would be the easiest way and-also more proper
> because again a unit test should never rely on
> outside information to perform the test.
> That is for integration tests.
"""
