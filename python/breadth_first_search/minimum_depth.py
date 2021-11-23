from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    depth = 1
    nodes = deque([root])
    while len(nodes) > 0:
        num_nodes = len(nodes)
        for _ in range(num_nodes):
            node = nodes.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        depth += 1 
    return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


if __name__ == '__main__':
    main()
