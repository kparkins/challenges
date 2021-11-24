from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    nodes = deque([root])
    while len(nodes) > 0:
        num_siblings = len(nodes)
        for i in range(num_siblings):
            node = nodes.popleft()
            if i == num_siblings - 1:
                result.append(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


if __name__ == '__main__':
    main()
