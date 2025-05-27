def in_order(node):
  if not node:
    return

  in_order(node.left)
  print(node)
  in_order(node.right)

in_order(A)
