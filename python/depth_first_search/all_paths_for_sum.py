class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_paths_recursive(root, s, paths, current_path):
    if root is None or s - root.val < 0:
        return
    if root.left is None and root.right is None and s - root.val == 0:
        paths.append(current_path + [root.val])
        return
    _find_paths_recursive(root.left, s - root.val, paths,
                          current_path + [root.val])
    _find_paths_recursive(root.right, s - root.val,
                          paths, current_path + [root.val])


def find_paths(root, s):
    results = []
    _find_paths_recursive(root, s, results, [])
    return results


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


if __name__ == '__main__':
    main()
