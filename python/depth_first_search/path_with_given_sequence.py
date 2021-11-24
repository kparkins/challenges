class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_path(root, sequence, index):
    if root is None or index >= len(sequence) or root.val != sequence[index]:
        return False
    if root.left is None and root.right is None and index == len(sequence) - 1:
        return True
    return _find_path(root.left, sequence, index + 1) or _find_path(root.right, sequence, index + 1)    

def find_path(root, sequence):
    return _find_path(root, sequence, 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


if __name__ == '__main__':
    main()
