from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def find_level_averages(root):
    result = []
    nodes = deque([root])
    while len(nodes) > 0:
        total = 0
        num_nodes = len(nodes)
        for _ in range(num_nodes):
            node = nodes.popleft()
            total += node.val
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        result.append(total / num_nodes)
    return result 

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


if __name__ == '__main__':
    main()







