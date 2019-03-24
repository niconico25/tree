"""Create tree images using graphviz.

#
# sample code
#
from tree.binary_search_tree import BinarySearchTree
from tree.display.graph import render

n = -1
bst = BinarySearchTree()
for i in 8, 3, 1, 6, 10, 4, 7, 14, 13:
    n += 1
    bst.insert(i)
    render(bst, 3, 'img_%02d' % n)

n += 1
bst.delete_left(8)
render(bst, 3, 'img_%02d' % n)

n += 1
bst.delete_right(7)
render(bst, 3, 'img_%02d' % n)

n += 1
bst.delete_right(3)
render(bst, 3, 'img_%02d' % n)
"""
import graphviz
import random
import string
from . import text


def source(binary_search_tree, max_depth=0):
    diagraph = _create_diagraph(binary_search_tree, max_depth)
    return diagraph.source


def render(binary_search_tree, max_depth=0, file_name='sample'):
    diagraph = _create_diagraph(binary_search_tree, max_depth)
    diagraph.render('img/' + file_name, cleanup=True)


def _create_diagraph(binary_search_tree, max_depth=0):
    #
    root = binary_search_tree.root
    node_list = [node for node in text.node_generator(root)]
    route_list = [list(text._route(root, node)) for node in node_list]
    depth_list = [len(route) - 1 for route in route_list]
    max_depth = max_depth if max_depth else max(depth_list)
    height_list = [max_depth - depth for depth in depth_list]

    #
    diagraph = graphviz.Digraph('BST', format='png')
    for node, height in zip(node_list, height_list):
        diagraph.node(str(id(node)), str(node.value))
        if node.left:
            diagraph.edge(str(id(node)), str(id(node.left)))
        elif height:
            _brank_edge(diagraph, str(id(node)), height)
        if node.right:
            diagraph.edge(str(id(node)), str(id(node.right)))
        elif height:
            _brank_edge(diagraph, str(id(node)), height)
    return diagraph


def _brank_edge(diagraph, identity, height):
    diagraph.edge(identity, _blank_tree(diagraph, height - 1), color='gray91')


def _blank_tree(diagraph, height):
    lowercase = string.ascii_lowercase
    identity = ''.join([random.choice(lowercase) for _ in range(10)])
    diagraph.node(identity, '', color='gray91')
    if height:
        _brank_edge(diagraph, identity, height)
        _brank_edge(diagraph, identity, height)
    return identity
