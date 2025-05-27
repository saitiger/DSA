# Recursive 
def pre_order(node):
  if not node:
    return

  print(node)
  pre_order(node.left)
  pre_order(node.right)

pre_order(A)

# Iterative
def pre_order_iterative(node):
  stk = [node]

  while stk:
    node = stk.pop()
    if node.right: stk.append(node.right)
    if node.left: stk.append(node.left)
    print(node)

pre_order_iterative(A)
