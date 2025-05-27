def search(node, target):
  if not node:
    return False

  if node.val == target:
    return True

  return search(node.left, target) or search(node.right, target)
