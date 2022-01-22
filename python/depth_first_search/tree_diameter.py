class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def _find_diameter(self, root):
        if root is None:
            return 0
        left_height = self._find_diameter(root.left)
        right_height = self._find_diameter(root.right)
        self.treeDiameter = max(self.treeDiameter, left_height + right_height + 1)
        return max(left_height, right_height) + 1 

    def find_diameter(self, root):
        self.treeDiameter = 0
        self._find_diameter(root)
        return self.treeDiameter

def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


if __name__ == '__main__':
    main()
