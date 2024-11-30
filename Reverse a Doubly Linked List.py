# Solution 1 Using Stack 

def reverse_dll(head):
    if head is None or head.next is None:
        return head

    stk = []
    temp = head

    while temp is not None:
        stk.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.data = stk.pop()
        temp = temp.next
    return head

# Solution 2 
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node
      
def reverse_dll(head):
    if head is None or head.next is None:
        return head
    
    prev = None  
    current = head  

    while current is not None:
        prev = current.back 
        # Swap the previous and next pointers
        current.back = current.next
        # Reversing the links
        current.next = prev 
        # Move to the next node in the original list
        current = current.back  
    return prev.back
