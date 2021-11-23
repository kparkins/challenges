from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

    def print_next_order(self):
        print('{} '.format(self.val), end='')
        cursor = self.next
        while cursor:
            print('{} '.format(cursor.val), end='')
            cursor = cursor.next
        print()


def connect_level_order_siblings(root):
    nodes = deque([root])
    while len(nodes) > 0:
        prev_node = None
        num_siblings = len(nodes)
        for _ in range(num_siblings):
            current_node = nodes.popleft()
            if prev_node is not None:
                prev_node.next = current_node
            if current_node.left:
                nodes.append(current_node.left)
            if current_node.right:
                nodes.append(current_node.right)
            prev_node = current_node


def connect_all_sublings(root):
    prev_node = None
    nodes = deque([root])
    while len(nodes) > 0:
        node = nodes.popleft()
        if prev_node:
            prev_node.next = node
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        prev_node = node


def setup():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    return root


def main():
    root = setup()
    print('Connect level order: \n')
    connect_level_order_siblings(root)
    root.print_level_order()

    root = setup()
    print('\nConnect all siblings: \n')
    connect_all_sublings(root)
    root.print_next_order()


if __name__ == '__main__':
    main()
