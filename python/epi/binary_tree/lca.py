from binary_tree import Node
'''
class Node:

    def __init__(self, data, left, right, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
'''

def _calc_path_length(child, parent):
    length = 0 
    while child and child != parent:
        child = child.parent
        length += 1
    return length

def find_lca(root, node1, node2):
    if not node1 or not node2 or not root:
        return root
    len1 = _calc_path_length(node1, root) 
    len2 = _calc_path_length(node2, root) 
    short = node1 if len1 < len2 else node2 
    long = node1 if short == node2 else node2
    difference = abs(len1 - len2) 
    while difference > 0:
        long = long.parent
        difference -= 1
    while long != short:
        long = long.parent
        short = short.parent
    return long


def test_find_lca():
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

    assert find_lca(root, None, None) == root
    assert find_lca(root, left, right) == root
    assert find_lca(root, leftleft, rightright) == root
    assert find_lca(root, leftrightright, rightright) == root
    
    assert find_lca(root, leftleft, leftright) == left
    assert find_lca(root, leftleft, leftrightright) == left
    assert find_lca(root, leftright, leftrightright) == leftright
