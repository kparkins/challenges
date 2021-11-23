from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    result = deque()
    nodes = deque()
    nodes.append(root)
    while len(nodes) > 0:
        temp = [] 
        for _ in range(len(nodes)):
            node = nodes.popleft()
            temp.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        result.appendleft(temp)
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))

if __name__ == '__main__':  
    main()
