class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _count_paths_recursive(root, s, current_path):
    if root == None:
        return 0
    path_count = 0
    current_sum = 0
    current_path.append(root)
    for i in range(len(current_path) - 1, -1, -1):
        current_sum += current_path[i].val
        if current_sum == s:
            path_count += 1
    path_count += _count_paths_recursive(root.left, s, current_path)
    path_count += _count_paths_recursive(root.right, s, current_path)
    current_path.pop()
    return path_count


def count_paths(root, s):
    return _count_paths_recursive(root, s, [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


if __name__ == '__main__':
    main()
