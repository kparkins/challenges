from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  nodes = deque()
  nodes.append(root)
  reverse = False
  while len(nodes) > 0: 
        temp = deque()
        num_nodes = len(nodes)      
        for _ in range(num_nodes):
            node = nodes.popleft()
            if reverse:
                temp.appendleft(node.val)
            else:
                temp.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        reverse = not reverse
        result.append(list(temp))
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
