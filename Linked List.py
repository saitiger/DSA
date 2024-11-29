# Singly Linked List

class SinglyNode:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val)

# Doubly Linked List

class DoublyNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

  def __str__(self):
    return str(self.val)

# Search for node value 
def search(head, val):
  curr = head
  while curr:
    if val == curr.val:
      return True
    curr = curr.next

  return False

search(Head, 7)

# Insert at beginning 
def insert_at_beginning(head, tail, val):
  new_node = DoublyNode(val, next=head)
  head.prev = new_node
  return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

# Insert at end 
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
