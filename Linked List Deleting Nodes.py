# 1) Deleting new node at beginning 

# Representation of a singly Linked-List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
# Function for printing LL representation 
def print_list(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.next

def delete_head(head):
      if head is None:
        return None
    temp = head  # Store the current head in a temporary variable to not tamper the original head.
    head = head.next
    del temp
    return head

# 2) Deleting new node at last node 
def delete_tail(head):
      temp = head
      if head is None or head.next is None: # If LL has either zero or one element return None
        return None 
      while temp.next.next is not None:
        temp = temp.next
      temp.next = None
      return head

# 3) Delete Kth Element 
def deleteK(head, k):
    if head is None:
        return head
    if k == 1:
        temp = head
        head = head.next
        temp = None
        return head
    temp = head
    prev = None
    cnt = 0
    while temp is not None:
        cnt += 1
        if cnt == k:
            prev.next = prev.next.next
            temp = None
            break
        prev = temp
        temp = temp.next
    return head

# 4) Delete for Value K 
class Solution:
def delete_val(head, k):
        temp = head
        if head is None:
          return None
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head.next
