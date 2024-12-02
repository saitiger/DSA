class Solution:
    def deleteAllOccurOfX(self, head, x):
        def deleteNode(head, delete):
            if (head == None or delete == None):
                return None
         
            # If node to be deleted is head node
            if (head == delete):
                head = delete.next
         
            if (delete.next != None):
                delete.next.prev = delete.prev
         
            if (delete.prev != None):
                delete.prev.next = delete.next

          return head
     
        if (head == None):
            return
     
        current = head
        while (current != None):
            if (current.data == x):
                next = current.next
                head = deleteNode(head, current)
                current = next
           else:
                current = current.next     
        return head
