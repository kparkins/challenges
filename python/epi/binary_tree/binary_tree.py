

class Node:

    def __init__(self, data, left, right, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data


def _calculate_height(node):
    if node is None:
        return 0
    left_height = _calculate_height(node.left)
    right_height = _calculate_height(node.right)
    return max(left_height, right_height) + 1


def _height_balance(node):
    if node is None:
        return 0, True
    left_height, left_balanced = _height_balance(node.left)
    if not left_balanced:
        return -1, False
    right_height, right_balanced = _height_balance(node.right)
    if not right_balanced:
        return -1, False
    max_height = max(left_height, right_height) + 1
    return max_height, left_balanced and right_balanced and abs(left_height - right_height) <= 1


def is_height_balanced(root):
    max_height, balanced = _height_balance(root)
    return balanced


def _is_symmetric(left_cursor, right_cursor):
    if not left_cursor and not right_cursor:
        return True
    elif left_cursor and right_cursor:

        if left_cursor.data != right_cursor.data:
            return False
        return _is_symmetric(left_cursor.left, right_cursor.right) and \
            _is_symmetric(left_cursor.right, right_cursor.left)
    return False


def is_symmetric(root):
    return _is_symmetric(root.left, root.right)


def reconstruct_tree(preorder, inorder):
    inorder_index_map = {inorder[i]: i for i in range(len(inorder))}

    def _reconstruct(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None
        node = Node(preorder[preorder_start], None, None)
        root_index = inorder_index_map[node.data]
        left_subtree_size = root_index - inorder_start + 1
        node.left = _reconstruct(
            preorder_start + 1, preorder_start + left_subtree_size, inorder_start, root_index)
        node.right = _reconstruct(
            preorder_start + left_subtree_size, preorder_end, root_index + 1, inorder_end)

    return _reconstruct(0, len(preorder), 0, len(inorder))


def inorder_traversal(node):
    def sucessor(node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        parent = node.parent
        while parent and node != parent.left:
            parent = parent.parent
            node = node.parent
        return parent

    cursor = node
    while cursor and cursor.left:
        cursor = cursor.left
    result = []
    while cursor:
        result.append(cursor.data)
        cursor = sucessor(cursor)
    return result


def test_is_height_balanced():
    tree = Node(2, Node(1, None, None), Node(3, None, None))
    assert is_height_balanced(tree)

    tree = Node(2, Node(1, Node(4, None, None), None), Node(3, None, None))
    assert is_height_balanced(tree)

    tree = Node(2, Node(1, Node(4, Node(5, None, None), None),
                None), Node(3, None, None))
    assert not is_height_balanced(tree)


def test_is_symmetric():

    root = Node(0, None, None)
    left = Node(1, None, None)
    right = Node(1, None, None)

    leftright = Node(4, None, None)
    rightleft = Node(4, None, None)

    root.left = left
    root.right = right

    left.right = leftright
    right.left = rightleft

    assert is_symmetric(root)

    rightright = Node(5, None, None)
    right.right = rightright

    assert not is_symmetric(root)


def test_inorder_traversal():
    root = Node(0, None, None)
    left = Node(1, None, None)
    right = Node(2, None, None)

    leftleft = Node(3, None, None)
    leftright = Node(4, None, None)
    rightright = Node(5, None, None)
    leftrightright = Node(6, None, None)

    root.left = left
    root.right = right

    left.parent = root
    left.left = leftleft
    left.right = leftright

    right.parent = root
    right.right = rightright

    rightright.parent = right

    leftleft.parent = left

    leftright.parent = left
    leftright.right = leftrightright

    leftrightright.parent = leftright
    print(inorder_traversal(root))
