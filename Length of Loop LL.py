class Solution:
    def length_of_loop(slow,fast):
      cnt = 1
      temp = slow
      while temp.next != slow:
        cnt+= 1
        temp = temp.next
      return cnt 
    def countNodesInLoop(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return length_of_loop(slow,fast)
        return 0
