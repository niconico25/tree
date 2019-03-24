def str_tree(tree):
    return str_node(tree.root)


def str_node(root):
    #
    if not root:
        return '\n'

    #
    if not all(0 <= value <= 99 for value in _value_generator(root)):
        raise ValueError('A value shoud be between 0 and 99.')

    #
    depth_list, position_list, value_list = _str_node(root)

    # Create layer_list.
    layer_len = (4 * 2**max(depth_list) - 2)
    layer = ' ' * layer_len
    layer_list = [layer] * (max(depth_list) + 1)
    for depth, position, value\
            in zip(depth_list, position_list, value_list):
        layer_list[depth] = _paste(
            pasted=layer_list[depth], seal=value, position=position,)

    #
    return '\n'.join(layer_list)


def _str_node(root):
    node_list = [node for node in node_generator(root)]
    route_list = [list(_route(root, node)) for node in node_list]
    value_list = [str(value).zfill(2) for value in _value_generator(root)]
    index_list = [_index(_path(route)) for route in route_list]
    depth_list = [len(route) - 1 for route in route_list]
    height_list = [max(depth_list) - depth for depth in depth_list]
    position_list = [_position(height, index) for height, index in
                     zip(height_list, index_list)]
    return depth_list, position_list, value_list


def node_generator(binary_search_node):
    bsn = binary_search_node
    if bsn.left:
        yield from node_generator(bsn.left)
    yield bsn
    if bsn.right:
        yield from node_generator(bsn.right)


def _value_generator(binary_search_node):
    bsn = binary_search_node
    if bsn.left:
        yield from _value_generator(bsn.left)
    yield bsn.value
    if bsn.right:
        yield from _value_generator(bsn.right)


def _route(root, node):
    """Search node by depth first search."""
    pseudo_root = type(node)(None)
    pseudo_root.right = root
    route = [pseudo_root]

    while route[-1] is not node:
        if route[-1].right:
            _seek_right_min(route)
        else:
            _seek_right_parent(route)

    del route[0]
    yield from (e for e in route)


def _seek_right_min(route):
    node = route[-1]

    # Down right side 1 time.
    route.append(node.right)
    node = route[-1]

    # Down left side until reaching a leaf.
    while node.left:
        route.append(node.left)
        node = route[-1]


def _seek_right_parent(route):
    # Up left side while a node is right side child.
    while True:
        node, parent = route.pop(), route[-1]
        if node is parent.left:
            break


#
def _path(route):
    path = []
    iterator = iter(route)
    next(iterator)
    for parent, child in zip(route, iterator):
        path.append(0 if parent.left is child else 1)
    return path


def _index(path):
    index = 0
    n = len(path)
    for digit, exponent in zip(path, reversed(range(n))):
        index += digit * 2**exponent
    return index


def _paste(pasted, seal, position):
    pasted = list(pasted)
    for i, c in enumerate(seal):
        pasted[position + i] = c
    return ''.join(pasted)


def _position(height, index):
    initial = 2 * (2**height - 1)
    space = 4 * 2**height
    position = initial + space * index
    return position


#
#
#
def register_printer(BinarySearchTree):
    BST = BinarySearchTree
    BST.insert = _register_printer(BST.insert)
    BST.delete_left = _register_printer(BST.delete_left)
    BST.delete_right = _register_printer(BST.delete_right)


def _register_printer(func):
    def decorated_func(binary_search_tree, *args, **kwargs):
        value = args[0]
        if not(0 <= value <= 99):
            raise ValueError('A value shoud be between 0 and 99.')

        result = func(binary_search_tree, *args, **kwargs)

        print(binary_search_tree)
        return result
    return decorated_func
