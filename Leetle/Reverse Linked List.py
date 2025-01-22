# Singly Linked List Definition
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solve(head):
    curr = head 
    prev = None

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt

    return prev
