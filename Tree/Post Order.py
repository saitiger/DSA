def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val)
