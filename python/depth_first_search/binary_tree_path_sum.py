class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, path_sum):
    if root is None or path_sum < 0:
        return False
    if root.left is None and root.right is None:
        return path_sum - root.val == 0
    return has_path(root.left, path_sum - root.val) or has_path(root.right, path_sum - root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


if __name__ == '__main__':
    main()
