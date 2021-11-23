
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    if root is None:
        return result
    queue.append(root)
    while len(queue) > 0: 
        level = []
        num_elements = len(queue)
        for _ in range(num_elements): 
            element = queue.popleft()
            level.append(element.val)
            if element.left is not None:
                queue.append(element.left)
            if element.right is not None:
                queue.append(element.right)
        result.append(level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


if __name__ == '__main__':
    main()
