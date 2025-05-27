from collections import deque

def level_order(node):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)

level_order(A)
