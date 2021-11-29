class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_sum_of_path_numbers(root, current_path):
    if root is None:
        return 0 
    s = 10 * current_path + root.val
    if root.left is None and root.right is None:
        return s
    return _find_sum_of_path_numbers(root.left, s) + _find_sum_of_path_numbers(root.right, s)


def find_sum_of_path_numbers(root):
    return _find_sum_of_path_numbers(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


if __name__ == '__main__':
    main()
