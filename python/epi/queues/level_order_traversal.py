
from collections import deque


class Node:

    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val


def get_level_order(root):
    result = []
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        level = []
        level_length = len(queue)
        for _ in range(level_length):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def test_level_order():
    tree = Node(0, Node(1, Node(3, None, None), Node(4, None, None)),
                Node(2, Node(5, None, None), Node(6, None, None)))
    assert [[0], [1, 2], [3, 4, 5, 6]] == get_level_order(tree)
