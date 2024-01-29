class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

def generate_trees(start, end):
  if start > end:
      return [None]

  all_trees = []

  for i in range(start, end + 1):
      left_trees = generate_trees(start, i - 1)
      right_trees = generate_trees(i + 1, end)

      for left_tree in left_trees:
          for right_tree in right_trees:
              root = TreeNode(i)
              root.left = left_tree
              root.right = right_tree
              all_trees.append(root)

  return all_trees

def preorder(root, result):
  if root:
      result.append(root.value)
      preorder(root.left, result)
      preorder(root.right, result)

def print_unique_bsts(n):
  if n == 0:
      return []

  all_trees = generate_trees(1, n)

  for tree in all_trees:
      result = []
      preorder(tree, result)
      print(result)

n = 3
print_unique_bsts(n)
