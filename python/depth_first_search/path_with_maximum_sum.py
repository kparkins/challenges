import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_max_path_sum(root):
    if root is None:
        return 0, -math.inf
    left_path_sum, left_max = _find_max_path_sum(root.left)
    right_path_sum, right_max = _find_max_path_sum(root.right)
    left_path_sum = max(left_path_sum, 0)
    right_path_sum = max(right_path_sum, 0)
    current_sum = left_path_sum + right_path_sum + root.val 
    return max(left_path_sum, right_path_sum) + root.val, max(left_max, max(right_max, current_sum))


def find_maximum_path_sum(root):
    r, max_so_far = _find_max_path_sum(root) 
    return max_so_far

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


if __name__ == '__main__':
    main()
